Lab: Editing and Running Python Programs
=========================================

The goal of this lab is to get a working Python program running on your
computer.

The Python Workflow
-------------------

Python does not require a separate compile step.  The workflow is:

1. Write a ``.py`` file with a text editor.
2. Run it directly with ``python3``.

There is no ``build`` or ``compile`` command.

Setting Up
----------

If Python 3 is not yet installed, download it from `python.org
<https://www.python.org>`_.  Open a terminal and verify:

.. code-block:: none

   $ python3 --version
   Python 3.12.0

We recommend `Visual Studio Code <https://code.visualstudio.com>`_ as an
editor.  Install the Python extension from the VS Code marketplace.

The Interactive Shell
---------------------

Before writing a file, try the interactive shell.  Type ``python3`` at the
terminal prompt:

.. code-block:: none

   $ python3
   Python 3.12.0 (default, ...)
   >>>

You are now at the Python REPL (Read-Evaluate-Print Loop).  Type any
expression and press Enter:

.. code-block:: none

   >>> 2 + 3
   5
   >>> "Hello!"
   'Hello!'
   >>> print("Hello, world!")
   Hello, world!

Exit with ``quit()`` or Ctrl-D.

Your First Script
-----------------

1. Create a new file called ``hello.py`` with this content:

   .. code-block:: python

      print("Hello, world!")

2. Run it from the terminal:

   .. code-block:: none

      $ python3 hello.py
      Hello, world!

The Painting Program
--------------------

Now run the painting program from :ref:`sample-program`.

1. Create a file called ``painting.py`` and type in the program.
2. Run it and verify you get the same output as shown in the sample run.
3. Run it a second time with different values (for example, length 15 and
   width 6.5) and check that the output is correct.

.. code-block:: none

   Calculation of Room Paint Requirements
   Enter room length: 15
   Enter room width: 6.5
   The wall area is 344.0 square feet.
   The ceiling area is 97.5 square feet.
