.. index:: labs; dictionaries, file; reading into dict

.. _lab-filedata:

Lab: File Data and Collections
===============================

.. note::

   *Source:* Adapted from the C# edition (``dictionaries/lab-filedata.rst``).
   The C# lab uses ``StreamReader`` and ``Dictionary<string,string>``; this
   Python version uses ``open()`` / ``with`` and Python ``dict``.

Goals for this lab:

- Read data from a text file into a dictionary.
- Query and report on the data using dictionary operations.
- Practice combining file I/O, loops, and collections.

Overview
--------

You will write a program that reads a simple data file and answers
queries about its contents.  The file ``grades.txt`` has one record per
line in the format ``name:score``:

.. code-block:: none

   Alice:91
   Bob:78
   Carol:85
   David:92
   Eve:67

Steps
-----

.. index:: file; read into dict

1. **Read the file into a dictionary**

   Write a function ``read_grades(filename)`` that opens ``filename``,
   reads each line, splits on ``:``, and returns a ``dict`` mapping each
   student name (string) to their score (integer).

   .. code-block:: python

      def read_grades(filename):
          grades = {}
          with open(filename) as f:
              for line in f:
                  name, score = line.strip().split(":")
                  grades[name] = int(score)
          return grades

2. **Query the dictionary**

   Using ``read_grades``, write a main program that:

   a. Prints the score for a user-supplied name (or a "not found" message).
   b. Prints the name and score of the student with the highest score.
   c. Prints the class average, rounded to one decimal place.
   d. Prints all students whose score is below a threshold entered by
      the user.

3. **Create the data file**

   Create ``grades.txt`` with at least five records in the ``name:score``
   format shown above.  Test your program with this file.

4. **Word frequency from a file**

   Write a second program that reads any plain-text file, counts the
   frequency of each word (case-insensitive, punctuation stripped), and
   prints the 10 most common words with their counts.

   Use ``collections.Counter`` for a concise solution, but also write
   the manual accumulation version using a plain ``dict`` for comparison.

Extension
---------

Modify the grade reader so the file can have blank lines and lines
starting with ``#`` (comments), which should both be skipped silently.
This is good defensive file-reading practice.
