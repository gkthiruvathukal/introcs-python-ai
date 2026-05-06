.. index:: stack, queue, collections.deque

.. _Stacks-Queues:

Stacks and Queues
=================

.. note::

   *Source:* Adapted from the C# edition (``datastructures/datastructures.rst``).
   C#'s ``Stack<T>`` and ``Queue<T>`` are replaced by Python's list-based
   stack and ``collections.deque``.  The abstract data type concepts
   (LIFO, FIFO) are language-agnostic.

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

.. code-block:: python

   class Stack:
       def __init__(self):
           self._data = []

       def push(self, item):
           self._data.append(item)

       def pop(self):
           if self.is_empty():
               raise IndexError("pop from empty stack")
           return self._data.pop()

       def peek(self):
           if self.is_empty():
               raise IndexError("peek at empty stack")
           return self._data[-1]

       def is_empty(self):
           return len(self._data) == 0

       def __len__(self):
           return len(self._data)

Application: Checking Balanced Brackets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: balanced brackets; stack

A classic stack use-case: verify that brackets are correctly matched:

.. code-block:: python

   def is_balanced(s):
       stack = Stack()
       pairs = {")": "(", "]": "[", "}": "{"}
       for ch in s:
           if ch in "([{":
               stack.push(ch)
           elif ch in ")]}":
               if stack.is_empty() or stack.pop() != pairs[ch]:
                   return False
       return stack.is_empty()

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

.. code-block:: python

   from collections import deque

   class Queue:
       def __init__(self):
           self._data = deque()

       def enqueue(self, item):
           self._data.append(item)

       def dequeue(self):
           if self.is_empty():
               raise IndexError("dequeue from empty queue")
           return self._data.popleft()

       def is_empty(self):
           return len(self._data) == 0

       def __len__(self):
           return len(self._data)
