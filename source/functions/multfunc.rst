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

.. code-block:: python

   def happy_birthday_emily():
       print("Happy Birthday to you!")
       print("Happy Birthday to you!")
       print("Happy Birthday, dear Emily.")
       print("Happy Birthday to you!")


   def happy_birthday_andre():
       print("Happy Birthday to you!")
       print("Happy Birthday to you!")
       print("Happy Birthday, dear Andre.")
       print("Happy Birthday to you!")


   happy_birthday_emily()
   print()
   happy_birthday_andre()

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

The ``if __name__ == '__main__':`` pattern (from :ref:`programstructure`)
keeps calls cleanly separated from definitions:

.. code-block:: python

   def happy_birthday_emily():
       ...

   def happy_birthday_andre():
       ...

   if __name__ == '__main__':
       happy_birthday_emily()
       print()
       happy_birthday_andre()
