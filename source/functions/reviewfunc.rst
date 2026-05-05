Chapter Review Questions
========================

1. What is the purpose of a function?  Name two advantages of using functions
   over copying and pasting code.

2. What is the difference between a *parameter* and an *argument*?

3. A function can have a ``return`` statement, or it can have none.  What
   value does Python return if there is no ``return`` statement?

4. What does *local scope* mean?  Why is it useful?

5. Which of the following names would Python allow as a function name?
   Which follow Python's naming convention?

   a. ``calculateArea``
   b. ``calculate_area``
   c. ``2fast``
   d. ``def``
   e. ``TOTAL``

6. What does ``import math`` do?  How do you then call ``math.sqrt``?

7. Write a function ``rectangle_area(length, width)`` that returns the area
   of a rectangle.  Include a docstring.

8. Write a function ``celsius_to_fahrenheit(c)`` that converts a temperature
   from Celsius to Fahrenheit (:math:`F = C \times 9/5 + 32`) and returns
   the result.  Then write a short program that uses it.

9. What is a docstring?  Write a docstring for the following function::

      def hypotenuse(a, b):
          return (a**2 + b**2) ** 0.5

10. Trace through the following code and predict the output::

       def f(x):
           y = x * 2
           return y + 1

       a = 3
       b = f(a)
       print(a, b)
