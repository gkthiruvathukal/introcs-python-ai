.. index:: terminal, shell, command line, stdin, stdout, stderr, sys.argv, argparse

.. _Terminal-Overview:

The Terminal
============

.. note::
   *Source:* Contributed by PhD students in COMP 501 at Loyola University Chicago.

Throughout this course you have been running Python programs by clicking a "Run"
button in an IDE or executing code in an interactive shell. Now we explore another
powerful way to interact with your programs: the **terminal**.

The terminal may seem intimidating at first — a text-based window with no buttons to
click. But it is one of the most important tools in a programmer's toolkit, and
learning to use it will make you more capable as a developer.

Terminal vs. Shell
------------------

People often use "terminal" and "shell" interchangeably, but they refer to different
things.

- **Terminal** (or terminal emulator) — the window on your screen where text
  appears. On macOS this is the Terminal app; on Windows, Command Prompt or
  PowerShell; on Linux, GNOME Terminal or similar.
- **Shell** — the program running *inside* the terminal that reads your commands
  and tells the operating system to execute them. Common shells include ``bash``,
  ``zsh``, ``fish``, and PowerShell.

Think of it this way: the terminal is the video-call window (Zoom, Teams) — just
the frame. The shell is the person you are talking to — the part that actually
understands and responds.

Why Programmers Use the Terminal
---------------------------------

Even though graphical interfaces are available, experienced programmers often
prefer the terminal for several reasons:

- **Speed** — typing a command is faster than navigating menus. Renaming 100 files
  with a graphical interface means 100 click-rename cycles; with the terminal, a
  single command handles all of them at once.
- **Precision** — you can express exactly what you want, with no ambiguity.
- **Automation** — sequences of commands can be saved in scripts and run
  automatically, including your Python programs.
- **Remote work** — the terminal works the same whether you are on your laptop or
  connected to a server on the other side of the world.
- **Universal skill** — terminal commands are similar or identical across operating
  systems; learning them once pays dividends everywhere.

Opening Your Terminal
---------------------

**macOS**: Press ``Command + Space``, type ``Terminal``, press Enter. Or find it
in ``Applications > Utilities > Terminal``.

**Windows**: Press the Windows key, type ``PowerShell`` or ``cmd``, press Enter.

**Linux**: Press ``Ctrl + Alt + T`` on most distributions.

When the terminal opens you will see a **prompt** — the shell's signal that it is
ready for a command. The prompt typically ends with ``$`` on macOS/Linux or ``>``
on Windows.

Essential Commands
------------------

``pwd`` — print working directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Shows your current location in the file system.

.. code-block:: none

   $ pwd
   /Users/yourname/Documents

``ls`` — list contents
^^^^^^^^^^^^^^^^^^^^^^^

Shows what is in your current directory (use ``dir`` on Windows Command Prompt).

.. code-block:: none

   $ ls
   homework.txt    python_projects    essay.docx

``cd`` — change directory
^^^^^^^^^^^^^^^^^^^^^^^^^^

Moves you to a different directory.

.. code-block:: none

   cd python_projects    # move into a subdirectory
   cd ..                 # move up one level
   cd ~                  # move to your home directory

``mkdir`` — make directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates a new directory. In the terminal, **no news is good news** — if the command
succeeds, you just get the prompt back.

.. code-block:: none

   mkdir my_project

``whoami`` — show current user
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

   $ whoami
   yourname

Standard Streams
----------------

When a program runs, it communicates through three standard channels:

- **stdin** (standard input) — where the program reads input. When you type into a
  running program, it comes through stdin.
- **stdout** (standard output) — where the program sends normal output. Python's
  ``print()`` writes to stdout.
- **stderr** (standard error) — where the program sends error messages. Having a
  separate channel for errors lets you handle them independently from normal output.

.. code-block:: none

   User Input → [stdin] → Your Program → [stdout] → Normal Output
                                       ↳ [stderr] → Error Messages

Here is a Python script that writes to all three:

.. code-block:: python

   import sys

   print("This goes to stdout")
   sys.stdout.write("This also goes to stdout\n")
   sys.stderr.write("This goes to stderr\n")

   user_input = input("Type something: ")
   print(f"You typed: {user_input}")

Running Python Scripts from the Terminal
-----------------------------------------

Create a file called ``hello_terminal.py``:

.. code-block:: python

   print("Hello from the terminal!")
   print("This script is running successfully.")

Then run it:

.. code-block:: none

   python hello_terminal.py

(Use ``python3`` if your system requires it.)

Exit Codes
^^^^^^^^^^

When a program ends it reports an **exit code** back to the shell:

- ``0`` means success.
- Any non-zero value means failure.

.. code-block:: python

   import sys

   choice = input("Should this program succeed? (yes/no): ")

   if choice.lower() == "yes":
       print("Success!")
       sys.exit(0)
   else:
       print("Failure!")
       sys.exit(1)

Check the exit code after running:

.. code-block:: none

   # macOS/Linux
   echo $?

   # Windows PowerShell
   echo $LASTEXITCODE

Command Line Arguments with ``sys.argv``
-----------------------------------------

Sometimes you want to give a program information *before* it starts running. Python's
``sys.argv`` is a list that holds:

- ``sys.argv[0]`` — the script name
- ``sys.argv[1]``, ``sys.argv[2]``, … — any extra words typed after the script name

.. code-block:: python

   import sys

   print("Arguments:", sys.argv)

   for i, arg in enumerate(sys.argv):
       print(f"Argument {i}: {arg}")

Run it:

.. code-block:: none

   python show_arguments.py hello world 123

Output:

.. code-block:: none

   Arguments: ['show_arguments.py', 'hello', 'world', '123']
   Argument 0: show_arguments.py
   Argument 1: hello
   Argument 2: world
   Argument 3: 123

Here is a script that uses ``sys.argv`` to greet a user:

.. code-block:: python

   import sys

   if len(sys.argv) < 2:
       print("Error: please provide your name.")
       print("Usage: python greet.py YourName")
       sys.exit(1)

   name = sys.argv[1]
   print(f"Hello, {name}!")
   sys.exit(0)

Professional CLI Programs with ``argparse``
--------------------------------------------

``sys.argv`` is simple but limited — it provides no automatic help, no validation,
and no support for optional flags. Python's ``argparse`` module solves all of this.

.. code-block:: python

   import argparse

   def main():
       parser = argparse.ArgumentParser(description="A friendly greeting program")
       parser.add_argument("name", help="Your name")
       parser.add_argument("-n", "--number", type=int, default=1,
                           help="Number of times to greet (default: 1)")
       args = parser.parse_args()

       for _ in range(args.number):
           print(f"Hello, {args.name}!")

       return 0

   if __name__ == "__main__":
       exit(main())

Try:

.. code-block:: none

   python greet_argparse.py Alice
   python greet_argparse.py Alice -n 5
   python greet_argparse.py --help

``argparse`` automatically generates a ``--help`` message that lists all arguments,
their types, and their descriptions — essential for any tool that others will use.

Here is a more complete example — a file search tool:

.. code-block:: python

   import argparse
   import sys

   def search_file(filename, keyword, case_sensitive=True, line_numbers=False):
       try:
           with open(filename, "r") as f:
               for line_num, line in enumerate(f, start=1):
                   haystack = line if case_sensitive else line.lower()
                   needle = keyword if case_sensitive else keyword.lower()
                   if needle in haystack:
                       if line_numbers:
                           print(f"{line_num}: {line.rstrip()}")
                       else:
                           print(line.rstrip())
           return 0
       except FileNotFoundError:
           print(f"Error: '{filename}' not found", file=sys.stderr)
           return 1
       except PermissionError:
           print(f"Error: permission denied for '{filename}'", file=sys.stderr)
           return 1

   def main():
       parser = argparse.ArgumentParser(
           description="Search for a keyword in a text file",
           epilog="Example: python search_file.py data.txt Python -i -n"
       )
       parser.add_argument("filename", help="Path to the file to search")
       parser.add_argument("keyword", help="Keyword to search for")
       parser.add_argument("-i", "--ignore-case", action="store_true",
                           help="Case-insensitive search")
       parser.add_argument("-n", "--line-numbers", action="store_true",
                           help="Show line numbers in output")
       args = parser.parse_args()

       return search_file(
           args.filename,
           args.keyword,
           case_sensitive=not args.ignore_case,
           line_numbers=args.line_numbers
       )

   if __name__ == "__main__":
       sys.exit(main())

Try:

.. code-block:: none

   python search_file.py story.txt dragon
   python search_file.py story.txt dragon -i
   python search_file.py story.txt dragon -i -n
   python search_file.py --help

Exercises
---------

1. Open your terminal and run ``pwd``, ``ls``, and ``whoami``. What do they tell
   you?
2. Create a directory called ``practice``, move into it, create two subdirectories
   inside it, and then navigate back to the parent.
3. Write a script ``greet.py`` that takes a name as a command line argument and
   prints ``Hello, <name>!``. Exit with code ``1`` if no name is provided.
4. Extend the script using ``argparse`` to also accept an optional ``--times``
   flag that controls how many times the greeting is printed.
5. Write a script ``process_numbers.py`` that:

   - Accepts one or more numbers as positional arguments.
   - Supports optional flags ``--sum``, ``--average``, ``--max``, and ``--min``.
   - Uses ``argparse`` and exits with a non-zero code if any argument is not a
     valid number.
