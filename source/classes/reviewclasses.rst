.. index:: review questions; classes

.. _Review-Classes:

Chapter Review Questions
========================

#.  What is the difference between a *class* and an *instance* of a class?

#.  What is ``__init__`` and when is it called?

#.  The ``self`` parameter.

    a.  Why does every instance method have ``self`` as its first parameter?
    b.  Do you pass ``self`` explicitly when calling a method?

#.  Instance variables vs. local variables.

    a.  What is an *instance variable*?
    b.  What is a *local variable* inside a method?
    c.  How long does each live?

#.  The ``__str__`` method.

    a.  What should ``__str__`` return?
    b.  When does Python call it automatically?

#.  What is the difference between ``__str__`` and ``__repr__``?

#.  Given a class ``Dog`` with ``__init__(self, name, breed)``, write the
    line that creates a ``Dog`` named ``"Rex"`` of breed ``"Lab"``.

#.  What Python convention signals that an attribute is intended to be
    private (not accessed from outside the class)?

#.  In the ``Rational`` class, ``__add__`` is defined.  What expression in
    user code triggers a call to ``__add__``?

#.  The ``@dataclass`` decorator.

    a.  What does ``@dataclass`` generate automatically?
    b.  What does it *not* generate?

#.  When would you prefer ``@dataclass(frozen=True)`` over a plain
    ``@dataclass``?

#.  What is *composition* in object-oriented design?  Give a one-sentence
    example.
