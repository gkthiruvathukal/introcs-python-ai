Lab: Division Sentences
=======================

In this lab you will practice using the floor division (``//``) and remainder
(``%``) operators to produce English sentences describing division.

Background
----------

When we divide 17 by 5 we get a quotient of 3 and a remainder of 2.  We can
write this as:

.. code-block:: none

   17 divided by 5 gives 3 remainder 2.

In Python:

.. code-block:: none

   >>> 17 // 5
   3
   >>> 17 % 5
   2

Part 1
------

Write a program that asks the user for two integers (a *dividend* and a
*divisor*) and prints a sentence of the form:

.. code-block:: none

   <dividend> divided by <divisor> gives <quotient> remainder <remainder>.

For example, with dividend 17 and divisor 5:

.. code-block:: none

   17 divided by 5 gives 3 remainder 2.

Part 2
------

Extend your program to also print the result as a mixed number (whole part
plus fraction):

.. code-block:: none

   17 / 5 = 3 and 2/5

Hint: the quotient is ``dividend // divisor`` and the remainder is
``dividend % divisor``.

Part 3
------

What happens when the remainder is 0?  Try 20 divided by 4.  Does your
sentence still make sense?  If not, how would you change it?  (You do not
need to implement the fix yet — just think about it.)
