.. index:: input, Console; ReadLine equivalent

.. _io:

Combining Input and Output
==========================

Most useful programs need to communicate with the user — asking for data and
reporting results.  In Python this is done with ``input()`` and ``print()``.

.. index:: input function

The ``input()`` Function
------------------------

``input()`` displays a prompt string, waits for the user to type something and
press Enter, and then returns what the user typed as a *string*:

.. code-block:: none

   >>> name = input("What is your name? ")
   What is your name? Alice
   >>> name
   'Alice'
   >>> type(name)
   <class 'str'>

The result is *always* a string, regardless of what the user types.

.. index:: type conversion, int(), float()

Converting Input to Numbers
----------------------------

Since ``input()`` always returns a string, you must convert to a number if
you need arithmetic.  Use ``int()`` for integers or ``float()`` for decimal
numbers:

.. code-block:: none

   >>> age_str = input("Enter your age: ")
   Enter your age: 20
   >>> age = int(age_str)
   >>> age + 1
   21

You can combine the two steps on one line, which is the most common pattern:

.. code-block:: none

   >>> age = int(input("Enter your age: "))
   Enter your age: 20

   >>> length = float(input("Enter room length: "))
   Enter room length: 20.5
   >>> type(length)
   <class 'float'>

.. warning::

   If the user types something that cannot be converted — for example, typing
   ``"abc"`` when you call ``int()`` — Python raises a ``ValueError`` and
   the program stops.  We cover how to handle this gracefully in the While
   Loops chapter.

A Complete Input/Output Example
---------------------------------

Here is a small program that reads two numbers and prints their sum:

.. code-block:: python

   a = float(input("Enter first number: "))
   b = float(input("Enter second number: "))
   print(f"The sum is {a + b}.")

Sample run:

.. code-block:: none

   Enter first number: 3.5
   Enter second number: 1.5
   The sum is 5.0.

.. index:: input; prompt, input; pattern

Order Matters
-------------

The prompt string in ``input()`` is shown *before* reading, so the user sees
what to type before entering a value.
