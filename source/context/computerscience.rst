Computer Science, Broadly
=========================

.. note::

   *Source:* Adapted from the C# edition context chapter.  The Algorithms,
   Data, and Abstraction subsections are original additions providing
   Python-oriented framing.

Computer science is the study of computation: what can be computed, how to
compute it efficiently, and how to build the systems that do the computing.
The word *computer* in "computer science" is somewhat misleading — the field is
really about *computation*, and the computer is just the machine we use to
perform it.

Algorithms
----------

At the heart of computer science is the *algorithm*: a precise, step-by-step
procedure for solving a problem.  An algorithm must be:

- **Unambiguous** — each step must be clear enough that it can be followed
  mechanically, without judgment.
- **Finite** — it must terminate after a finite number of steps.
- **Correct** — it must produce the right answer for all valid inputs.

A program is an algorithm expressed in a language a computer can execute.
Writing programs is one of the central skills of computer science, but it is
not the whole of it.  Computer scientists also study which problems *can* be
solved algorithmically, how efficiently they can be solved, and how to build
reliable software systems from many interacting programs.

Data
----

Algorithms operate on *data*.  Understanding how data is represented and
organized is just as important as understanding algorithms.  Should a
collection of items be stored in a list?  A dictionary?  A tree?  The choice
affects both the correctness and the speed of the program.

Abstraction
-----------

One of the most powerful ideas in computer science is *abstraction*: hiding
details behind a well-defined interface so that you can use something without
knowing everything about how it works.  When you call ``print()``, you do not
need to know how Python turns a string into pixels on a screen.  The details
are hidden.  You interact with the abstraction.

Functions, modules, classes, and libraries are all tools for building
abstractions.  Learning to create and use abstractions effectively is a major
goal of this course.

Why This Matters
----------------

The problems you will solve in this course are small — printing a greeting,
calculating a paint requirement, guessing a number.  But the skills you
develop — breaking a problem into steps, expressing those steps precisely,
testing your solution — apply directly to problems of any size.  Every large
software system is built from pieces that are individually understandable.
