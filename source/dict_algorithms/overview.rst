.. index:: dictionary algorithms, counting, grouping, filtering, merging, frequency

.. _Dictionary-Algorithms:

Dictionary Algorithms
=====================

.. note::
   *Source:* Contributed by PhD students in COMP 501 at Loyola University Chicago.

Dictionaries are one of Python's most powerful data structures because they map keys
to values with extremely fast lookup times. As programs grow in size and complexity,
certain dictionary patterns appear again and again. This chapter covers the most
important ones.

Counting with Dictionaries
--------------------------

Counting occurrences is one of the most common uses of a dictionary.

.. code-block:: python

   words = ["apple", "banana", "apple", "pear", "banana", "apple"]
   counts = {}

   for w in words:
       if w not in counts:
           counts[w] = 1
       else:
           counts[w] += 1

   print(counts)

Output:

.. code-block:: none

   {'apple': 3, 'banana': 2, 'pear': 1}

The ``.get()`` method makes this more concise:

.. code-block:: python

   counts = {}
   for w in words:
       counts[w] = counts.get(w, 0) + 1

``get(key, 0)`` returns the current count if the key exists, or ``0`` if it does
not, avoiding a ``KeyError``.

Filtering Dictionaries
-----------------------

Build a new dictionary containing only the key/value pairs that satisfy a condition:

.. code-block:: python

   scores = {"Alice": 95, "Bob": 82, "Carol": 71, "Diana": 99}
   high_scores = {}

   for name, score in scores.items():
       if score > 80:
           high_scores[name] = score

   print(high_scores)

Output:

.. code-block:: none

   {'Alice': 95, 'Bob': 82, 'Diana': 99}

Grouping with Dictionaries
---------------------------

Grouping places items that share a characteristic into lists under a common key.

.. code-block:: python

   words = ["apple", "ant", "banana", "berry", "car", "cat"]
   groups = {}

   for w in words:
       first = w[0]
       if first not in groups:
           groups[first] = []
       groups[first].append(w)

   print(groups)

Output:

.. code-block:: none

   {'a': ['apple', 'ant'], 'b': ['banana', 'berry'], 'c': ['car', 'cat']}

The general grouping pattern is:

.. code-block:: none

   for item in data:
       key = some_property(item)
       if key not in groups:
           groups[key] = []
       groups[key].append(item)

``setdefault`` is a convenient shorthand:

.. code-block:: python

   groups = {}
   for w in words:
       groups.setdefault(w[0], []).append(w)

Reversing a Dictionary
-----------------------

Swap keys and values. This works correctly only when values are unique and hashable.

.. code-block:: python

   grades = {"A": 90, "B": 80, "C": 70}
   reversed_grades = {v: k for k, v in grades.items()}
   print(reversed_grades)

Output:

.. code-block:: none

   {90: 'A', 80: 'B', 70: 'C'}

If values are not unique, later entries overwrite earlier ones during the reversal.

Merging Dictionaries
---------------------

Python 3.9+ provides the merge operator ``|``:

.. code-block:: python

   a = {"x": 1, "y": 2}
   b = {"y": 3, "z": 4}

   c = a | b
   print(c)

Output:

.. code-block:: none

   {'x': 1, 'y': 3, 'z': 4}

If both dictionaries share a key, the right-hand dictionary wins. For older Python:

.. code-block:: python

   c = dict(a)
   c.update(b)

Safe Access with ``.get()``
----------------------------

Use ``.get()`` to avoid ``KeyError`` when a key may not exist:

.. code-block:: python

   config = {"debug": True}
   mode = config.get("mode", "production")
   print(mode)

Output:

.. code-block:: none

   production

Nested Dictionaries
--------------------

Dictionaries can hold other dictionaries, allowing hierarchical data:

.. code-block:: python

   student = {
       "name": "Alice",
       "scores": {"math": 90, "science": 85}
   }

   print(student["scores"]["math"])

Output:

.. code-block:: none

   90

Algorithms on Lists of Dictionaries
-------------------------------------

A list of dictionaries is a common format for tabular data (CSV rows, JSON records,
API responses). Several dictionary algorithms apply naturally to this structure.

**Frequency count over a field:**

.. code-block:: python

   people = [
       {"name": "Alice", "age": 30},
       {"name": "Bob",   "age": 25},
       {"name": "Cara",  "age": 30},
   ]

   freq = {}
   for p in people:
       age = p["age"]
       freq[age] = freq.get(age, 0) + 1

   print(freq)

Output:

.. code-block:: none

   {30: 2, 25: 1}

**Index by a unique field** (convert list → dictionary for O(1) lookup):

.. code-block:: python

   index = {p["name"]: p for p in people}
   print(index["Alice"])

Output:

.. code-block:: none

   {'name': 'Alice', 'age': 30}

**Group records by a field:**

.. code-block:: python

   by_age = {}
   for p in people:
       by_age.setdefault(p["age"], []).append(p)

Group by Length (Practice)
--------------------------

Implement a function that groups words by their length:

.. code-block:: python

   def group_by_length(words):
       groups = {}
       for w in words:
           groups.setdefault(len(w), []).append(w)
       return groups

   print(group_by_length(["tea", "to", "apple", "jam", "bag"]))

Output:

.. code-block:: none

   {3: ['tea', 'jam', 'bag'], 2: ['to'], 5: ['apple']}

Real-World Applications
-----------------------

Dictionary algorithms appear throughout software:

- **Analytics pipelines** — counting events, computing statistics.
- **Search indexes** — mapping words to the documents that contain them.
- **Grouping and categorization** — organizing records by department, date,
  or status.
- **Summarizing survey data** — counting responses per answer option.

Recognizing when a problem maps to one of these patterns is a key skill in Python
programming.

Exercises
---------

1. Count the frequency of each character in the string ``"mississippi"``.
2. Given a list of words, filter out any word with fewer than four letters and
   return a dictionary mapping the remaining words to their lengths.
3. Given a list of student records (each a dictionary with ``name``, ``grade``,
   and ``score``), group them by ``grade``.
4. Reverse the dictionary ``{"red": 1, "green": 2, "blue": 3}``. What happens
   if two keys share the same value?
5. Merge two configuration dictionaries so that values in the second dictionary
   take priority over the first.
6. Write a function ``top_n(counts, n)`` that returns the ``n`` most frequent
   items from a frequency dictionary as a sorted list of ``(item, count)`` tuples.
