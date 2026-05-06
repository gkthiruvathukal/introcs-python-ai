Chapter Review Questions
========================

.. note::

   *Source:* Adapted from the C# edition data-chapter review questions.
   Python-specific questions (f-strings, floor division, truthiness) are
   original additions.

1. Python has two main numeric types.

   a.  Name them.
   b.  How does ``/`` differ from ``//``?

2. In Python, do you need to declare a variable before using it?
   What happens if you use a variable that has never been assigned?

3. Consider ``input()``.

   a.  What type does it always return?
   b.  Why does that matter when you want to do arithmetic with user input?

4. Consider these two lines::

      print("The total is " + total)
      print(f"The total is {total}")

   a.  Which one will cause a ``TypeError`` if ``total`` is an integer?
   b.  Explain why.

5. f-strings.

   a.  What is an f-string?
   b.  Write an f-string that prints a float variable ``price`` formatted
       to exactly 2 decimal places.

6. The built-in ``type()`` function.

   a.  What does ``type(x)`` tell you?
   b.  Give an example of a situation where you might call it.

7. What is ``None`` in Python?  Give one situation where it appears
   automatically without the programmer writing it explicitly.

8. Python is called *dynamically typed*.  What does that mean?

9. Write a program that reads a temperature in Fahrenheit from the user and
   prints it in Celsius.  The formula is :math:`C = (F - 32) \times 5 / 9`.

10. What is the value of each expression?

    a. ``17 % 5``
    b. ``17 // 5``
    c. ``2 ** 8``
    d. ``int(3.9)``
    e. ``str(100) + "00"``
