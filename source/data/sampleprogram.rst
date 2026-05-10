.. index:: introduction

.. _sample-program:

A Sample Python Program
=======================

As a start, consider a small problem and a program to solve it.  Suppose you
paint the walls of rooms in one color and the ceiling in another, and you want
to calculate the size of the areas to cover with paint.  For simplicity, ignore
doors.  What data do you need to start with?  Clearly the dimensions of the
room.  Suppose we consider modern houses where the height of the room is
predictably 8 feet, so the new starting data is just the length and width of
the room.

You need to:

1. Obtain the length and width from the user.
2. Calculate the wall area and ceiling area.
3. Let the user know the results.

This is a common programming pattern: data in, calculate results, output
results.  In this case the calculations in the middle are straightforward.

Here is what the program looks like when it runs, with the user typing
``20.5`` and ``10``:

.. code-block:: none

   Calculation of Room Paint Requirements
   Enter room length: 20.5
   Enter room width: 10
   The wall area is 488.0 square feet.
   The ceiling area is 205.0 square feet.

Here is the program:

.. code-block:: python

   HEIGHT = 8

   print("Calculation of Room Paint Requirements")
   length = float(input("Enter room length: "))
   width = float(input("Enter room width: "))

   wall_area = 2 * (length + width) * HEIGHT
   ceiling_area = length * width

   print(f"The wall area is {wall_area} square feet.")
   print(f"The ceiling area is {ceiling_area} square feet.")

This section gives an overview of a working program, even if some explanations
do not make total sense yet.  Do not worry if you do not understand everything
here — these concepts are each explained in detail in later sections.

Line by line
------------

.. index:: assignment statement, constant; naming convention, ALL_CAPS convention

.. code-block:: python

   HEIGHT = 8

This is an *assignment statement*.  It creates a variable named ``HEIGHT`` and
gives it the value ``8``.  We use all capital letters by convention to suggest
that this value will not change — it is a *constant*.  Python has no special
syntax for constants; all-caps naming is just a widely followed convention.

.. code-block:: python

   print("Calculation of Room Paint Requirements")

``print`` is a built-in Python function that writes output to the screen.  Its
*argument* — the value inside the parentheses — is a *string*, a sequence of
characters enclosed in quotes.  The string is displayed without the quotes.

.. code-block:: python

   length = float(input("Enter room length: "))

This line does several things at once, working from the inside out:

1. ``input("Enter room length: ")`` displays the prompt string and then waits
   for the user to type something and press Enter.  It always returns a
   *string* — for example, ``"20.5"``.
2. ``float(...)`` converts that string to a floating-point number: ``20.5``.
3. The result is *assigned* to the variable ``length``.

There is no need to declare ``length`` first or specify its type.

.. code-block:: python

   wall_area = 2 * (length + width) * HEIGHT
   ceiling_area = length * width

.. index:: assignment statement; arithmetic, expression; evaluation order

These are arithmetic *assignment statements*.  The expression on the right-hand
side is evaluated first, then the result is stored in the variable on the left.
The ``*`` symbol means multiplication.  In the sample run:

.. code-block:: none

   2 * (20.5 + 10) * 8  →  488.0

.. code-block:: python

   print(f"The wall area is {wall_area} square feet.")

The ``f`` before the opening quote makes this an *f-string* (formatted string).
Inside the curly braces, ``{wall_area}`` is replaced by the current value of
that variable.  So with ``wall_area = 488.0``, the output is:

.. code-block:: none

   The wall area is 488.0 square feet.

.. index:: whitespace

Whitespace
----------

The blank lines in the program help the human reader separate sections
visually; Python ignores them.  Indentation also matters in Python, but for a
program without functions or loops (like this one), the statements are simply
at the leftmost column.  We will discuss indentation fully when we reach
functions and loops.
