.. index:: if; common mistakes, pitfalls

If-Statement Pitfalls
======================

.. note::

   *Source:* Adapted from the C# edition (``decisions/ifpitfalls.rst``).
   Python-specific pitfalls (truthiness testing, ``is None``, missing
   ``elif``) are original additions.

As you start writing ``if`` statements, watch out for these common
mistakes.

.. index:: = vs ==

Using ``=`` Instead of ``==``
------------------------------

In Python, ``=`` is assignment and ``==`` is comparison.  Using ``=``
inside a condition is a ``SyntaxError``:

.. code-block:: python

   # SyntaxError in Python (unlike C, which silently allows this)
   if x = 5:
       print("five")

   # correct
   if x == 5:
       print("five")

Python's syntax rule prevents this entire class of bug.

.. index:: indentation; pitfall

Indentation Errors
------------------

Python uses indentation to define blocks.  Mixing tabs and spaces, or
using inconsistent indentation, causes an ``IndentationError`` or
``TabError``:

.. code-block:: python

   # wrong — second print is not part of the if body
   if x > 0:
       print("positive")
   print("This always runs")   # outside the if

   # correct — both prints inside the body
   if x > 0:
       print("positive")
       print("This also only runs when x > 0")

A good code editor highlights indentation and warns about inconsistencies.

.. index:: elif vs separate if

Missing ``elif`` (Redundant Checks)
--------------------------------------

When cases are mutually exclusive, use ``elif`` rather than separate
``if`` statements.  Using separate ``if`` statements checks all conditions
even after one has matched:

.. code-block:: python

   # wrong — all three ifs are checked even when the first matches
   score = 95
   if score >= 90:
       grade = "A"
   if score >= 80:    # this also runs! grade gets overwritten to "B"
       grade = "B"
   if score >= 70:
       grade = "C"

   # correct — only the first matching branch runs
   if score >= 90:
       grade = "A"
   elif score >= 80:
       grade = "B"
   elif score >= 70:
       grade = "C"

.. index:: truthiness pitfall

Testing Truthiness
------------------

Python allows any value in a condition — not just a true Boolean.  This
can be convenient but also a source of confusion:

.. code-block:: python

   name = input("Enter name: ")

   # works but potentially misleading
   if name:
       print("Name provided.")

   # explicit — clearer intent
   if name != "":
       print("Name provided.")

For ``None`` checks, always use ``is`` (not ``==``):

.. code-block:: python

   result = some_function()

   if result is None:        # correct
       print("No result.")

   if result == None:        # works but not idiomatic
       print("No result.")

   if not result:            # WRONG if 0, [], or "" are valid results
       print("No result.")

.. index:: off-by-one in conditions

Off-by-One in Range Conditions
--------------------------------

When checking membership in a range, be precise about ``<`` vs ``<=``:

.. code-block:: python

   # should include 100 as a valid score, but doesn't
   if 0 <= score < 100:
       print("valid")

   # correct
   if 0 <= score <= 100:
       print("valid")

Always test the boundary values: exactly 0 and exactly 100 in this case.

Forgetting ``else``
-------------------

If a variable is set inside ``if`` but not in an ``else``, it may be
uninitialized when the condition is false:

.. code-block:: python

   if score >= 60:
       status = "pass"
   # if score < 60, status is never set — NameError below!
   print(status)

Fix: always set the variable before the ``if``, or add an ``else``:

.. code-block:: python

   status = "fail"          # default
   if score >= 60:
       status = "pass"
   print(status)
