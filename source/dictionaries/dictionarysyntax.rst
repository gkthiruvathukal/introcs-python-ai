.. index:: dictionary, dict; syntax, dict; key-value
   ACM-IEEE CS2013; SDF3 Fundamental Data Structures
   ACM-IEEE CS2023; SDF3 Fundamental Data Structures

.. _Dictionary-Syntax:

Dictionary Syntax
=================

A *dictionary* maps *keys* to *values*.  Given a key, you can look up its
associated value in constant time — like looking up a word in a reference
book.

Creating Dictionaries
---------------------

.. index:: dict; literal, dict; constructor

Use braces with ``key: value`` pairs:

.. code-block:: python

   e2sp = {"one": "uno", "two": "dos", "three": "tres"}
   word_count = {}       # empty dict
   ages = {"Alice": 30, "Bob": 25}

.. index:: dict(); constructor

You can also use ``dict()`` with keyword arguments:

.. code-block:: python

   e2sp = dict(one="uno", two="dos", three="tres")

Accessing and Modifying Entries
---------------------------------

.. index:: dict; access, dict; update

Use square brackets to get or set a value by key:

.. code-block:: python

   print(e2sp["one"])       # "uno"
   e2sp["four"] = "cuatro"  # add new entry
   e2sp["two"] = "DOS"      # update existing entry

.. index:: KeyError, dict.get(); default value

Accessing a key that does not exist raises a ``KeyError``.  Use
``dict.get(key, default)`` to avoid the exception:

.. code-block:: python

   print(e2sp.get("five", "not found"))   # "not found"
   print(e2sp.get("one", "not found"))    # "uno"

Membership Test
---------------

.. index:: in; dict key

Use ``in`` to test whether a key is present:

.. code-block:: python

   print("three" in e2sp)    # True
   print("seven" in e2sp)    # False

Removing Entries
----------------

.. index:: del; dict, dict.pop()

- ``del d[key]`` removes the entry (raises ``KeyError`` if absent).
- ``d.pop(key)`` removes and returns the value; accepts an optional default.
- ``d.clear()`` removes all entries.

.. code-block:: python

   del e2sp["two"]
   removed = e2sp.pop("three", None)
   print(len(e2sp))    # number of remaining entries

Iterating Over a Dictionary
-----------------------------

.. index:: dict.keys(), dict.values(), dict.items(), for; dict

.. code-block:: python

   e2sp = {"one": "uno", "two": "dos", "three": "tres"}

   for key in e2sp:             # iterate over keys (insertion order)
       print(key, "->", e2sp[key])

   for key in e2sp.keys():      # explicit keys view
       print(key)

   for val in e2sp.values():    # values view
       print(val)

   for key, val in e2sp.items():  # key-value pairs
       print(f"{key}: {val}")

Output of the last loop:

.. code-block:: none

   one: uno
   two: dos
   three: tres

Key Type Restriction
--------------------

.. index:: dict; key must be immutable

Dictionary keys must be *immutable* — strings, numbers, and tuples are
valid keys; lists are not.  This restriction exists because of how hash
tables work (see :ref:`Dictionary-Efficiency`).
