.. index:: review questions; data structures

.. _Review-Data-Structures:

Chapter Review Questions
========================

#.  LIFO.

    a.  What does LIFO stand for?
    b.  Which data structure follows LIFO order?

#.  FIFO.

    a.  What does FIFO stand for?
    b.  Which data structure follows FIFO order?

#.  Why is ``collections.deque`` preferred over a plain Python list for
    implementing a queue?

#.  Stacks with Python lists.

    a.  When using a Python list as a stack, which end is the "top" —
        index 0 or the last index?
    b.  Which list methods correspond to push and pop?

#.  Write code to push the values 1, 2, 3 onto a stack, then pop and
    print each value.  What order do they print in?

#.  What does ``None`` represent in a singly linked list?

#.  Trace what happens to the ``head`` pointer when you call ``prepend``
    on an empty linked list, then call it again on the resulting
    one-element list.

#.  Index access performance.

    a.  What is the time complexity of index access (``lst[i]``) for a
        Python list?
    b.  What is it for a linked list?
    c.  Why do they differ?

#.  Given the linked list ``5 -> 10 -> 20 -> None``, show the state after
    calling ``remove(10)``.

#.  Trade-offs between linked lists and Python lists.

    a.  Name one situation where a linked list has a performance advantage.
    b.  Name one situation where a Python list is faster.
