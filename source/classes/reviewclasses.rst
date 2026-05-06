.. index:: review questions; classes

.. _Review-Classes:

Chapter Review Questions
========================

.. note::

   *Source:* Adapted from the C# edition (``classes/reviewclasses.rst``).
   Questions updated for Python syntax: ``__init__`` replaces constructors,
   ``self`` replaces ``this``, dunder methods replace operator overloading.

#.  What is the difference between a *class* and an *instance* of a class?

#.  What is ``__init__`` and when is it called?

#.  Why does every instance method have ``self`` as its first parameter?
    Do you pass ``self`` explicitly when calling a method?

#.  What is the difference between an *instance variable* and a *local
    variable* inside a method?  How long does each live?

#.  What does ``__str__`` return, and when does Python call it
    automatically?

#.  What is the difference between ``__str__`` and ``__repr__``?

#.  Given a class ``Dog`` with ``__init__(self, name, breed)``, write the
    line that creates a ``Dog`` named ``"Rex"`` of breed ``"Lab"``.

#.  What Python convention signals that an attribute is intended to be
    private (not accessed from outside the class)?

#.  In the ``Rational`` class, ``__add__`` is defined.  What expression in
    user code triggers a call to ``__add__``?

#.  What does ``@dataclass`` generate automatically?  What does it *not*
    generate?

#.  When would you prefer ``@dataclass(frozen=True)`` over a plain
    ``@dataclass``?

#.  What is *composition* in object-oriented design?  Give a one-sentence
    example.
