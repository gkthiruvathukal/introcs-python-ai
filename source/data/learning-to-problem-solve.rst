Learning to Solve Problems
==========================

.. note::

   *Source:* Adapted from the C# edition (``data/learning-to-problem-solve.rst``).
   The six-step framework and bill-splitting example are Python translations
   of the original.

Programming is fundamentally about *problem solving*.  The computer is a tool;
the skill is figuring out how to express a solution in a way the computer can
execute.

A Framework for Problem Solving
---------------------------------

When you encounter a new problem, work through these steps:

1. **Understand the problem.**  What are the inputs?  What is the expected
   output?  Work through a specific example by hand before writing any code.

2. **Identify the data.**  What values do you need to store?  What types
   should they be?  Give them meaningful names.

3. **Break it into steps.**  A program that calculates paint requirements
   needs to: read the room dimensions, calculate wall area, calculate ceiling
   area, and print the results.  Each step is simple; together they solve the
   problem.

4. **Write the code.**  Translate each step into Python.  Start with the
   simplest version that works.

5. **Test.**  Run the program with inputs you can check by hand.  Try edge
   cases: what if one dimension is zero?  What if the user types something
   that is not a number?

6. **Refine.**  Clean up names, add comments where the logic is non-obvious,
   and look for anything that could break.

The Data-in, Calculate, Data-out Pattern
-----------------------------------------

Many programs follow a simple pattern:

.. code-block:: none

   1. Get data from the user (or a file)
   2. Perform calculations
   3. Output the results

The painting program from :ref:`sample-program` follows this pattern exactly.
So do most of the early programs in this book.  Recognizing the pattern helps
you organize your thinking.

Worked Example: Splitting a Bill
---------------------------------

**Problem:** A group of friends had dinner and want to split the bill evenly,
including a 20% tip.

**Step 1 — Understand the problem.**
Inputs: total bill amount, number of people.
Output: amount each person owes.

**Step 2 — Work through an example by hand.**
Bill = $80, people = 4.
Tip = 20% of $80 = $16.
Total = $80 + $16 = $96.
Per person = $96 / 4 = $24.

**Step 3 — Write the code:**

.. code-block:: python

   bill = float(input("Enter the bill amount: $"))
   people = int(input("How many people? "))

   tip = bill * 0.20
   total = bill + tip
   per_person = total / people

   print(f"Each person owes ${per_person:.2f}.")

**Step 4 — Test.**
With bill = 80 and people = 4, the output should be ``Each person owes $24.00.``

Notice how closely the code matches the hand calculation.  Programming at its
best is translating a clear solution into clear code.

Getting Unstuck
---------------

Everyone gets stuck.  A few strategies that help:

- **Print intermediate values.**  Add ``print()`` statements to see what your
  variables hold at each step.
- **Simplify.**  Remove parts of the program until it works, then add them back.
- **Read the error message.**  Python's errors are informative — read them carefully,
  starting from the bottom.
- **Step away.**  A short break often lets you see the problem with fresh eyes.
