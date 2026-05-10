.. index:: recursive descent parser, parsing; recursive descent,
           grammar; arithmetic expressions, AST; expression tree,
           mutual recursion; parser, associativity; grammar
   ACM-IEEE CS2013; PL2 Functional Programming
   ACM-IEEE CS2023; PL2 Functional Programming
   ACM-IEEE CS2013; AL1 Basic Analysis
   ACM-IEEE CS2023; AL1 Basic Analysis
   ACM-IEEE CS2013; PL4 Type Systems
   ACM-IEEE CS2023; PL4 Type Systems

.. _Recursion-Descent-Parser:

Recursive Descent Parsing
==========================

A *recursive descent parser* translates a token sequence into a tree
using one function per grammar rule.  When a grammar rule refers to
another rule, the function calls that other function; when a rule refers
to itself, the function recurses.  This makes the correspondence between
grammar and code almost mechanical.

We will build a calculator that parses and evaluates arithmetic
expressions such as ``2 + 3 * 4`` and ``2 ^ (3 + 1)``, correctly
handling operator precedence and associativity.

.. index:: grammar; operator precedence encoding, operator precedence; grammar layers

The Grammar
-----------

Operator precedence is encoded by layering rules.  Lower-precedence
operators appear *higher* in the grammar and call higher-precedence rules
to collect their operands:

.. code-block:: none

   expr    -> term   (('+' | '-') term)*      addition / subtraction
   term    -> unary  (('*' | '/') unary)*     multiplication / division
   unary   -> ('+' | '-') power | power       unary sign
   power   -> primary ('^' power)?            exponentiation
   primary -> NUMBER | '(' expr ')'           atom or grouped expression

The ``*`` in ``(... term)*`` means "zero or more" and is handled by a
loop.  The ``?`` in ``('^' power)?`` means "zero or one" and is handled
by an ``if``.  ``primary`` calling ``expr`` is *mutual recursion*: it
re-enters the grammar at the top to evaluate a parenthesised
sub-expression.

.. index:: AST; NamedTuple nodes, NamedTuple; AST

AST Nodes
----------

Each node in the *abstract syntax tree* (AST) is a ``NamedTuple``:

.. literalinclude:: ../../examples/introcs-python/recursion/rd_nodes.py
   :language: python
   :start-after: # start: rd_nodes
   :end-before: # end: rd_nodes

``Number`` holds a literal value.  ``UnaryOp`` holds an operator and its
single operand.  ``BinOp`` holds an operator and its two operands.
``Expr`` is a type alias that lets the type checker verify tree structure.

.. index:: tokenizer; arithmetic expression, tokenize module; stdlib

Tokenizing the Input
---------------------

Before parsing, the expression string is split into *tokens* — the
smallest meaningful units (numbers and operators):

.. literalinclude:: ../../examples/introcs-python/recursion/rd_tokenizer.py
   :language: python
   :start-after: # start: rd_tokenizer
   :end-before: # end: rd_tokenizer

Python's built-in ``tokenize`` module does the heavy lifting.
``tokenize_expr`` filters the token stream to only numbers and the seven
allowed operators, discarding whitespace and encoding metadata.

.. code-block:: python

   print(tokenize_expr("2 + 3 * 4"))

Output:

.. code-block:: none

   [('NUMBER', '2'), ('OP', '+'), ('NUMBER', '3'), ('OP', '*'), ('NUMBER', '4')]

.. index:: Parser class; recursive descent, grammar rule; method mapping

The Parser
-----------

The ``Parser`` class holds the token list and a position cursor.  Each
grammar rule becomes one method that advances the cursor and returns an
AST node:

.. literalinclude:: ../../examples/introcs-python/recursion/rd_parser.py
   :language: python
   :start-after: # start: rd_parser
   :end-before: # end: rd_parser

The helper ``_match`` checks whether the current token matches a given
type and value, advances if it does, and returns ``True`` or ``False``.
Each grammar method calls the next-higher-precedence method first, then
loops or recurses over the operator it owns.

.. index:: left-associativity; while loop, right-associativity; recursive call

Left and Right Associativity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Associativity controls how repeated equal-precedence operators group.
``2 - 3 - 4`` is left-associative: ``(2 - 3) - 4 = -5``.
``2 ^ 3 ^ 2`` is right-associative: ``2 ^ (3 ^ 2) = 512``.

The grammar encodes this distinction directly in two patterns:

- **Left-associative** operators (``+``, ``-``, ``*``, ``/``): use a
  ``while`` loop that keeps consuming matching operators and builds the
  tree left-to-right.
- **Right-associative** operators (``^``): use a single ``if`` with a
  *recursive call*, so the right operand is fully evaluated before it
  becomes the right child.

``power`` demonstrates the recursive right-associative pattern:

.. code-block:: python

   def power(self) -> Expr:
       node = self.primary()
       if self._match('OP', '^'):
           node = BinOp(node, '^', self.power())  # right-associative: recurse
       return node

Calling ``self.power()`` on the right side builds the right subtree
first, producing right-to-left grouping.

.. index:: structural recursion; evaluator, pattern matching; AST, match statement; evaluator

Evaluating the AST
-------------------

The evaluator walks the AST using the same recursive structure as the
grammar: a node containing sub-nodes is evaluated by recursively
evaluating those sub-nodes first:

.. literalinclude:: ../../examples/introcs-python/recursion/rd_evaluator.py
   :language: python
   :start-after: # start: rd_evaluator
   :end-before: # end: rd_evaluator

Python 3.10+ ``match`` statements destructure each ``NamedTuple`` variant
cleanly.  The ``Number`` case returns the stored value directly.
``UnaryOp`` and ``BinOp`` each call ``eval_expr`` recursively on their
operand(s) before applying the operator.  This is *structural recursion*:
the recursion follows the shape of the data, mirroring the way the parser
built the tree in the first place.

.. index:: recursive descent parser; end-to-end, calc function; parser

Putting It Together
--------------------

A thin wrapper ties the three phases together:

.. literalinclude:: ../../examples/introcs-python/recursion/rd_calc.py
   :language: python
   :start-after: # start: rd_calc
   :end-before: # end: rd_calc

.. code-block:: python

   print(calc("2 + 3 * 4"))      # multiplication before addition
   print(calc("(2 + 3) * 4"))    # parentheses override precedence
   print(calc("2 ^ 3 ^ 2"))      # right-assoc: 2 ^ (3^2) = 2^9
   print(calc("-5 + 2"))          # unary minus

Output:

.. code-block:: none

   14.0
   20.0
   512.0
   -3.0

Each phase is independently testable: the tokenizer by inspecting its
output list, the parser by printing the AST, and the evaluator by
constructing nodes by hand.  Property-based tests can generate random
valid expressions and compare ``calc()`` against Python's own ``eval()``
to verify correctness across a wide range of inputs.
