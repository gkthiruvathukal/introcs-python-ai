.. index:: review questions; data structures

.. _Review-Data-Structures:

Chapter Review Questions
========================

.. note::

   *Source:* Adapted from the C# edition (``datastructures/datastructures.rst``).
   The C# chapter is a brief placeholder; questions cover the full Python
   content on stacks, queues, and linked lists.

#.  What does LIFO stand for?  Which data structure follows LIFO order?

#.  What does FIFO stand for?  Which data structure follows FIFO order?

#.  Why is ``collections.deque`` preferred over a plain Python list for
    implementing a queue?

#.  In a stack implemented with a Python list, which end is the "top" —
    index 0 or the last index?  Which list methods correspond to push
    and pop?

#.  Write code to push the values 1, 2, 3 onto a stack, then pop and
    print each value.  What order do they print in?

#.  What does ``None`` represent in a singly linked list?

#.  Trace what happens to the ``head`` pointer when you call ``prepend``
    on an empty linked list, then again on the resulting one-element list.

#.  What is the time complexity of index access (``lst[i]``) for a Python
    list vs. a linked list?  Why do they differ?

#.  Given the linked list ``5 -> 10 -> 20 -> None``, show the state after
    calling ``remove(10)``.

#.  Name one situation where a linked list has a performance advantage
    over a Python list, and one situation where a Python list is faster.
