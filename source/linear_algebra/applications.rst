.. index:: perceptron; linear algebra, neural network; single layer,
           activation function, AI; linear algebra connection
   ACM-IEEE CS2013; IS1 Fundamental Issues
   ACM-IEEE CS2023; IS1 Fundamental Issues

.. _Linear-Algebra-Applications:

Applications: From Algebra to AI
==================================

.. note::
   *Source:* Python-specific — no equivalent in the C# edition.

.. todo::

   Write the applications section covering:

   - Polynomial evaluation (Horner's method) as a motivating warm-up;
     cross-reference the ``hardware`` chapter where it was introduced
   - A single perceptron: inputs as a vector, weights as a vector,
     bias as a scalar, output = step(dot(weights, inputs) + bias)
   - Walk through a concrete example (e.g. AND gate) step by step
   - Show how a layer of neurons is just matrix–vector multiplication
   - Brief discussion of why numpy is essential at real scale
     (cross-reference the Monte Carlo case study timing results)
   - Optionally: least-squares line fitting as a practical algebra example
   - Review questions / exercises connecting back to the vector and
     matrix sections
