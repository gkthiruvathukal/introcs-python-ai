Motivation for This Book
========================

This is really a preface, but the Sphinx publishing environment we use does not
have a separate preface section.

Pedagogy
--------

Our first aim is to provide a good introduction and conceptual framework for
computer science — not an encyclopedic coverage of Python.  Python will not be
most students' only language, or necessarily the most used.  Designing and
creating algorithms in a particular language is an important skill requiring
ongoing effort, so most of the text is centered on concrete Python programs.

We tend to introduce examples first, then the general syntax, then more
examples and exercises.  There are review questions at the end of most chapters.
Labs are intended as early practice on a subject, with generally small bits
requested at a time.  There are also larger assignments in the appendix.

Why Python?
-----------

Python is a good first language for several reasons.

**It is interactive.**  You can type statements directly into the Python
interpreter and see results immediately, without writing a complete program
first.  This makes it easy to experiment.

**It is concise.**  A Python program that does something useful is often
significantly shorter than the equivalent in Java or C#.  There is less
*boilerplate* — required scaffolding that does not itself express the
programmer's intent.

**It is widely used.**  Python is one of the most popular programming
languages in the world.  It is used in web development, scientific computing,
data science, artificial intelligence, scripting, and automation.

**It is dynamically typed.**  Variables do not need to be declared.  A variable
takes the type of whatever value is assigned to it.  This means you can focus on
the problem you are solving rather than managing type declarations.

**It is readable.**  Python uses indentation to show structure, instead of
braces.  Programs that follow Python's style conventions tend to look like
structured English prose.

Characteristics of Python
--------------------------

Here is a brief overview of Python's key characteristics.

*Scripting.*
Python does not require a separate compile step.  The Python interpreter
can execute programs directly.  You can also type statements interactively
at the ``>>>`` prompt.

*Dynamically typed.*
Variables are not declared.  A value of any type may be assigned to any
variable.  The *value* has a type; the *variable* does not.

*High-level.*
Python has high-level data structures built into the language, such as
lists, dictionaries, and sets.  Memory management is automatic.

*Modular.*
Python programs are organized as collections of modules.  Each module is a
``.py`` file.  The standard library provides an enormous set of ready-to-use
modules.

*Object-oriented.*
Python supports object-oriented programming with classes and inheritance.
Unlike some languages, Python does not *require* you to use objects for
everything.  This book introduces procedural programming first, then
objects.

Object-oriented programming is introduced gradually.  After the chapter on
functions you can read the first sections of :ref:`classes` to get an early
look at defining your own objects; but the full chapter is placed after
collections, where objects are most naturally useful.
