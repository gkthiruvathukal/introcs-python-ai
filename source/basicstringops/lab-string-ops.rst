.. _lab-string-ops:

.. index::
   single: labs; string operations

Lab: String Operations
=======================

.. note::

   *Source:* Parts 1, 3, and 4 adapted from the C# edition
   (``basicstringops/lab-string-ops.rst``).  Parts 2 (Initials) and 5
   (Pig Latin) are original additions.

Goals
-----

#. Practice string indexing and slicing.
#. Use string methods to inspect and transform text.
#. Apply problem-solving techniques with limited tools.

This lab uses the material from :ref:`string-indexing` and
:ref:`string-methods-length`.  Parts 3 and 4 also use ``if``/``elif``/``else``
from the Decisions chapter — if you have not reached that chapter yet, you
can skip or come back to those parts.

Structure
---------

Write a single Python file called ``string_lab.py``.  Implement each part as
its own function and call all of them from ``main()``.  Add one function at a
time and test before moving on.

Part 1: String Length
---------------------

Write a function ``show_length()`` that reads a string from the user and
prints its length with a label.

Sample run:

.. code-block:: none

   Enter a string: Hello, world!
   Length: 13

Part 2: Initials
----------------

Write a function ``initials()`` that reads a full name (first and last,
separated by a single space) and prints the person's initials in the form
``F.L.``

Sample run:

.. code-block:: none

   Enter your full name: Marcel Proust
   Initials: M.P.

*Hint:* Use ``split()`` to separate first and last name, then index each
part.

Part 3: Sentence Type
---------------------

Write a function ``sentence_type()`` that reads a sentence and prints whether
it is *declarative* (ends in ``.``), *interrogatory* (ends in ``?``),
*exclamatory* (ends in ``!``), or *not a sentence* (anything else).

Sample runs:

.. code-block:: none

   Enter a sentence: The sky is blue.
   Declarative

   Enter a sentence: Is it raining?
   Interrogatory

*Hint:* Use ``endswith()``.

Part 4: Last, First
--------------------

Write a function ``last_first()`` that reads a full name (first and last)
and prints it in the form ``Last, First``.

Sample run:

.. code-block:: none

   Enter your full name: Marcel Proust
   Proust, Marcel

Extend the function to handle a single name (no space), printing it
unchanged:

Sample run:

.. code-block:: none

   Enter your full name: Socrates
   Socrates

*Hint:* Use ``find()`` to check whether a space exists.

Part 5: Pig Latin
-----------------

Write a function ``pig_latin(word)`` that converts a word to simple Pig
Latin: move the first character to the end and add ``"ay"``.

.. code-block:: none

   >>> pig_latin("hello")
   'ellohay'
   >>> pig_latin("python")
   'ythonpay'

Use slicing: the first character is ``word[0]``, the rest is ``word[1:]``.

Putting It Together
-------------------

Your ``main()`` function should call each part in order:

.. code-block:: python

   def main() -> None:
       show_length()
       initials()
       sentence_type()
       last_first()
       word = input("Enter a word for Pig Latin: ")
       print(pig_latin(word))

   if __name__ == '__main__':
       main()
