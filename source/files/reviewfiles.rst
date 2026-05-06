.. index:: review questions; files

.. _Review-Files:

Chapter Review Questions
========================

.. note::

   *Source:* Adapted from the C# edition (``files/reviewfiles.rst``).
   Questions about ``StreamReader``/``StreamWriter`` are replaced by
   Python ``open()`` and ``with`` statement equivalents.

#.  The ``with`` statement and ``open()``.

    a.  What does the ``with`` statement do when used with ``open()``?
    b.  Why is this preferable to calling ``f.close()`` manually?

#.  What mode string do you pass to ``open()`` to write to a file?
    What happens if the file already exists?

#.  What mode string do you pass to ``open()`` to append to an existing file?

#.  Iterating over lines.

    a.  In a ``for line in f:`` loop, does each ``line`` string include the
        trailing newline character?
    b.  How do you remove it?

#.  Two ways to read a file.

    a.  What does ``f.read()`` return?
    b.  What does ``f.readlines()`` return?
    c.  When would you prefer each?

#.  Write a cross-platform path for the file ``data.txt`` located in a
    subdirectory called ``input`` of the current directory, using
    ``pathlib.Path``.

#.  What does ``..`` mean in a relative path?

#.  In the path ``Path("a") / "b" / "c.txt"``, what is returned by:

    a.  ``.name``
    b.  ``.stem``
    c.  ``.suffix``
    d.  ``.parent``

#.  What method checks whether a path points to an existing file?

#.  What is logically wrong with the following code?::

       with open("data.txt") as f:
           first = f.readline()
           if "error" in f.readline():
               print("Error on line:", f.readline())
