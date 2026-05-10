.. index:: input; validation, try/except

User Input Utilities
====================

Python has no built-in library for validated input, but building one is a good
exercise in combining loops, functions, and error handling.

Simple Prompt Helpers
---------------------

The simplest helper re-prompts the user when input cannot be converted:

.. literalinclude:: ../../examples/introcs-python/while/ui.py
   :language: python
   :start-after: # start: prompt_int_float
   :end-before: # end: prompt_int_float

.. index:: try/except

A Brief Note on ``try``/``except``
-----------------------------------

``int(input(...))`` raises a ``ValueError`` if the user types something that
cannot be converted to an integer (like ``"abc"``).  A ``try``/``except``
block catches that error so the program can respond gracefully instead of
crashing:

.. code-block:: none

   try:
       risky_operation()
   except SomeError:
       handle_the_error()

If ``risky_operation()`` raises ``SomeError``, execution jumps to the
``except`` block.  If no error occurs, the ``except`` block is skipped.
Error handling is covered more fully in a later chapter; for now just use
this pattern as written.

.. index:: input; range validation, input; validation loop

Prompting Within a Range
-------------------------

A more useful helper also enforces a valid range:

.. literalinclude:: ../../examples/introcs-python/while/ui.py
   :language: python
   :start-after: # start: prompt_int_in_range
   :end-before: # end: prompt_int_in_range

Sample interaction:

.. code-block:: none

   Enter a score (0-100): 233
   233 is out of range!  Enter a value from 0 to 100.
   Enter a score (0-100): -1
   -1 is out of range!  Enter a value from 0 to 100.
   Enter a score (0-100): 85

Yes/No Prompt
-------------

Another common need is a yes/no confirmation:

.. literalinclude:: ../../examples/introcs-python/while/ui.py
   :language: python
   :start-after: # start: prompt_yes_no
   :end-before: # end: prompt_yes_no

.. index:: module; helper functions, separation of concerns; input

Using the Helpers
-----------------

Collect these functions in a module (e.g., ``ui.py``) and import them:

.. code-block:: python

   from ui import prompt_int, prompt_int_in_range, prompt_yes_no

   age  = prompt_int("Enter your age: ")
   score = prompt_int_in_range("Enter score (0-100): ", 0, 100)
   if prompt_yes_no("Save result?"):
       print(f"Saved: age={age}, score={score}")

These helpers keep your main program free of repetitive validation code —
the same separation-of-concerns idea we applied to computation and output
in the functions chapter.
