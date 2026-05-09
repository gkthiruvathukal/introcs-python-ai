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

The CS Course Sequence
----------------------

.. index::
   CS0; Computing Principles
   CS1; Introduction to Computer Science
   CS2; Data Structures
   CS3; Algorithms
   course sequence; CS curriculum

The ACM/IEEE curriculum frameworks assume a standard undergraduate CS course
progression. The table below maps the informal labels used in this chapter
to their typical course titles and content focus.

.. list-table::
   :header-rows: 1
   :widths: 10 28 62

   * - Label
     - Common Course Title(s)
     - Focus
   * - **CS0**
     - Computing Principles;
       AP CS Principles;
       Introduction to Computing
     - Conceptual introduction to computing for non-majors or as a bridge
       course. Minimal or no programming; often uses block-based languages
       (Scratch), spreadsheets, or very simple Python/JavaScript scripts.
       Covers the societal impact of computing, the internet, data, and
       algorithms at a high level.
   * - **CS1**
     - Introduction to Computer Science;
       Introduction to Programming;
       Foundations of Computer Science
     - First programming course for majors. Variables, types, expressions,
       conditionals, loops, functions, basic I/O, and introductory data
       structures (lists, dictionaries). Typically taught in Python, Java,
       or C++. *This textbook targets CS1.*
   * - **CS2**
     - Data Structures;
       Data Structures and Algorithms;
       Object-Oriented Programming
     - Second programming course. Inheritance and polymorphism, linked
       lists, stacks, queues, trees, graphs, sorting algorithms, and
       introductory complexity analysis (Big-O). OOP design principles.
       Discrete Mathematics is often a co-requisite or prerequisite.
   * - **CS3**
     - Algorithms;
       Algorithm Design and Analysis;
       Systems Programming;
       Computer Organization
     - "CS3" is not a single course — it represents the tier of courses
       taken after CS2. Common CS3-level courses include: a formal
       *Algorithms* course (NP-completeness, dynamic programming,
       graph algorithms), *Systems Programming* (C, memory management,
       processes and threads), and *Computer Organization* (assembly
       language, caches, pipelines).
   * - **CS3+**
     - Compilers; Operating Systems;
       Programming Languages;
       Theory of Computation;
       Artificial Intelligence
     - Upper-division and graduate courses that build on a full CS1–CS3
       foundation. KUs at this level are not expected in an introductory
       curriculum.

How to Read the KA Tables
--------------------------

.. index:: curriculum alignment; coverage levels

Each Knowledge Area table below lists **every** Knowledge Unit in that area —
including units this textbook does not address. The **Coverage** column uses:

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

The **Course Level** column shows where a KU is *first expected* in a typical
CS curriculum — CS0, CS1, CS2, CS3, or CS3+. The Gap Analysis section focuses
on KUs at the CS1 level, since this is a CS1 textbook.

Coverage Summary
----------------

.. index:: curriculum alignment; summary

.. list-table::
   :header-rows: 1
   :widths: 34 10 8 8 8 14

   * - Knowledge Area
     - Total KUs
     - Full
     - Partial
     - Minimal
     - Not Covered
   * - SDF — Software Development Fundamentals
     - 4
     - 2
     - 2
     - 0
     - 0
   * - PL — Programming Languages
     - 10
     - 0
     - 3
     - 2
     - 5
   * - AL — Algorithms and Complexity
     - 7
     - 0
     - 1
     - 2
     - 4
   * - SP — Social Issues and Professional Practice
     - 9
     - 1
     - 1
     - 0
     - 7
   * - AR — Architecture and Organization
     - 8
     - 0
     - 0
     - 2
     - 6
   * - SE — Software Engineering
     - 10
     - 0
     - 4
     - 0
     - 6

Not-covered counts include both CS1-level gaps and CS2+/CS3+ topics that are
intentionally out of scope for a first course. The per-KA tables distinguish
these via the Course Level column.

Software Development Fundamentals (SDF)
----------------------------------------

.. index::
   CS2013; SDF
   CS2023; SDF
   SDF; Software Development Fundamentals

SDF is the Knowledge Area most directly targeted by a first programming course.
CS2013 assigns all four KUs to Core Tier 1 or Tier 1/2.  This textbook covers
SDF thoroughly — it is the backbone of the curriculum.

.. list-table::
   :header-rows: 1
   :widths: 26 10 8 36 20

   * - Knowledge Unit
     - CS2013 Tier
     - Level
     - Textbook Chapters / Notes
     - Coverage
   * - **SDF1** Algorithms and Design
     - Tier 1
     - CS1
     - Context, Data, Functions
     - **Full**
   * - **SDF2** Fundamental Programming Concepts
     - Tier 1
     - CS1
     - Data, Functions, Decisions, While, For,
       Files, User Input, Recursion
     - **Full**
   * - **SDF3** Fundamental Data Structures
     - Tier 1/2
     - CS1
     - Lists, Tuples, Dicts, Lists of Dicts,
       Dict Algorithms, Data Structures.
       *Missing:* binary search trees, graphs
       (CS2 topics).
     - **Partial**
   * - **SDF4** Development Methods
     - Tier 1
     - CS1
     - Testing, Error Handling.
       *Missing:* systematic debugging strategies,
       refactoring as a standalone topic.
     - **Partial**

.. index::
   SDF; Algorithms and Design
   SDF; Fundamental Programming Concepts
   SDF; Fundamental Data Structures
   SDF; Development Methods

**CS2023 note.** CS2023 retains all four SDF KUs and adds an explicit
competency requiring students to *select* the appropriate control structure
for a given problem — a distinction this textbook honours through its
separate ``while`` and ``for`` chapters.

Programming Languages (PL)
---------------------------

.. index::
   CS2013; PL
   CS2023; PL
   PL; Programming Languages

CS2013 defines ten PL KUs. PL1 and PL4 are Core Tier 1 CS1 topics; PL2 and
PL3 become relevant by CS2. PL5–PL10 are CS2+/CS3+ and are not expected in
a first course. CS2023 reorganises and elevates type systems and functional
programming.

.. list-table::
   :header-rows: 1
   :widths: 26 10 8 36 20

   * - Knowledge Unit
     - CS2013 Tier
     - Level
     - Textbook Chapters / Notes
     - Coverage
   * - **PL1** Object-Oriented Programming
     - Tier 1
     - CS1
     - Classes.
       *Missing:* inheritance, subclasses,
       ``super()``, method overriding, polymorphism
       (CS2 depth, but basic OOP is CS1).
     - **Partial**
   * - **PL2** Functional Programming
     - Tier 2
     - CS2
     - For (list comprehensions), Recursion
       (memoisation via ``lru_cache``).
       *Missing:* closures, ``map``/``filter``,
       higher-order functions as a paradigm.
     - **Minimal**
   * - **PL3** Event-Driven and Reactive Programming
     - Tier 2
     - CS1
     - GUI (Tkinter event loop, callbacks,
       ``command=`` bindings).
       *Missing:* reactive/stream programming models.
     - **Partial**
   * - **PL4** Basic Type Systems
     - Tier 1
     - CS1
     - Data, Functions (type hints, ``typing``
       module). *Missing:* formal type compatibility
       rules, type inference.
     - **Partial**
   * - **PL5** Program Representation
     - Tier 2
     - CS2
     - (CS2 topic — not addressed)
     - **—**
   * - **PL6** Language Translation and Execution
     - Tier 2
     - CS2
     - Modules (``__name__``, interpreter model).
       Superficial; bytecode and runtime model absent.
     - **Minimal**
   * - **PL7** Syntax Analysis
     - Tier 2
     - CS3
     - (CS3 topic — not addressed)
     - **—**
   * - **PL8** Semantics
     - Elective
     - CS3+
     - (CS3+ topic — not addressed)
     - **—**
   * - **PL9** Pragmatics
     - Tier 2
     - CS2
     - (CS2 topic — not addressed)
     - **—**
   * - **PL10** Logic Programming
     - Elective
     - CS3+
     - (CS3+ topic — not addressed)
     - **—**

.. index::
   PL; Object-Oriented Programming
   PL; Functional Programming
   PL; Event-Driven Programming
   PL; Basic Type Systems
   PL; Language Translation and Execution

**CS2023 note.** CS2023 elevates PL2/Functional Programming from Tier 2 to
*Should*, reflecting the industry shift toward functional styles in Python,
JavaScript, and Rust. It also introduces a dedicated *Type Systems and
Semantics* KU aligned with Python's gradual-typing model; current coverage
could be deepened. Inheritance and polymorphism remain *Must*-level; their
absence is the largest single PL gap.

Algorithms and Complexity (AL)
-------------------------------

.. index::
   CS2013; AL
   CS2023; AL
   AL; Algorithms and Complexity

CS2013 has seven AL KUs. AL1–AL3 are Core Tier 1 but are primarily taught in
CS2 (Data Structures), where formal analysis, sorting theory, and tree/graph
algorithms are the main subject. AL4–AL7 are Tier 2 or Elective and belong
to a dedicated CS3-level Algorithms course.

.. list-table::
   :header-rows: 1
   :widths: 26 10 8 36 20

   * - Knowledge Unit
     - CS2013 Tier
     - Level
     - Textbook Chapters / Notes
     - Coverage
   * - **AL1** Basic Analysis
     - Tier 1
     - CS2
     - Lists, Data Structures (informal Big-O
       comparisons). *Missing:* formal asymptotic
       notation, recurrence relations, space/time
       trade-offs.
     - **Minimal**
   * - **AL2** Algorithmic Strategies
     - Tier 1
     - CS2
     - Recursion (divide-and-conquer).
       *Missing:* greedy algorithms, explicit dynamic
       programming, backtracking.
     - **Minimal**
   * - **AL3** Fundamental Data Structures and Algorithms
     - Tier 1
     - CS2
     - Lists (sequential/binary search; selection,
       bubble, Timsort), Dicts (hash tables,
       conceptual), Data Structures (stacks, queues,
       linked lists). *Missing:* binary search trees,
       graph algorithms (BFS, DFS).
     - **Partial**
   * - **AL4** Basic Computability Theory
     - Tier 2
     - CS3
     - (CS3 topic — not addressed)
     - **—**
   * - **AL5** The Complexity Classes P and NP
     - Tier 2
     - CS3
     - (CS3 topic — not addressed)
     - **—**
   * - **AL6** Automata Theory
     - Elective
     - CS3+
     - (CS3+ topic — not addressed)
     - **—**
   * - **AL7** Advanced Computational Complexity
     - Elective
     - CS3+
     - (CS3+ topic — not addressed)
     - **—**

.. index::
   AL; Basic Analysis
   AL; Algorithmic Strategies
   AL; Fundamental Data Structures and Algorithms

**CS2023 note.** CS2023 retains AL1–AL3 at *Must* level and adds stronger
guidance on analysing recursive algorithms via recurrence relations. The
Recursion chapter provides the right examples but does not derive the
corresponding complexity expressions.

Social Issues and Professional Practice (SP)
--------------------------------------------

.. index::
   CS2013; SP
   CS2023; SP
   SP; Social Issues and Professional Practice

CS2013 has nine SP KUs. SP1–SP3 (Social Context, Analytical Tools, and
Professional Ethics) are Core Tier 1 and are expected in every CS programme
including CS1. SP4–SP6 are Tier 2, appropriate for CS1 but often deferred to
CS2. SP7, SP8, and SP9 are Elective; SP8 (History) is addressed in full.

.. list-table::
   :header-rows: 1
   :widths: 26 10 8 36 20

   * - Knowledge Unit
     - CS2013 Tier
     - Level
     - Textbook Chapters / Notes
     - Coverage
   * - **SP1** Social Context
     - Tier 1
     - CS1
     - Context (motivational framing of computing's
       societal role). *Missing:* structured analysis
       of computing's impact on employment, culture,
       and underrepresented communities.
     - **Partial**
   * - **SP2** Analytical Tools
     - Tier 1
     - CS1
     - (Not addressed — ethical reasoning frameworks
       such as consequentialism and deontology are
       not covered)
     - **—**
   * - **SP3** Professional Ethics
     - Tier 1/2
     - CS1
     - (Not addressed — ACM Code of Ethics, academic
       integrity, computing law not covered)
     - **—**
   * - **SP4** Intellectual Property
     - Tier 2
     - CS1
     - (Not addressed — copyright, open-source
       licensing not covered)
     - **—**
   * - **SP5** Privacy and Civil Liberties
     - Tier 2
     - CS1
     - (Not addressed — data privacy, surveillance,
       encryption policy not covered)
     - **—**
   * - **SP6** Professional Communication
     - Tier 2
     - CS2
     - (CS2 topic — technical writing, oral
       presentations not addressed)
     - **—**
   * - **SP7** Sustainability
     - Elective
     - CS2
     - (CS2 topic — not addressed)
     - **—**
   * - **SP8** History
     - Elective
     - CS1
     - Computing History (prehistory through stored-
       program era; key figures including women ENIAC
       programmers and Ada Lovelace).
     - **Full**
   * - **SP9** Economics of Computing
     - Elective
     - CS2
     - (CS2 topic — not addressed)
     - **—**

.. index::
   SP; Social Context
   SP; Analytical Tools
   SP; Professional Ethics
   SP; Intellectual Property
   SP; Privacy and Civil Liberties
   SP; History
   ACM Code of Ethics; not covered

**CS2023 note.** CS2023 makes Professional Ethics a *Must* topic and expands
it to include AI ethics, algorithmic bias, and data privacy. It also adds a
new *Diversity, Equity, and Inclusion* KU. The Computing History chapter
partially addresses DEI history through the ENIAC programmers and Ada Lovelace,
but a systematic treatment is needed.

Architecture and Organization (AR)
------------------------------------

.. index::
   CS2013; AR
   CS2023; AR
   AR; Architecture and Organization

CS2013 has eight AR KUs. AR1 and AR2 are Core Tier 1 and expected at a
conceptual level in CS1; AR3 (Assembly Level) is Tier 1 but is the primary
subject of a CS2/CS3-level Computer Organization course. AR4–AR8 are Tier 2
or Elective and belong to upper-division systems courses.

.. list-table::
   :header-rows: 1
   :widths: 26 10 8 36 20

   * - Knowledge Unit
     - CS2013 Tier
     - Level
     - Textbook Chapters / Notes
     - Coverage
   * - **AR1** Digital Logic and Digital Systems
     - Tier 1
     - CS2
     - Hardware (CPU, RAM, storage overview),
       Computing History (von Neumann architecture).
       *Missing:* Boolean gates, combinational
       circuits, fetch-decode-execute cycle in detail.
     - **Minimal**
   * - **AR2** Machine Level Representation of Data
     - Tier 1
     - CS2
     - Data (bits, bytes, f-string format specifiers
       for hex/binary), Computing History (Pascaline,
       two's complement mentioned historically).
       *Missing:* signed/unsigned integers, IEEE 754
       floating point, two's complement arithmetic.
     - **Minimal**
   * - **AR3** Assembly Level Machine Organization
     - Tier 1
     - CS2
     - (CS2/Systems topic — not addressed)
     - **—**
   * - **AR4** Memory System Organization and Architecture
     - Tier 2
     - CS3
     - (CS3 topic — not addressed)
     - **—**
   * - **AR5** Interfacing and Communication
     - Tier 2
     - CS3
     - (CS3 topic — not addressed)
     - **—**
   * - **AR6** Functional Organization
     - Tier 2
     - CS3
     - (CS3 topic — not addressed)
     - **—**
   * - **AR7** Multiprocessing and Alternative Architectures
     - Elective
     - CS3+
     - (CS3+ topic — not addressed)
     - **—**
   * - **AR8** Performance Enhancements
     - Elective
     - CS3+
     - (CS3+ topic — not addressed)
     - **—**

.. index::
   AR; Digital Logic and Digital Systems
   AR; Machine Level Representation of Data
   AR; Assembly Level Machine Organization

**CS2023 note.** CS2023 retains AR1 and AR2 at *Must* level but clarifies
that a CS1 course need only achieve a *conceptual* treatment of hardware
organisation — gate-level circuits and assembly language remain CS2 expectations.

Software Engineering (SE)
--------------------------

.. index::
   CS2013; SE
   CS2023; SE
   SE; Software Engineering

CS2013 has ten SE KUs. SE3 (Tools and Environments) is Core Tier 1 and the
only SE KU expected at CS1. SE1, SE6, and SE7 bridge CS1 and CS2; the
remaining six KUs (SE2, SE4, SE5, SE8–SE10) belong to CS2+ software
engineering courses.

.. list-table::
   :header-rows: 1
   :widths: 26 10 8 36 20

   * - Knowledge Unit
     - CS2013 Tier
     - Level
     - Textbook Chapters / Notes
     - Coverage
   * - **SE1** Software Processes
     - Tier 2
     - CS2
     - Testing (test-first development),
       Basic String Ops (problem-solving framework).
       *Missing:* SDLC models, agile methods,
       iterative development as a process.
     - **Partial**
   * - **SE2** Project Management
     - Tier 2
     - CS2
     - (CS2 topic — not addressed)
     - **—**
   * - **SE3** Tools and Environments
     - Tier 1
     - CS1
     - Terminal (CLI, shell commands, redirection),
       Testing (pytest), User Input (``sys.argv``).
       *Missing:* version control (lab stub exists
       but content not yet written).
     - **Partial**
   * - **SE4** Requirements Engineering
     - Tier 2
     - CS2
     - (CS2 topic — not addressed)
     - **—**
   * - **SE5** Software Design
     - Tier 2
     - CS2
     - (CS2 topic — not addressed)
     - **—**
   * - **SE6** Software Construction
     - Tier 2
     - CS1
     - Testing (docstrings, type hints, code style).
       *Missing:* code review, pair programming,
       static analysis tools.
     - **Partial**
   * - **SE7** Verification and Validation
     - Tier 2
     - CS1
     - Testing (pytest unit tests, assert statements,
       test coverage concept). *Missing:* integration
       testing, regression testing, formal V&V.
     - **Partial**
   * - **SE8** Software Evolution
     - Elective
     - CS3+
     - (CS3+ topic — not addressed)
     - **—**
   * - **SE9** Software Reliability
     - Elective
     - CS3+
     - (CS3+ topic — not addressed)
     - **—**
   * - **SE10** Formal Methods
     - Elective
     - CS3+
     - (CS3+ topic — not addressed)
     - **—**

.. index::
   SE; Software Processes
   SE; Tools and Environments
   SE; Software Construction
   SE; Verification and Validation
   version control; not covered

**CS2023 note.** CS2023 promotes version control (Git) to *Must* at the
introductory level, elevating it from a Tier 2 detail to an expected CS1
competency. The existing appendix stub ``lab-versioncontrol.rst`` would, once
completed, close this gap.

Gap Analysis
------------

.. index:: curriculum alignment; gap analysis, curriculum; gaps

The table below consolidates every KU rated **Minimal** or **—** that falls
within the CS1 course level. CS2/CS3/CS3+ topics are intentionally deferred
and are not listed as gaps for a CS1 textbook.

.. list-table::
   :header-rows: 1
   :widths: 20 8 8 34 30

   * - Gap
     - KU
     - Priority
     - What Is Missing
     - Suggested Remedy
   * - Professional ethics
     - SP3
     - **High**
     - ACM Code of Ethics; academic integrity;
       computing law; AI ethics and algorithmic
       bias (CS2023 adds these).
     - Add a dedicated section to the Context
       chapter or a short standalone chapter.
   * - Ethical reasoning tools
     - SP2
     - **High**
     - Philosophical frameworks (consequentialism,
       deontology, virtue ethics) for evaluating
       computing decisions.
     - Combine with the SP3 remediation above.
   * - Inheritance and polymorphism
     - PL1
     - **High**
     - Subclasses, ``super()``, method overriding,
       duck typing as Python's polymorphism model.
     - Extend the Classes chapter with a second
       section on inheritance.
   * - Intellectual property
     - SP4
     - Medium
     - Copyright, open-source licensing (MIT, GPL,
       Apache), software patents.
     - Add a short section to the Context or
       Modules chapter (e.g., choosing a licence
       for your own project).
   * - Privacy and civil liberties
     - SP5
     - Medium
     - Data collection, surveillance, encryption
       policy, GDPR concepts.
     - Weave into the Internet Data chapter as
       an ethical reflection after API usage.
   * - Version control
     - SE3
     - Medium
     - Git workflow; commits; branches;
       pull requests; ``git log`` / ``git blame``.
     - Complete ``appendix/lab-versioncontrol.rst``.
   * - Event-driven depth
     - PL3
     - Low
     - Reactive/stream programming models beyond
       simple widget callbacks.
     - Extend the GUI chapter; appropriate for
       CS1 enrichment.

Notes on CS2023
---------------

.. index:: CS2023; differences from CS2013, CS2023; competency framework

CS2023 represents an evolution rather than a revolution of CS2013. The
following changes are most relevant to this textbook:

**Competency-based framing.** CS2023 defines *competencies* (knowledge +
skills + dispositions) alongside traditional topic lists. A competency for
SDF2/Fundamental Programming Concepts, for example, requires students not
just to understand loops but to *select the appropriate loop construct* for a
given problem — a distinction this textbook honours through its explicit
``while`` vs. ``for`` chapters.

**Professional Ethics elevated.** Ethics moved from Tier 1/Elective in CS2013
to *Must* in CS2023 across SP2 and SP3. The gap identified above is more
urgent under CS2023.

**Functional programming elevated.** CS2023 raises PL2/Functional Programming
from Tier 2 to *Should* — one level below *Must* — reflecting the industry
trend toward functional styles in Python, JavaScript, and Rust.

**Type systems expanded.** CS2023 introduces a dedicated *Type Systems and
Semantics* KU (building on PL4) that includes gradual typing — highly relevant
to Python's ``typing`` module and the type-hint approach taken throughout this
textbook. Deepening that coverage would meet this expectation.

**Version control promoted.** CS2023 elevates SE3/Version Control to *Must*
at the CS1 level, reflecting industry consensus that Git is a day-one skill.

**New: Diversity, Equity, and Inclusion.** CS2023 adds a KU requiring
programmes to address DEI in computing contexts. The Computing History chapter
partially addresses this through its coverage of the ENIAC programmers and
Ada Lovelace, but a more systematic treatment is needed.

Recommendations for Instructors
---------------------------------

.. index:: curriculum alignment; instructor recommendations

This textbook is designed as a CS1 course and intentionally defers some
topics (formal algorithm analysis, trees and graphs, assembly language,
compilers) to CS2 and later courses. The following additions would bring it
to near-full CS2013 Core Tier 1 coverage for a CS1 context:

1. **Add an ethics section** (closes SP2 + SP3) to the Context chapter
   covering the ACM Code of Ethics, ethical reasoning frameworks, academic
   integrity, and basic computing law. This is the highest-priority gap
   under both CS2013 and CS2023.

2. **Add an inheritance section** (closes PL1) to the Classes chapter
   demonstrating subclasses, ``super()``, and method overriding with a
   concrete example (e.g., extending the ``Contact`` class to
   ``ProfessionalContact``).

3. **Complete the version control lab** (closes SE3) in
   ``appendix/lab-versioncontrol.rst`` covering Git commits, branches, and
   the pull-request workflow. This is *Must*-level in CS2023.

4. **Weave privacy and IP notes** (partially closes SP4 + SP5) into the
   Internet Data chapter when discussing API keys, rate limits, and data
   collected from users.

Topics such as formal Big-O proofs, binary search trees, greedy algorithms,
and machine-level data representation are better addressed in CS2 (Data
Structures). Topics such as Boolean gates, assembly language, and the
fetch-decode-execute cycle belong in a CS2/CS3-level Computer Organization
course. This textbook lays the groundwork for all of them through its
coverage of recursion, stacks/queues/linked lists, and the hardware and
computing history chapters.
