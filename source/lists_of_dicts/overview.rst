.. index:: lists of dictionaries, nested data, records, CRUD, factory function

.. _Lists-Of-Dictionaries:

Lists of Dictionaries
=====================

.. note::
   *Source:* Contributed by PhD students in COMP 501 at Loyola University Chicago.

In earlier chapters we learned that a dictionary represents a single entity with
labeled fields — one student, one product, one book. But real applications rarely
manage just one record. A school tracks hundreds of students; a store manages
thousands of products. When you need a collection of records that all share the same
structure, a **list of dictionaries** is the natural tool.

Think of it like a spreadsheet: each dictionary is one row, with consistent column
names (keys) across every row. The list holds all the rows together.

Why Lists of Dictionaries?
--------------------------

Consider tracking students with separate parallel lists:

.. code-block:: python

   names = ["Alice", "Bob", "Charlie"]
   ages  = [20,      22,    21      ]
   gpas  = [3.8,     3.6,   3.9     ]

Adding a student means appending to three lists. Removing one means deleting from
three lists at the correct index. One mistake and the data is misaligned.

A list of dictionaries keeps each record self-contained:

.. code-block:: python

   students = [
       {"name": "Alice Johnson", "age": 20, "major": "Computer Science", "gpa": 3.8},
       {"name": "Bob Martinez",  "age": 22, "major": "Mathematics",      "gpa": 3.6},
       {"name": "Charlie Davis", "age": 21, "major": "Physics",          "gpa": 3.9},
   ]

Adding or removing a student now touches exactly one item in the list. The data
stays synchronized because each record is a complete, independent unit.

The One-Dictionary-Per-Record Principle
----------------------------------------

Each dictionary in the list should represent exactly one complete entity.

.. code-block:: python

   # INCORRECT — one student split across three dictionaries
   students = [
       {"name": "Alice"},
       {"age": 20},
       {"gpa": 3.8},
   ]

   # CORRECT — each dictionary is one complete student
   students = [
       {"name": "Alice", "age": 20, "gpa": 3.8},
       {"name": "Bob",   "age": 22, "gpa": 3.6},
   ]

Consistent Structure with a Factory Function
---------------------------------------------

When all records must share the same keys and value types, a **factory function**
enforces that consistency:

.. code-block:: python

   def create_student(name, age, gpa, major="Undecided"):
       if not isinstance(name, str) or not name.strip():
           raise ValueError("Name must be a non-empty string.")
       if not 0.0 <= gpa <= 4.0:
           raise ValueError("GPA must be between 0.0 and 4.0.")
       return {"name": name, "age": age, "gpa": gpa, "major": major}

   students = []
   students.append(create_student("Alice Johnson", 20, 3.8, "Computer Science"))
   students.append(create_student("Bob Martinez",  22, 3.6, "Mathematics"))
   students.append(create_student("Charlie Davis", 21, 3.9))  # uses default major

The factory function is a single source of truth for what a record looks like. It
prevents key-name typos, sets sensible defaults, and catches invalid values early.

Accessing Data
--------------

Accessing data in a list of dictionaries chains two operations: a list index, then
a dictionary key.

.. code-block:: python

   first_name = students[0]["name"]
   last_gpa   = students[-1]["gpa"]

   print(first_name)   # Alice Johnson
   print(last_gpa)     # 3.9

To safely access a key that might be missing, use ``.get()``:

.. code-block:: python

   email = students[0].get("email", "not provided")

Iterating Over Records
-----------------------

A ``for`` loop processes every record in the collection:

.. code-block:: python

   for student in students:
       print(f"{student['name']} ({student['major']}) — GPA: {student['gpa']}")

Output:

.. code-block:: none

   Alice Johnson (Computer Science) — GPA: 3.8
   Bob Martinez (Mathematics) — GPA: 3.6
   Charlie Davis (Undecided) — GPA: 3.9

Filtering Records
-----------------

Collect records that meet a condition into a new list:

.. code-block:: python

   honor_roll = []
   for student in students:
       if student["gpa"] >= 3.7:
           honor_roll.append(student)

Or using a list comprehension:

.. code-block:: python

   honor_roll = [s for s in students if s["gpa"] >= 3.7]

Searching for a Record
-----------------------

Find the first record that matches a condition:

.. code-block:: python

   def find_student(students, name):
       for student in students:
           if student["name"] == name:
               return student
       return None

   result = find_student(students, "Bob Martinez")
   if result:
       print(result)

Updating a Record
-----------------

Locate the record and assign a new value to its key:

.. code-block:: python

   for student in students:
       if student["name"] == "Alice Johnson":
           student["gpa"] = 3.9
           break

Sorting
-------

``sorted()`` accepts a ``key`` function that extracts the value to sort by:

.. code-block:: python

   by_gpa  = sorted(students, key=lambda s: s["gpa"], reverse=True)
   by_name = sorted(students, key=lambda s: s["name"])

Grouping Records
----------------

Collect records that share a common field value into a dictionary of lists:

.. code-block:: python

   by_major = {}
   for student in students:
       major = student["major"]
       if major not in by_major:
           by_major[major] = []
       by_major[major].append(student)

Lists of Dictionaries and JSON
-------------------------------

JSON data maps directly to Python lists and dictionaries. The ``json`` module
handles the conversion:

.. code-block:: python

   import json

   # Convert to JSON
   json_str = json.dumps(students, indent=2)
   print(json_str)

   # Convert back to a list of dictionaries
   data = json.loads(json_str)

This makes lists of dictionaries the natural format for reading API responses and
working with data files.

Exercises
---------

1. Create a list of at least five product dictionaries, each with keys ``id``,
   ``name``, ``price``, ``quantity``, and ``category``.
2. Write a function ``total_value(products)`` that returns the total inventory
   value (sum of ``price * quantity`` for all products).
3. Write a function ``low_stock(products, threshold)`` that returns a list of
   products with ``quantity`` below the threshold.
4. Sort the product list by price (ascending) and print the result.
5. Group the products by ``category`` and print how many items are in each group.
6. Write a factory function ``create_product(...)`` with appropriate validation,
   then rebuild the list using it.
