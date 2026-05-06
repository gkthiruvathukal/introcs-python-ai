.. index:: review questions; lists

.. _Review-Lists:

Chapter Review Questions
========================

.. note::

   *Source:* Adapted from the C# edition (``lists/reviewlists.rst`` and
   ``arrays/reviewarrays.rst``).  Questions updated for Python list syntax
   and methods.

#.  What is the index of the first element of a list?  The last?

#.  How do you get the number of elements in a list named ``data``?

#.  Two ways to sort.

    a.  What does ``list.sort()`` do?
    b.  What does ``sorted(lst)`` do?
    c.  When would you prefer each?

#.  What does ``data[2:5]`` return if ``data = [10, 20, 30, 40, 50, 60]``?

#.  What does ``data[-1]`` refer to?

#.  What is the difference between ``list.append(x)`` and
    ``list.extend(other)``?

#.  What error is raised if you call ``data.remove(x)`` and ``x`` is not
    in the list?

#.  The ``pop()`` method.

    a.  What does ``data.pop()`` return if ``data = [1, 2, 3]``?
    b.  What does ``data`` contain after the call?

#.  Write a list comprehension that produces the squares of odd numbers
    from 1 to 9: ``[1, 9, 25, 49, 81]``.

#.  Aliasing.

    .. code-block:: python

       a = [1, 2, 3]
       b = a
       b.append(4)
       print(a)

    a.  What is printed?
    b.  Why is the output surprising?
    c.  How would you make a true independent copy of ``a``?

#.  Linear search vs. binary search.

    a.  What is the time complexity of each?
    b.  What additional requirement does binary search impose on the list?

#.  Trace through one complete pass of bubble sort on ``[5, 3, 1, 4]``
    and show the state of the list after each swap.
