.. index:: Python installation, virtual environment, venv, uv, Homebrew, WSL, Windows Subsystem for Linux, python3

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

Follow the prompts. Once Homebrew is installed, install the latest Python 3:

.. code-block:: none

   brew install python

Verify your installation:

.. code-block:: none

   python3 --version

Output should show Python 3.12 or later:

.. code-block:: none

   Python 3.x.x

**Option B: Use the python.org installer (no Homebrew)**

Download the macOS installer for the current Python 3 release from:

   https://www.python.org/downloads/

Run the ``.pkg`` file and follow the installer. When it completes, open a new
terminal window and verify:

.. code-block:: none

   python3 --version

Output should show Python 3.12 or later:

.. code-block:: none

   Python 3.x.x

Either way, once you have Python 3.12 or later installed, continue to the
:ref:`Virtual Environments <Virtual-Environments>` section below.

Linux
------

Most Linux distributions include Python 3, but it may not be 3.12. Use your
distribution's package manager to install the right version.

**Ubuntu / Debian:**

.. code-block:: none

   sudo apt update
   sudo apt install python3 python3-venv python3-dev

.. note::
   On older Ubuntu releases (22.04 and earlier) the default ``python3`` may be
   below 3.12. Check with ``python3 --version`` and, if needed, install a
   newer version via the `deadsnakes PPA <https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa>`__.

**Fedora / RHEL / CentOS:**

.. code-block:: none

   sudo dnf install python3

**Arch Linux:**

.. code-block:: none

   sudo pacman -S python

(Arch typically ships the latest stable Python.)

Verify after installation:

.. code-block:: none

   python3 --version

Output should show Python 3.12 or later:

.. code-block:: none

   Python 3.x.x

.. _Virtual-Environments:

Virtual Environments
---------------------

Regardless of your platform, you should always work inside a **virtual
environment** rather than installing packages into the system Python. A virtual
environment is an isolated copy of Python with its own package directory. This
keeps your projects independent from each other and from the system.

**Creating a virtual environment**

Navigate to the directory where you want to keep your coursework and create a
virtual environment named ``.venv``:

.. code-block:: none

   python3 -m venv .venv

This creates a ``.venv/`` subdirectory containing a private Python interpreter
and package directory.

**Activating the virtual environment**

You must activate the virtual environment every time you open a new terminal
before doing any Python work for this course.

On macOS and Linux (including WSL):

.. code-block:: none

   source .venv/bin/activate

Your prompt will change to show the environment name:

.. code-block:: none

   (.venv) $

On Windows (only if using native PowerShell, not WSL):

.. code-block:: none

   .venv\Scripts\activate

**Verifying the environment**

With the environment active, confirm that Python and pip point into the virtual
environment:

.. code-block:: none

   which python
   python --version

Output:

.. code-block:: none

   /path/to/your/coursework/.venv/bin/python
   Python 3.x.x

**Deactivating**

When you are finished working, you can deactivate the environment:

.. code-block:: none

   deactivate

.. note::
   **Activate before you work.** Every time you open a new terminal session,
   run ``source .venv/bin/activate`` before running any Python commands for
   this course. Forgetting to activate is the most common source of "but it
   worked before!" confusion.

Alternative: Using ``uv``
--------------------------

``uv`` is a fast Python package and project manager written in Rust. It can
install Python itself, create virtual environments, and manage packages — all
in one tool, and dramatically faster than ``pip``. It also solves the
version-selection problem cleanly: you tell ``uv`` which Python version you
want and it handles the rest, no matter what the system default is.

``uv`` requires Homebrew on macOS. On Linux (and WSL) it has its own
installer script.

**Installing uv**

On macOS (requires Homebrew):

.. code-block:: none

   brew install uv

On Linux and WSL:

.. code-block:: none

   curl -LsSf https://astral.sh/uv/install.sh | sh

Restart your terminal (or run ``source ~/.bashrc``) after the Linux install
so that the ``uv`` binary is on your ``PATH``.

**Installing Python 3.12 with uv**

``uv`` can download and manage Python versions independently of the system:

.. code-block:: none

   uv python install 3.12

**Creating a virtual environment with uv**

.. code-block:: none

   uv venv --python 3.12 .venv

This creates the same ``.venv/`` directory as before, but lets you specify the
Python version directly — no need to worry about what ``python3`` points to on
your system. Activate it exactly as before:

.. code-block:: none

   source .venv/bin/activate

**Installing packages with uv**

Once the environment is active, use ``uv pip`` in place of ``pip``:

.. code-block:: none

   uv pip install <package-name>

.. note::
   For this course the standard ``venv`` and ``pip`` approach taught above is
   perfectly fine. ``uv`` is worth knowing about, but adds an extra dependency
   (Homebrew on macOS). Both paths produce the same virtual environment and
   work the same way once activated.
