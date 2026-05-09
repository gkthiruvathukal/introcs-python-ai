.. index::
   CS2013; curriculum alignment
   CS2023; curriculum alignment
   ACM; computing curriculum
   IEEE; computing curriculum
   curriculum; ACM/IEEE standards

.. _Curriculum-Alignment:

Alignment with ACM/IEEE Curriculum Standards
============================================

.. note::
   *Source:* Python-specific — no direct C# equivalent.

This chapter maps the content of *Introduction to Computer Science in Python*
against the two most widely used computing curriculum frameworks published by
the ACM and IEEE Computer Society:

- **CS2013** — *Computer Science Curricula 2013* (ACM/IEEE-CS Joint Task Force).
  The established reference used by the majority of accredited CS programmes.
  It organises content into **Knowledge Areas (KAs)**, each subdivided into
  **Knowledge Units (KUs)**, with topics rated Core Tier 1, Core Tier 2, or
  Elective.

- **CS2023** — *Computer Science Curricula 2023* (ACM/IEEE-CS, published
  December 2023).  The current revision; it retains the KA/KU structure but
  introduces a competency-based framework and revises the tier terminology
  to *Must* / *Should* / *May*.

.. warning::
   The CS2013 mappings in this chapter are authoritative. The CS2023 notes
   represent the authors' best understanding of a recently published document;
   instructors should verify CS2023 mappings against the official ACM/IEEE-CS
   publication before using them for formal accreditation purposes.

How to Read This Chapter
------------------------

.. index:: curriculum alignment; coverage levels

Each table below covers one Knowledge Area. The **Coverage** column uses the
following four levels:

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Level
     - Meaning
   * - **Full**
     - All or nearly all core topics are substantively addressed.
   * - **Partial**
     - Most core topics are addressed; identifiable gaps remain.
   * - **Minimal**
     - The topic is introduced but not developed to the depth
       the standard expects.
   * - **—**
     - Topic is absent from the textbook.

The **Gap Analysis** section at the end consolidates every "Minimal" or
"—" entry and discusses what would be needed to reach full coverage.

Coverage Summary
----------------

.. index:: curriculum alignment; summary

The following table gives a bird's-eye view across all Knowledge Areas
relevant to an introductory course.

.. list-table::
   :header-rows: 1
   :widths: 40 15 15 15 15

   * - Knowledge Area
     - KUs covered
     - Full
     - Partial / Minimal
     - Not covered
   * - SDF — Software Development Fundamentals
     - 4 of 4
     - 2
     - 2
     - 0
   * - PL — Programming Languages
     - 4 of 10
     - 0
     - 3
     - 1
   * - AL — Algorithms and Complexity
     - 3 of 7
     - 0
     - 2
     - 1
   * - SP — Social Issues and Professional Practice
     - 3 of 9
     - 1
     - 1
     - 1
   * - AR — Architecture and Organization
     - 2 of 8
     - 0
     - 0
     - 2
   * - SE — Software Engineering
     - 2 of 10
     - 0
     - 2
     - 0

Software Development Fundamentals (SDF)
----------------------------------------

.. index::
   CS2013; SDF
   CS2023; SDF
   SDF; Software Development Fundamentals

SDF is the most directly relevant Knowledge Area for a first programming
course. CS2013 assigns all four of its KUs to Core Tier 1 or Tier 2. CS2023
retains the SDF structure largely intact under the same name.

.. list-table::
   :header-rows: 1
   :widths: 28 10 32 15 15

   * - Knowledge Unit
     - CS2013
     - Key Topics Addressed
     - Chapter(s)
     - Coverage
   * - SDF/Algorithms and Design
     - Tier 1
     - Algorithm properties; problem-solving strategies;
       input-process-output model; pseudocode;
       relationship between algorithms and programs
     - Context, Data, Functions
     - **Full**
   * - SDF/Fundamental Programming Concepts
     - Tier 1
     - Syntax and semantics; variables and primitive types;
       expressions and assignments; I/O and file I/O;
       conditionals; iteration; functions and parameter
       passing; recursion
     - Data, Functions, Decisions, While, For, Files,
       User Input, Recursion
     - **Full**
   * - SDF/Fundamental Data Structures
     - Tier 1/2
     - Strings; arrays (lists); records (dicts);
       abstract data types; stacks and queues;
       linked lists; sorting; searching.
       *Gaps:* binary trees and graphs not implemented.
     - Basic String Ops, Lists, Tuples,
       Dictionaries, Lists of Dicts,
       Dict Algorithms, Data Structures
     - **Partial**
   * - SDF/Development Methods
     - Tier 1
     - Unit testing; test-first development;
       documentation and type hints; error handling.
       *Gaps:* systematic debugging strategies and
       refactoring not covered as standalone topics.
     - Testing, Error Handling
     - **Partial**

.. index::
   SDF; Algorithms and Design
   SDF; Fundamental Programming Concepts
   SDF; Fundamental Data Structures
   SDF; Development Methods

**CS2023 note.** CS2023 retains all four SDF KUs. It adds an explicit
emphasis on *ethical* dimensions of software development (e.g., writing
accessible, inclusive code) that is not yet addressed in this textbook.

Programming Languages (PL)
---------------------------

.. index::
   CS2013; PL
   CS2023; PL
   PL; Programming Languages

CS2013 has ten PL KUs; a first course typically touches four. CS2023 renames
and reorganises the PL KUs somewhat, placing greater emphasis on type systems
and functional paradigms.

.. list-table::
   :header-rows: 1
   :widths: 28 10 32 15 15

   * - Knowledge Unit
     - CS2013
     - Key Topics Addressed
     - Chapter(s)
     - Coverage
   * - PL/Object-Oriented Programming
     - Tier 1
     - Classes; encapsulation; information hiding;
       separation of behaviour and implementation;
       ``__init__``, ``__str__``, ``__repr__``.
       *Gaps:* inheritance and polymorphism absent.
     - Classes
     - **Partial**
   * - PL/Basic Type Systems
     - Tier 1
     - Types as value sets + operations; primitive types;
       compound types; dynamic typing; type hints.
       *Gaps:* type inference and formal type compatibility
       not treated.
     - Data, Functions (type hints)
     - **Partial**
   * - PL/Functional Programming
     - Tier 2
     - List comprehensions; ``lambda``; ``sorted`` with key
       functions; memoisation via ``functools.lru_cache``.
       *Gaps:* closures, higher-order functions as a
       paradigm, and purely functional style not covered.
     - For (comprehensions), Tuples,
       Recursion (memoisation)
     - **Minimal**
   * - PL/Event-Driven and Reactive Programming
     - Tier 2
     - Event loop; widgets; callback functions; ``command=``.
     - GUI
     - **Partial**
   * - PL/Language Translation and Execution
     - Tier 2
     - Interpreted vs. compiled execution; the role of
       the interpreter; ``__name__ == '__main__'``.
     - Modules
     - **Minimal**

.. index::
   PL; Object-Oriented Programming
   PL; Basic Type Systems
   PL; Functional Programming
   PL; Event-Driven Programming
   PL; Language Translation and Execution

**CS2023 note.** CS2023 elevates type systems and functional programming to
higher priority and adds a KU on *Language Design and Evolution*. Inheritance
and polymorphism remain expected for Tier 1 coverage; their absence is the
single largest PL gap in this textbook.

Algorithms and Complexity (AL)
-------------------------------

.. index::
   CS2013; AL
   CS2023; AL
   AL; Algorithms and Complexity

CS2013 has seven AL KUs; a first course is expected to address three
(Basic Analysis, Algorithmic Strategies, and Fundamental Data Structures
and Algorithms) at Tier 1.

.. list-table::
   :header-rows: 1
   :widths: 28 10 32 15 15

   * - Knowledge Unit
     - CS2013
     - Key Topics Addressed
     - Chapter(s)
     - Coverage
   * - AL/Basic Analysis
     - Tier 1
     - Big-O notation; best/worst/expected case;
       O(1), O(N), O(N log N) comparisons.
       *Gaps:* formal asymptotic proofs; recurrence
       relations not covered.
     - Lists (sorting, searching),
       Data Structures
     - **Minimal**
   * - AL/Algorithmic Strategies
     - Tier 1
     - Divide-and-conquer (recursion); memoisation
       (dynamic programming flavour).
       *Gaps:* greedy algorithms, explicit dynamic
       programming, backtracking not covered.
     - Recursion
     - **Minimal**
   * - AL/Fundamental Data Structures and Algorithms
     - Tier 1
     - Sequential and binary search; selection, bubble,
       insertion sort; Timsort (O(N log N)); hash tables
       (conceptual); stacks and queues.
       *Gaps:* binary search trees, graph algorithms.
     - Lists (sorting, searching),
       Dictionaries (hashing), Data Structures
     - **Partial**

.. index::
   AL; Basic Analysis
   AL; Algorithmic Strategies
   AL; Fundamental Data Structures and Algorithms

**CS2023 note.** CS2023 retains the same three intro-level AL KUs. It adds
stronger guidance on analysing recursive algorithms (via recurrence relations),
which aligns with this textbook's recursion chapter but only superficially.

Social Issues and Professional Practice (SP)
--------------------------------------------

.. index::
   CS2013; SP
   CS2023; SP
   SP; Social Issues and Professional Practice

CS2013 has nine SP KUs. Core Tier 1 includes Social Context, Analytical
Tools, and Professional Ethics. CS2023 expands SP significantly, adding KUs
on *Diversity, Equity, and Inclusion* and *Environmental Sustainability*.

.. list-table::
   :header-rows: 1
   :widths: 28 10 32 15 15

   * - Knowledge Unit
     - CS2013
     - Key Topics Addressed
     - Chapter(s)
     - Coverage
   * - SP/Social Context
     - Tier 1
     - Social implications of computing; impact on
       employment and society; computing and culture.
     - Context (motivation)
     - **Partial**
   * - SP/History
     - Elective
     - Prehistory and mechanical computers; stored-program
       era; programming languages; the Internet; key
       figures including women pioneers.
     - Computing History
     - **Full**
   * - SP/Professional Ethics
     - Tier 1
     - ACM Code of Ethics; plagiarism and academic
       integrity; community values and law.
     - —
     - **—**

.. index::
   SP; Social Context
   SP; History
   SP; Professional Ethics
   ACM Code of Ethics; not covered

**CS2023 note.** CS2023 makes Professional Ethics a *Must* topic and expands
it to include AI ethics, algorithmic bias, and data privacy — none of which
are covered in this textbook. This is a significant gap for programmes seeking
CS2023 alignment.

Architecture and Organization (AR)
------------------------------------

.. index::
   CS2013; AR
   CS2023; AR
   AR; Architecture and Organization

CS2013 has eight AR KUs; an introductory course is expected to cover Digital
Logic and Machine Level Data at Tier 1. Coverage in this textbook is
intentionally high-level to serve a CS1 audience.

.. list-table::
   :header-rows: 1
   :widths: 28 10 32 15 15

   * - Knowledge Unit
     - CS2013
     - Key Topics Addressed
     - Chapter(s)
     - Coverage
   * - AR/Digital Logic and Digital Systems
     - Tier 1
     - Overview of CPU, RAM, storage, I/O, and the
       motherboard; input-process-output model;
       stored-program concept (von Neumann architecture).
       *Gaps:* combinational vs. sequential logic; gate
       circuits not covered.
     - Hardware, Computing History
       (von Neumann)
     - **Minimal**
   * - AR/Machine Level Representation of Data
     - Tier 1
     - Brief mention of bits and bytes; binary and
       hexadecimal via f-string format specifiers.
       *Gaps:* signed/unsigned integers; floating-point
       representation; two's complement not covered as
       a topic (only mentioned historically).
     - Data (f-strings), Computing History
       (Pascaline / two's complement)
     - **Minimal**

.. index::
   AR; Digital Logic and Digital Systems
   AR; Machine Level Representation of Data

**CS2023 note.** CS2023 retains both KUs at *Must* level. The expectation
for a first course remains a conceptual rather than circuit-level treatment,
so the gap is smaller than the raw rating implies.

Software Engineering (SE)
--------------------------

.. index::
   CS2013; SE
   CS2023; SE
   SE; Software Engineering

CS2013 has ten SE KUs. For a CS1 course, only Tools and Environments
is Core Tier 1; the others become relevant in CS2/CS3. This textbook
addresses two SE KUs through its terminal and testing chapters.

.. list-table::
   :header-rows: 1
   :widths: 28 10 32 15 15

   * - Knowledge Unit
     - CS2013
     - Key Topics Addressed
     - Chapter(s)
     - Coverage
   * - SE/Tools and Environments
     - Tier 1
     - Command-line interface; shell commands;
       pytest testing framework; standard streams
       and redirection; ``sys.argv`` / ``argparse``.
       *Gap:* version control (lab stub exists but
       content not yet written).
     - Terminal, Testing, User Input
     - **Partial**
   * - SE/Software Processes
     - Tier 2
     - Test-first development; incremental development;
       problem-solving framework.
     - Basic String Ops
       (problem-solving), Testing
     - **Partial**

.. index::
   SE; Tools and Environments
   SE; Software Processes
   version control; not covered

**CS2023 note.** CS2023 promotes version control (Git) to *Must* at the
introductory level. The existing appendix stub ``lab-versioncontrol.rst``
would, once completed, close this gap.

Gap Analysis
------------

.. index:: curriculum alignment; gap analysis, curriculum; gaps

The table below consolidates every topic rated **Minimal** or **—** (not
covered) and indicates the effort required to address it.

.. list-table::
   :header-rows: 1
   :widths: 20 10 10 35 25

   * - Gap
     - KA/KU
     - Priority
     - What Is Missing
     - Suggested Remedy
   * - Inheritance and polymorphism
     - PL/OOP
     - High
     - Subclasses, ``super()``, method overriding,
       duck typing as Python's polymorphism mechanism.
     - Extend the Classes chapter with a second
       section on inheritance.
   * - Professional ethics
     - SP/Ethics
     - High
     - ACM Code of Ethics; academic integrity;
       computing law; AI ethics (CS2023).
     - Add a dedicated section to the Context
       chapter or a short standalone chapter.
   * - Big-O analysis
     - AL/Basic Analysis
     - Medium
     - Formal notation; recurrence relations;
       space vs. time trade-offs.
     - Deepen the sorting/searching coverage and
       add an analysis section to Data Structures.
   * - Algorithmic strategies
     - AL/Algorithmic Strategies
     - Medium
     - Greedy algorithms; explicit divide-and-conquer
       examples; dynamic programming beyond memoisation.
     - Extend the Recursion chapter or add a new
       Algorithms chapter.
   * - Trees and graphs
     - SDF/FDS, AL/FDSA
     - Medium
     - Binary search trees; graph representation
       and traversal (BFS/DFS).
     - Extend the Data Structures chapter.
   * - Machine-level data representation
     - AR/Machine Level
     - Low (CS1)
     - Binary, octal, hexadecimal; two's complement;
       IEEE 754 floating point.
     - Add a section to the Hardware or Data chapter.
   * - Functional programming
     - PL/Functional
     - Low (CS1)
     - Closures; ``map``/``filter``; purely functional
       style; immutable data.
     - Extend the For or Functions chapter.
   * - Version control
     - SE/Tools
     - Medium
     - Git workflow; commits; branches; pull requests.
     - Complete the existing
       ``appendix/lab-versioncontrol.rst`` stub.
   * - Hardware depth
     - AR/Digital Logic
     - Low (CS1)
     - Boolean gates; combinational circuits; the fetch-
       decode-execute cycle in detail.
     - Beyond scope for CS1; suitable for a companion
       CS Systems or Architecture course.

Notes on CS2023
---------------

.. index:: CS2023; differences from CS2013, CS2023; competency framework

CS2023 represents an evolution rather than a revolution of CS2013. The
following changes are most relevant to this textbook:

**Competency-based framing.** CS2023 defines *competencies* (knowledge +
skills + dispositions) alongside the traditional topic lists. A competency
for SDF/Fundamental Programming Concepts, for example, requires students to
not just understand loops but to *select the appropriate loop construct* for a
given problem — a distinction this textbook honours through its explicit
discussion of ``while`` vs. ``for`` trade-offs.

**Professional Ethics elevated.** Ethics moved from Tier 1/Elective in CS2013
to *Must* in CS2023 across multiple KUs. The gap identified above is more
urgent under CS2023.

**Functional programming elevated.** CS2023 raises functional programming
from Tier 2 to *Should* — one level below *Must* — reflecting the industry
trend toward functional styles in Python, JavaScript, and Rust. This textbook's
minimal coverage of this KU warrants attention.

**Type systems expanded.** CS2023 introduces a distinct KU on *Type Systems
and Semantics* that includes gradual typing — highly relevant to Python's
``typing`` module and the type-hint approach taken throughout this textbook.
The current coverage could be deepened to meet this expectation.

**New: Diversity, Equity, and Inclusion.** CS2023 adds a KU requiring
programmes to address DEI in computing contexts. This textbook's Computing
History chapter partially addresses this through its coverage of the ENIAC
programmers and Ada Lovelace, but a more systematic treatment is needed.

Recommendations for Instructors
---------------------------------

.. index:: curriculum alignment; instructor recommendations

This textbook is designed as a CS1 course and intentionally defers some
topics (inheritance, formal algorithm analysis, discrete structures) to CS2
and later courses. The following three additions would bring it to near-full
CS2013 Core Tier 1/2 coverage for a CS1 context:

1. **Add an ethics section** to the Context chapter covering the ACM Code of
   Ethics, academic integrity, and basic computing law. This closes the single
   highest-priority gap identified above and satisfies both CS2013 and CS2023.

2. **Add an inheritance section** to the Classes chapter demonstrating
   subclasses, ``super()``, and method overriding with a concrete example
   (e.g., extending the ``Contact`` class to ``ProfessionalContact``).

3. **Complete the version control lab** (``appendix/lab-versioncontrol.rst``)
   covering Git commits, branches, and the pull-request workflow. This is
   *Must*-level in CS2023 and increasingly expected even in CS1.

Topics such as greedy algorithms, formal complexity proofs, binary trees, and
machine-level data representation are better addressed in a second-semester
course (Data Structures, Algorithms, or Systems). This textbook lays the
foundation for all of them through its coverage of Big-O notation, recursion,
stacks/queues/linked lists, and the computing history chapter's treatment of
hardware concepts.
