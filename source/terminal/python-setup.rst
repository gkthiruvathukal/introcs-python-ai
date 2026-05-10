.. index:: Python installation, virtual environment, venv, Homebrew, WSL, Windows Subsystem for Linux, pyenv, python3

.. _Python-Setup:

Installing and Setting Up Python
=================================

.. note::
   *Source:* Python-specific — no equivalent in the C# edition.

This book is terminal-centric by design. We believe that learning to work at the
command line from the start builds habits that will serve you throughout your career.
That means we deliberately de-emphasize graphical IDEs and point-and-click
installers. The terminal is where programmers live, and this chapter gets you set
up there.

.. note::
   **Recommended platforms: macOS and Linux.** Both provide a Unix-compatible
   shell experience out of the box. Windows can work, but only via the Windows
   Subsystem for Linux (WSL). If you are on Windows, read the Windows section
   below first, then follow the Linux instructions.

We target **Python 3.12 or later** throughout this book.

Windows: Use WSL
-----------------

Windows does not ship with a Unix-compatible shell, and the native Windows
command prompt (``cmd.exe``) or PowerShell behave differently enough from a
Unix terminal that following along becomes unnecessarily difficult. The solution
is the **Windows Subsystem for Linux (WSL)**, which runs a real Linux environment
directly on Windows — no virtual machine required.

We recommend WSL 2 with the Ubuntu distribution. Microsoft provides official
setup instructions here:

   https://learn.microsoft.com/en-us/windows/wsl/install

The short version: open PowerShell as Administrator and run:

.. code-block:: none

   wsl --install

This installs WSL 2 and Ubuntu by default. Once installation completes and you
have rebooted, launch **Ubuntu** from the Start menu. You will be dropped into a
Bash shell inside a real Ubuntu environment.

From that point forward, follow the **Linux** instructions below exactly as
written. Everything will work the same way.

macOS
------

macOS ships with Python 3 pre-installed, but Apple's bundled version is often
out of date and tied to system tools — not ideal for coursework. We recommend
one of the two approaches below.

**Option A: Install Python via Homebrew (recommended)**

`Homebrew <https://brew.sh>`__ is the standard package manager for macOS. If
you do not already have it, install it by running this command in your terminal:

.. code-block:: none

   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Follow the prompts. Once Homebrew is installed, install Python 3.12:

.. code-block:: none

   brew install python@3.12

Homebrew installs Python alongside a ``pip`` and a ``python3.12`` binary. Verify
your installation:

.. code-block:: none

   python3.12 --version

Output:

.. code-block:: none

   Python 3.12.x

**Option B: Use the python.org installer (no Homebrew)**

Download the macOS installer for Python 3.12 (or later) from:

   https://www.python.org/downloads/

Run the ``.pkg`` file and follow the installer. When it completes, open a new
terminal window and verify:

.. code-block:: none

   python3 --version

Output:

.. code-block:: none

   Python 3.12.x

Either way, once you have Python 3.12 installed, continue to the
:ref:`Virtual Environments <Virtual-Environments>` section below.

Linux
------

Most Linux distributions include Python 3, but it may not be 3.12. Use your
distribution's package manager to install the right version.

**Ubuntu / Debian:**

.. code-block:: none

   sudo apt update
   sudo apt install python3.12 python3.12-venv python3.12-dev

**Fedora / RHEL / CentOS:**

.. code-block:: none

   sudo dnf install python3.12

**Arch Linux:**

.. code-block:: none

   sudo pacman -S python

(Arch typically ships the latest stable Python.)

Verify after installation:

.. code-block:: none

   python3.12 --version

Output:

.. code-block:: none

   Python 3.12.x

.. _Virtual-Environments:

Virtual Environments
---------------------

Regardless of your platform, you should always work inside a **virtual
environment** rather than installing packages into the system Python. A virtual
environment is an isolated copy of Python with its own package directory. This
keeps your projects independent from each other and from the system.

**Creating a virtual environment**

Navigate to the directory where you want to keep your coursework and create a
virtual environment named ``venv``:

.. code-block:: none

   python3.12 -m venv venv

This creates a ``venv/`` subdirectory containing a private Python interpreter
and package directory.

**Activating the virtual environment**

You must activate the virtual environment every time you open a new terminal
before doing any Python work for this course.

On macOS and Linux (including WSL):

.. code-block:: none

   source venv/bin/activate

Your prompt will change to show the environment name:

.. code-block:: none

   (venv) $

On Windows (only if using native PowerShell, not WSL):

.. code-block:: none

   venv\Scripts\activate

**Verifying the environment**

With the environment active, confirm that Python and pip point into the virtual
environment:

.. code-block:: none

   which python
   python --version

Output:

.. code-block:: none

   /path/to/your/coursework/venv/bin/python
   Python 3.12.x

**Deactivating**

When you are finished working, you can deactivate the environment:

.. code-block:: none

   deactivate

.. note::
   **Activate before you work.** Every time you open a new terminal session,
   run ``source venv/bin/activate`` before running any Python commands for
   this course. Forgetting to activate is the most common source of "but it
   worked before!" confusion.

A Note on ``uv``
-----------------

If you continue in software development beyond this course, you will likely
encounter ``uv``, a fast Python package and project manager written in Rust. It
can create virtual environments, install packages, and manage Python versions all
in one tool, and it is dramatically faster than ``pip``. For an introductory
course, however, ``venv`` and ``pip`` are the right starting point — they are
built into Python itself, require no additional installation, and teach the
underlying concepts directly. Once you are comfortable with those, ``uv`` is
worth exploring.
