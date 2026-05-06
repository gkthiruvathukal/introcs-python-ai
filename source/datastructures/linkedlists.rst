.. index:: linked list, Node class, singly linked list

.. _Linked-Lists:

Linked Lists
============

.. note::

   *Source:* Adapted from the C# edition (``datastructures/datastructures.rst``).
   Python uses ``None`` where C# uses ``null`` as the end-of-list sentinel.
   The ``Node`` class and linked-list logic are otherwise directly
   analogous to the C# pointer-based implementation.

A *linked list* stores elements in nodes, where each node holds a value
and a reference to the next node.  Unlike Python's built-in list, a
linked list does not require a contiguous block of memory.

The Node Class
--------------

.. index:: Node class

.. code-block:: python

   class Node:
       def __init__(self, data, next_node=None):
           self.data = data
           self.next = next_node

Each node points to the next node in the chain.  The last node's
``next`` is ``None`` — the Python equivalent of a null pointer.

Building a Linked List by Hand
--------------------------------

.. index:: linked list; construction

.. code-block:: python

   # Build the list  1 -> 2 -> 3 -> None
   head = Node(1, Node(2, Node(3)))

Traversal
---------

.. index:: linked list; traversal

Walk the list by following ``next`` until ``None``:

.. code-block:: python

   def print_list(head):
       current = head
       while current is not None:
           print(current.data, end=" -> ")
           current = current.next
       print("None")

.. code-block:: python

   print_list(head)

Output:

.. code-block:: none

   1 -> 2 -> 3 -> None

The SinglyLinkedList Class
--------------------------

.. index:: SinglyLinkedList

A wrapper class manages the ``head`` pointer and provides clean methods:

.. code-block:: python

   class SinglyLinkedList:
       def __init__(self):
           self.head = None

       def prepend(self, data):
           self.head = Node(data, self.head)

       def append(self, data):
           new_node = Node(data)
           if self.head is None:
               self.head = new_node
               return
           current = self.head
           while current.next is not None:
               current = current.next
           current.next = new_node

       def remove(self, data):
           if self.head is None:
               return
           if self.head.data == data:
               self.head = self.head.next
               return
           current = self.head
           while current.next is not None:
               if current.next.data == data:
                   current.next = current.next.next
                   return
               current = current.next

       def __iter__(self):
           current = self.head
           while current is not None:
               yield current.data
               current = current.next

       def __str__(self):
           return " -> ".join(str(x) for x in self) + " -> None"

.. code-block:: python

   lst = SinglyLinkedList()
   lst.append(10)
   lst.append(20)
   lst.append(30)
   lst.prepend(5)
   print(lst)

   lst.remove(20)
   print(lst)

Output:

.. code-block:: none

   5 -> 10 -> 20 -> 30 -> None
   5 -> 10 -> 30 -> None

Performance Comparison
-----------------------

.. index:: linked list; performance

+-------------------+------------+------------+
| Operation         | List       | LinkedList |
+===================+============+============+
| Index access      | O(1)       | O(N)       |
+-------------------+------------+------------+
| Prepend           | O(N)       | O(1)       |
+-------------------+------------+------------+
| Append            | O(1) amort | O(N)       |
+-------------------+------------+------------+
| Insert in middle  | O(N)       | O(N)       |
+-------------------+------------+------------+
| Remove from front | O(N)       | O(1)       |
+-------------------+------------+------------+

Python's built-in list is a dynamic array and is faster for most uses.
Linked lists shine when you need O(1) prepend or frequent insertions at
a known position.
