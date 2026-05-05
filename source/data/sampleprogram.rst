A Sample Python Program
=======================

.. todo::

   Python equivalent of the painting program. Demonstrate:

   - ``input()`` for user input
   - Arithmetic
   - ``print()`` with f-strings
   - No type declarations needed

   .. code-block:: python

      HEIGHT = 8

      print("Calculation of Room Paint Requirements")
      length = float(input("Enter room length: "))
      width = float(input("Enter room width: "))

      wall_area = 2 * (length + width) * HEIGHT
      ceiling_area = length * width

      print(f"The wall area is {wall_area} square feet.")
      print(f"The ceiling area is {ceiling_area} square feet.")
