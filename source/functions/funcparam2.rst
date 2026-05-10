Multiple Function Parameters
=============================

A function can have more than one parameter.  Parameters are listed in the
``def`` line separated by commas.

.. index:: function; multiple parameters

Example: Addition
-----------------

.. code-block:: python

   def print_sum(a, b):
       total = a + b
       print(f"The sum of {a} and {b} is {total}.")

   print_sum(3, 4)
   print_sum(10, 25)

Output:

.. code-block:: none

   The sum of 3 and 4 is 7.
   The sum of 10 and 25 is 35.

When you call ``print_sum(3, 4)``:
- parameter ``a`` receives the value ``3``
- parameter ``b`` receives the value ``4``

This matching is *positional* — the first argument goes to the first
parameter, the second to the second, and so on.

.. index:: function; keyword arguments

Keyword Arguments
-----------------

You can also pass arguments by name (called *keyword arguments*):

.. code-block:: none

   >>> print_sum(b=4, a=3)
   The sum of 3 and 4 is 7.

With keyword arguments, order does not matter.  We will see keyword arguments
used more heavily later (for example, ``print(end="")`` uses them).

.. index:: function; default parameter values, optional parameter

Default Values
--------------

Parameters can have *default values*.  If the caller omits the argument, the
default is used:

.. code-block:: python

   def greet(name, greeting="Hello"):
       print(f"{greeting}, {name}!")

   greet("Alice")            # uses default greeting
   greet("Bob", "Hi there")  # overrides default

Output:

.. code-block:: none

   Hello, Alice!
   Hi there, Bob!

Parameters with default values must come *after* parameters without defaults.
