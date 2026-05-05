.. index:: string

Strings, Part I
===============

.. note::

   *Source:* Drawn from the SE4ML Python chapter (``chapter_python.rst``,
   lines 2312–2355) and the C# edition (``data/strings1.rst``).  String
   literals, concatenation, repetition, and immutability follow the SE4ML
   presentation; ``str()`` conversion is adapted from the C# edition.

A *string* is a sequence of characters.  Strings are one of the most
commonly used types in Python.

.. index:: string literal, quotes

String Literals
---------------

You can write a string literal using either single quotes or double quotes:

.. code-block:: none

   >>> 'Hello'
   'Hello'
   >>> "Hello"
   'Hello'

They are equivalent.  Using double quotes inside single-quoted strings (and
vice versa) avoids backslashes:

.. code-block:: none

   >>> 'She said, "Hello."'
   'She said, "Hello."'
   >>> "It's a fine day."
   "It's a fine day."

For strings spanning multiple lines, use *triple quotes* — either ``"""`` or
``'''``:

.. code-block:: none

   >>> poem = """Roses are red,
   ... Violets are blue."""
   >>> print(poem)
   Roses are red,
   Violets are blue.

.. index:: string concatenation, string repetition

String Operations
-----------------

The ``+`` operator *concatenates* (joins) two strings:

.. code-block:: none

   >>> "Hello, " + "world!"
   'Hello, world!'
   >>> first = "Ada"
   >>> last = "Lovelace"
   >>> full = first + " " + last
   >>> full
   'Ada Lovelace'

The ``*`` operator *repeats* a string:

.. code-block:: none

   >>> "ha" * 3
   'hahaha'
   >>> "-" * 20
   '--------------------'

.. index:: len()

String Length
-------------

``len()`` returns the number of characters in a string:

.. code-block:: none

   >>> len("Hello")
   5
   >>> len("")
   0
   >>> len("Ada Lovelace")
   12

.. index:: string; immutability

Strings are Immutable
---------------------

Strings cannot be changed after they are created.  You can create a *new*
string based on an old one, but you cannot modify the original:

.. code-block:: none

   >>> s = "Hello"
   >>> s[0] = "J"       # This will cause an error
   TypeError: 'str' object does not support item assignment

To "change" a string, create a new one:

.. code-block:: none

   >>> s = "J" + s[1:]
   >>> s
   'Jello'

Slicing and indexing are covered in the Basic String Operations chapter.

.. index:: str(), type conversion

Converting to String
---------------------

Use ``str()`` to convert other types to strings:

.. code-block:: none

   >>> str(42)
   '42'
   >>> str(3.14)
   '3.14'
   >>> "The answer is " + str(42)
   'The answer is 42'

Note that you *cannot* concatenate a string and a number directly:

.. code-block:: none

   >>> "The answer is " + 42
   TypeError: can only concatenate str (not "int") to str

You must convert first with ``str()``, or use an f-string (see :ref:`fstrings`).
