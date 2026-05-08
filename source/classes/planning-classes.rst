.. index:: class; planning, OOP; design

.. _Plan-Classes:

Planning a Class Structure
==========================

.. note::

   *Source:* Adapted from the C# edition (``classes/planning_classes.rst``).
   The design principles — identify nouns as classes, verbs as methods,
   data as instance variables — are language-agnostic.

Before writing code, it pays to think about what classes you need and
what each class is responsible for.

Nouns and Verbs
---------------

.. index:: OOP; nouns as classes

A reliable starting point: read the problem description and

- *Nouns* (especially those that appear in more than one place, or that
  have several pieces of data attached) suggest *classes*.
- *Verbs* associated with a noun suggest *methods* of that class.
- *Adjectives* or data attributes suggest *instance variables*.

Consider a simple library system.  The problem mentions *books*,
*patrons*, and *loans*.  A book has a title, author, and ISBN.  A patron
has a name and a library card number.  A loan connects a book to a patron
and records a due date.  From this, three classes emerge naturally:
``Book``, ``Patron``, and ``Loan``.

Identifying Instance Variables and Methods
-------------------------------------------

.. index:: instance variable; planning, method; planning

For each class, ask:

1. **What data defines an instance?**  These become instance variables.
2. **What can an instance do, or have done to it?**  These become methods.
3. **How should an instance be displayed as a string?**  That's ``__str__``.

For a ``Book`` class:

- Data: ``title``, ``author``, ``isbn``
- Methods: ``__init__``, ``__str__``, ``is_available()``

Keep each class focused on one responsibility.  If a class is doing too
many unrelated things, split it.

Relationships Between Classes
------------------------------

.. index:: OOP; class relationships

Classes interact through their public methods.  A ``Loan`` holds
references to a ``Book`` and a ``Patron``:

.. code-block:: python

   class Loan:
       def __init__(self, book: str, patron: str, due_date: str):
           self.book = book
           self.patron = patron
           self.due_date = due_date

       def __str__(self) -> str:
           return f"{self.patron} borrowed {self.book} (due {self.due_date})"

This pattern — one class holding a reference to another — is called
*composition*.  It is the main way to build larger systems from smaller
classes.

A Checklist
-----------

Before writing a class, be able to answer:

- What instance variables does it have, and what type is each?
- What does ``__init__`` receive as arguments?
- What methods does it expose to the rest of the program?
- What should ``__str__`` return?

If you can answer these questions clearly, writing the code is usually
straightforward.
