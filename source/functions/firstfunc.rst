.. index:: function; def

A First Function Definition
===========================

.. note::

   *Source:* Adapted from the C# edition (``functions/firstfunc.rst``) and the
   SE4ML Python chapter (``chapter_python.rst``, lines 485–562).  The birthday
   example mirrors the C# original; ``def`` syntax details follow the SE4ML
   presentation.

Programs often need to repeat the same sequence of steps in more than one
place.  Rather than copy and paste, we define a *function* — a named block of
code we can call by name.

The Birthday Problem
--------------------

Suppose you want to print a birthday song for a friend named Emily:

.. code-block:: python

   print("Happy Birthday to you!")
   print("Happy Birthday to you!")
   print("Happy Birthday, dear Emily.")
   print("Happy Birthday to you!")

Now suppose you also want to print the song for a friend named Andre.  You
could copy the four lines and change the name — but what if you also decide to
add a fifth line?  You would have to make the change in two places.  Functions
solve this problem.

.. index:: def statement

Defining a Function
-------------------

A function definition uses the ``def`` keyword:

.. code-block:: python

   def happy_birthday():
       print("Happy Birthday to you!")
       print("Happy Birthday to you!")
       print("Happy Birthday, dear Emily.")
       print("Happy Birthday to you!")

Key things to notice:

- The ``def`` line ends with a colon ``:``.
- The body of the function is *indented* — the standard is 4 spaces.
- The function name follows the same rules as variable names: lowercase with
  underscores (``snake_case``).
- The parentheses ``()`` are required even when there are no parameters.

Calling a Function
------------------

To run the code in a function, you *call* it by writing its name followed by
parentheses:

.. code-block:: python

   def happy_birthday():
       print("Happy Birthday to you!")
       print("Happy Birthday to you!")
       print("Happy Birthday, dear Emily.")
       print("Happy Birthday to you!")

   happy_birthday()

Output:

.. code-block:: none

   Happy Birthday to you!
   Happy Birthday to you!
   Happy Birthday, dear Emily.
   Happy Birthday to you!

The function definition does not produce any output on its own.  Only when you
*call* it does the code run.

Calling Multiple Times
----------------------

The advantage becomes clear when you call the function more than once:

.. code-block:: python

   happy_birthday()
   happy_birthday()

Output:

.. code-block:: none

   Happy Birthday to you!
   Happy Birthday to you!
   Happy Birthday, dear Emily.
   Happy Birthday to you!
   Happy Birthday to you!
   Happy Birthday to you!
   Happy Birthday, dear Emily.
   Happy Birthday to you!

One definition, used wherever needed.
