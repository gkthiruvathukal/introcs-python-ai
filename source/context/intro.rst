.. _resources-online:

Resources Online
================

.. note::

   *Source:* Adapted from the C# edition introduction.  Python workflow,
   REPL usage, and VS Code recommendation sections are original additions.

This book is designed for the introductory computer science course at Loyola
University Chicago.  The materials are available to all on the web.

.. note::

   For all work in this course, install Python 3 and use the command-line
   tools.  The basic workflow is:

   1. Write a ``.py`` file in a text editor (VS Code is recommended).
   2. Run it from the terminal::

         python3 filename.py

   You can also experiment interactively by typing ``python3`` at the
   terminal to enter the interactive shell.

*  The course example repository will contain all example programs referenced
   in the book.  Download or clone it and keep it alongside your work.

*  `python.org <https://www.python.org>`_ is the official Python website.
   It includes documentation for the standard library and language reference.

*  `Visual Studio Code <https://code.visualstudio.com>`_ with the Python
   extension is the recommended editor.  It provides syntax highlighting,
   error detection, and an integrated terminal.

.. index:: Python; interactive shell
   REPL

The Interactive Shell
---------------------

Python provides an interactive shell (also called a REPL, for
Read-Evaluate-Print Loop) that lets you type expressions and see their
values immediately.  Start it by typing ``python3`` at your terminal:

.. code-block:: none

   $ python3
   Python 3.12.0 (default, ...)
   Type "help", "copyright", "credits" or "license" for more information.
   >>>

Type any expression and press Enter::

   >>> 2 + 3
   5
   >>> "Hello, world!"
   'Hello, world!'

This is very useful for experimenting with small pieces of code.  We will use
the ``>>>`` prompt throughout the book to show interactive examples.

To exit the shell, type ``quit()`` or press Ctrl-D.

.. _alt-formats:

Alternate Formats
-----------------

This book is available in HTML, PDF, and EPUB formats.  See the download
links at the top of each page.
