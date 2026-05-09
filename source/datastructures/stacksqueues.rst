.. index:: stack, queue, collections.deque
   ACM-IEEE CS2013; SDF3 Fundamental Data Structures
   ACM-IEEE CS2023; SDF3 Fundamental Data Structures
   ACM-IEEE CS2013; AL3 Fundamental Data Structures and Algorithms
   ACM-IEEE CS2023; AL3 Fundamental Data Structures and Algorithms

.. _Stacks-Queues:

Stacks and Queues
=================

.. note::

   *Source:* Adapted from the C# edition (``datastructures/datastructures.rst``).
   C#'s ``Stack<T>`` and ``Queue<T>`` are replaced by Python's list-based
   stack and ``collections.deque``.  The abstract data type concepts
   (LIFO, FIFO) are language-agnostic.

.. index:: abstract data type, ADT

Stacks and queues are *abstract data types* — they define what operations
are available, not how they are implemented.

Stacks (LIFO)
-------------

.. index:: stack; LIFO, push, pop

A *stack* follows **Last-In, First-Out** order: the most recently added
item is the first to be removed, like a stack of plates.

Operations:

- **push**: add an item to the top
- **pop**: remove and return the top item
- **peek**: inspect the top item without removing it
- **is_empty**: check whether the stack is empty

.. index:: list; as stack, O(1); list.append and pop

**Using a Python list as a stack:**

.. code-block:: python

   stack = []
   stack.append(1)    # push
   stack.append(2)
   stack.append(3)

   print(stack[-1])   # peek: 3
   print(stack.pop()) # pop: 3
   print(stack.pop()) # pop: 2
   print(stack)       # [1]

``list.append()`` adds to the end (top); ``list.pop()`` removes from the
end — both O(1).

A Stack Class
^^^^^^^^^^^^^

.. index:: Stack class

Wrapping the list in a class gives a cleaner interface:

.. literalinclude:: ../../examples/introcs-python/datastructures/stack.py
   :language: python
   :start-after: # start: Stack
   :end-before: # end: Stack

Application: Checking Balanced Brackets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: balanced brackets; stack

A classic stack use-case: verify that brackets are correctly matched:

.. literalinclude:: ../../examples/introcs-python/datastructures/stack.py
   :language: python
   :start-after: # start: is_balanced
   :end-before: # end: is_balanced

.. code-block:: python

   print(is_balanced("({[]})"))   # True
   print(is_balanced("({[})"))    # False

Queues (FIFO)
-------------

.. index:: queue; FIFO, enqueue, dequeue, collections.deque

A *queue* follows **First-In, First-Out** order: like a line of people
waiting, the first to join is the first to leave.

Operations:

- **enqueue**: add an item to the back
- **dequeue**: remove and return the front item
- **is_empty**: check whether the queue is empty

**Using ``collections.deque``:**

.. index:: deque; O(1) both ends, collections.deque; efficiency

A Python list is slow for dequeue (removing from the front is O(N)).
``collections.deque`` supports O(1) operations at both ends:

.. code-block:: python

   from collections import deque

   queue = deque()
   queue.append("Alice")    # enqueue
   queue.append("Bob")
   queue.append("Carol")

   print(queue.popleft())   # dequeue: Alice
   print(queue.popleft())   # dequeue: Bob
   print(queue)             # deque(['Carol'])

A Queue Class
^^^^^^^^^^^^^

.. index:: Queue class

.. literalinclude:: ../../examples/introcs-python/datastructures/queue.py
   :language: python
   :start-after: # start: Queue
   :end-before: # end: Queue
