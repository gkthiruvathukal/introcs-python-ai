.. index:: string; problem solving
   problem solving

.. _solve-string-replace:

A Creative Problem Solution
============================

.. note::

   *Source:* Problem statement, incremental-development approach, and
   test-first framing adapted from the C# edition
   (``basicstringops/problem-solving-replace.rst``).  The Python
   implementation using ``find`` and slicing is an original adaptation
   (the C# version used ``Substring`` and ``IndexOf``).

The exercises so far have been straightforward: learn a method, apply it.
Now we introduce a *problem-solving* exercise to practice combining
what you know in a less obvious way.

The Problem
-----------

Given a string such as ``"It was the best of times."``, find and replace
the *first* occurrence of one substring (``"best"``) with another
(``"worst"``), producing ``"It was the worst of times."``.

Python's ``str.replace()`` already does this, so for this exercise we
will **implement it ourselves** using only indexing, slicing, and
``find()``.  The goal is problem-solving practice, not reinventing the
standard library.

.. index:: test-first development, function; signature

Function Signature and Tests First
-----------------------------------

Before writing the body, define the interface and write test cases.  This
is a form of *test-first development*: write tests that describe what the
function must do, then make them pass.

.. code-block:: python

   def string_replace(s: str, target: str, replacement: str) -> str:
       """Return s with the first occurrence of target replaced by replacement.

       If target is not in s, return s unchanged.
       """
       pass   # to be implemented


   def main() -> None:
       print(string_replace("It was the best of times.", "best", "worst"))
       # expected: It was the worst of times.
       print(string_replace("abcabc", "bc", "X"))
       # expected: aXabc
       print(string_replace("hello", "xyz", "Q"))
       # expected: hello  (target not found)
       print(string_replace("aaaa", "aa", "B"))
       # expected: Baaa  (only first occurrence)

   if __name__ == '__main__':
       main()

Running this with ``pass`` as the body will print ``None`` four times —
but the test structure is in place.

.. index:: incremental development, pair: problem solving; incremental

Building the Solution Incrementally
-------------------------------------

A common mistake is to try to write the whole function at once.  Instead,
build it in small steps, testing after each one.

**Step 1 — Find the location of target**

We need to know *where* the target is.  Use ``find()``:

.. code-block:: python

   i = s.find(target)

If ``target`` is not in ``s``, ``find()`` returns ``-1``.  Handle that
case first:

.. code-block:: python

   def string_replace(s: str, target: str, replacement: str) -> str:
       i = s.find(target)
       if i == -1:
           return s      # nothing to replace

Now the third test already passes.

**Step 2 — Visualize the pieces**

For ``s = "It was the best of times."`` and ``target = "best"``:

.. code-block:: none

   Index: 0         1         2
          0123456789012345678901234
       s: It was the best of times.

``find("best")`` returns 12.  We need three pieces:

- Everything *before* the target: ``s[:i]``          → ``"It was the "``
- The replacement itself:          ``replacement``     → ``"worst"``
- Everything *after* the target:   ``s[i + len(target):]``  → ``" of times."``

**Step 3 — Concatenate the pieces**

.. literalinclude:: ../../examples/introcs-python/basicstringops/string_replace.py
   :language: python
   :start-after: # start: string_replace
   :end-before: # end: string_replace

All four tests should now pass.  Run and verify.

Reflection
----------

A few lessons from this exercise:

- **Write tests first.**  They clarify the goal and let you check progress
  at each step.
- **Use concrete examples** to find the right index arithmetic before
  writing general code.
- **Build incrementally.**  Handle the easy case (not found) first, then
  the main case.
- **``len(target)``** is what you need to skip past the target — not a
  literal ``4`` or ``5``.

Of course, in real code you would just write
``s.replace(target, replacement, 1)``.  But walking through the
implementation teaches you to think with indices, slicing, and
``find()`` — all tools you will need again.
