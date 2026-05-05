.. index:: f-string, format string

.. _fstrings:

F-Strings and String Formatting
================================

Combining strings with variable values is one of the most common tasks in a
program.  Python's *f-strings* (formatted string literals) are the modern,
readable way to do it.

.. index:: f-string; basic syntax

Basic F-Strings
---------------

An f-string is a string literal prefixed with ``f`` (or ``F``).  Inside the
string, any expression enclosed in curly braces ``{}`` is evaluated and its
value is inserted:

.. code-block:: none

   >>> name = "Alice"
   >>> age = 20
   >>> print(f"My name is {name} and I am {age} years old.")
   My name is Alice and I am 20 years old.

Any Python expression can go inside ``{}``:

.. code-block:: none

   >>> x = 5
   >>> print(f"The square of {x} is {x ** 2}.")
   The square of 5 is 25.

   >>> a, b = 3, 4
   >>> print(f"The hypotenuse is {(a**2 + b**2) ** 0.5:.2f}.")
   The hypotenuse is 5.00.

.. index:: format specifier

Format Specifiers
-----------------

After the expression you can add a *format specifier* separated by a colon to
control how the value is displayed.

**Floating-point precision:**

.. code-block:: none

   >>> pi = 3.141592653589793
   >>> print(f"pi ≈ {pi:.4f}")
   pi ≈ 3.1416

   >>> price = 9.5
   >>> print(f"Price: ${price:.2f}")
   Price: $9.50

**Field width and alignment:**

.. code-block:: none

   >>> for i in range(1, 4):
   ...     print(f"{i:3}  {i**2:5}")
   ...
     1      1
     2      4
     3      9

   - ``:3`` means: right-align in a field of width 3.
   - ``:<10`` means: left-align in a field of width 10.
   - ``:^10`` means: center in a field of width 10.

**Integer formatting:**

.. code-block:: none

   >>> n = 255
   >>> print(f"{n:d}")     # decimal
   255
   >>> print(f"{n:08b}")   # binary, zero-padded to 8 digits
   11111111
   >>> print(f"{n:x}")     # hexadecimal
   ff

.. index:: str.format()

Older Formatting Methods
------------------------

You may encounter two older formatting styles in existing code.

*The* ``.format()`` *method:*

.. code-block:: python

   print("The wall area is {} square feet.".format(wall_area))
   print("Name: {0}, Age: {1}".format(name, age))

*Percent-style formatting:*

.. code-block:: python

   print("pi = %.4f" % 3.14159)

F-strings are preferred in new code because they are more readable and
slightly faster.

The Painting Program Revisited
-------------------------------

Here is the output section of the painting program using f-strings:

.. code-block:: python

   print(f"The wall area is {wall_area} square feet.")
   print(f"The ceiling area is {ceiling_area} square feet.")

To display the areas with exactly one decimal place:

.. code-block:: python

   print(f"The wall area is {wall_area:.1f} square feet.")
   print(f"The ceiling area is {ceiling_area:.1f} square feet.")
