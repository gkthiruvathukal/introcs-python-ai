Multiple Function Definitions
==============================

.. note::

   *Source:* Adapted from the C# edition (``functions/multfunc.rst``).
   The ``if __name__ == '__main__':`` pattern is a Python-specific original
   addition.

A program can contain as many function definitions as needed.  Functions can
call other functions.

.. index:: function; multiple definitions

Example: Two Birthday Songs
----------------------------

.. literalinclude:: ../../examples/introcs-python/functions/birthday.py
   :language: python
   :start-after: # start: birthday_functions
   :end-before: # end: birthday_functions

Output:

.. code-block:: none

   Happy Birthday to you!
   Happy Birthday to you!
   Happy Birthday, dear Emily.
   Happy Birthday to you!

   Happy Birthday to you!
   Happy Birthday to you!
   Happy Birthday, dear Andre.
   Happy Birthday to you!

This works, but notice the duplication — the two functions are nearly
identical.  The next section shows how to eliminate it using parameters.

.. index:: function; definition order, NameError; undefined function

Order of Definitions and Calls
-------------------------------

A function must be *defined* before it is *called*.  In a script, definitions
typically appear at the top and calls at the bottom:

.. code-block:: python

   def greet():
       print("Hello!")

   greet()      # OK — defined above

The following would fail:

.. code-block:: python

   greet()      # NameError — not yet defined

   def greet():
       print("Hello!")

The ``if __name__ == '__main__':`` pattern (from the Program Structure section)
keeps calls cleanly separated from definitions:

.. literalinclude:: ../../examples/introcs-python/functions/birthday.py
   :language: python
