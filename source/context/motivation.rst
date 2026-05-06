Motivation for This Book
========================

.. note::

   *Source:* Pedagogy and Why Python sections drawn from the SE4ML Python
   chapter (``chapter_python.rst``, lines 14–110).  Characteristics of Python
   list is an original synthesis.

This is really a preface, but the Sphinx publishing environment we use does not
have a separate preface section.

Pedagogy
--------

Our first aim is to provide a good introduction and conceptual framework for
computer science — not an encyclopedic coverage of Python.  Python will not be
most students' only language, or necessarily the most used.  Designing and
creating algorithms in a particular language is an important skill requiring
ongoing effort, so most of the text is centered on concrete Python programs.

We tend to introduce examples first, then the general syntax, then more
examples and exercises.  There are review questions at the end of most chapters.
Labs are intended as early practice on a subject, with generally small bits
requested at a time.  There are also larger assignments in the appendix.

Why Python?
-----------

Python is a good first language for several reasons.

**It is interactive.**  You can type statements directly into the Python
interpreter and see results immediately, without writing a complete program
first.  This makes it easy to experiment.

**It is concise.**  A Python program that does something useful is often
significantly shorter than the equivalent in Java or C#.  There is less
*boilerplate* — required scaffolding that does not itself express the
programmer's intent.

**It is widely used.**  Python is one of the most popular programming
languages in the world.  It is used in web development, scientific computing,
data science, artificial intelligence, scripting, and automation.

**It is dynamically typed.**  Variables do not need to be declared.  A variable
takes the type of whatever value is assigned to it.  This means you can focus on
the problem you are solving rather than managing type declarations.

**It is readable.**  Python uses indentation to show structure, instead of
braces.  Programs that follow Python's style conventions tend to look like
structured English prose.

Characteristics of Python
--------------------------

Here is a brief overview of Python's key characteristics.

**Scripting.**
Python does not require a separate compile step.  The Python interpreter
can execute programs directly.  You can also type statements interactively
at the ``>>>`` prompt.

**Dynamically typed.**
Variables are not declared.  A value of any type may be assigned to any
variable.  The *value* has a type; the *variable* does not.

**High-level.**
Python has high-level data structures built into the language, such as
lists, dictionaries, and sets.  Memory management is automatic.

**Modular.**
Python programs are organized as collections of modules.  Each module is a
``.py`` file.  The standard library provides an enormous set of ready-to-use
modules.

**Object-oriented.**
Python supports object-oriented programming with classes and inheritance.
Unlike some languages, Python does not *require* you to use objects for
everything.  This book introduces procedural programming first, then
objects.

Object-oriented programming is introduced gradually.  After the chapter on
functions you can read the first sections of the classes chapter to get an
early look at defining your own objects; but the full chapter is placed after
collections, where objects are most naturally useful.

Programming in the Age of Artificial Intelligence
--------------------------------------------------

A reasonable question today is: *if AI can write code, why learn to program?*
We think this gets the situation exactly backwards — and we have heard this
question before.

.. note::

   The argument in this section is developed more fully in:

   Chandra N. Sekharan and George K. Thiruvathukal,
   *"Now's the Time: Computer Science Must Evolve to Emphasize Software
   and Systems Engineering with Artificial Intelligence (AI),"*
   IEEE Computer, Education Department, 2026.
   `arXiv:2604.27230 <https://arxiv.org/abs/2604.27230>`_

   That paper contends that CS education must shift its focus so that
   programming, data structures, and algorithms serve as foundational
   elements within a systems and engineering curriculum — not as ends in
   themselves.  This book is a practical companion to that argument.

A Pattern of Disruption
^^^^^^^^^^^^^^^^^^^^^^^^

Every generation of programmers has faced a tool that was supposed to make
programming knowledge unnecessary.  Each time, the same anxiety arose, and
each time, the answer turned out to be the same.

**The calculator** (1970s) was going to end mathematical thinking.  Instead
it shifted emphasis toward understanding *when* and *why* to compute, not
just how to execute arithmetic by hand.  Mathematical literacy became more
important, not less.

**High-level languages and compilers** threatened assembly programmers who
feared no one would understand machines anymore.  The field grew enormously,
and the programmers who understood what compilers were doing remained the
most effective ones.

**The Web and search engines** (1990s) raised the question: why memorize
anything if you can look it up?  Yet expertise still determined who asked
the right questions and who could evaluate the answers returned.

**Wikipedia** made encyclopedic knowledge freely available overnight.  The
concern was that students would stop learning facts.  What actually happened
is that background knowledge became *more* important, not less — because
you need a mental framework to know which article to look for, whether to
trust it, and what it means in context.

**Blogs, tutorials, and documentation sites** made it easy to find
step-by-step guides for nearly any programming task.  Assembling working
code from online examples became a normal part of practice.  It still
required judgment about which example was relevant, correct, and secure.

**Text messaging and mobile autocorrect** were supposed to ruin writing.
People still need to communicate clearly; the tool changed the mechanics
but not the underlying need for coherent thought.

**Stack Overflow and copy-paste programming** (2000s–present) normalized
finding a working code snippet and dropping it into a project.  This has
always carried the same risk: using something you do not understand.
Experienced engineers learned to read every line before committing it;
less experienced ones accumulated technical debt and security holes.

**GitHub Copilot and AI code completion** (early 2020s) accelerated this
further, generating whole functions from a comment.  The same debate
re-emerged, louder.

**Generative AI** (now) is the latest step in this progression — not a
break from it.  The crucial difference is *velocity*.  AI does not
introduce a new kind of risk; it raises the speed at which copy-paste
culture operates and makes the output look more authoritative because it
is more fluent and more tailored.  A Stack Overflow snippet can be traced
to a source you can read and critique.  AI output arrives without
provenance, confident in tone, and wrong in ways that are harder to spot
precisely because the surface looks so clean.

Each disruption raised the floor — routine tasks got automated — and raised
the bar for what counts as meaningful human contribution.  Deep knowledge
did not become obsolete; it became the thing that distinguished engineers
who directed the tools well from those who were directed by them.

Reading Before Writing
^^^^^^^^^^^^^^^^^^^^^^^

In every discipline where writing matters, we expect people to read deeply
before they can write well.  A student of literature who has never read a
novel is unlikely to write one well.  A scientist who has never studied
prior work is unlikely to design a meaningful experiment, let alone
critique someone else's conclusions.  A journalist who has never read good
reporting is unlikely to recognise it when they produce it.

The same principle applies to code.  AI tools produce code as output.  If
you have never written or read code yourself, you have little foundation
for judging whether that output is correct, efficient, or secure.  You are
unlikely to spot the mistake you have never learned to recognise.  It is
hard to formulate a precise question if you lack the vocabulary to describe
what you want.  The background knowledge is not optional — it is what makes
the tool useful rather than dangerous.

**AI output is code, and code requires a reader.**
Even when AI writes most of the code, a person must evaluate it — for
correctness, for security, for maintainability, and for fit with the
surrounding system.  That evaluation requires genuine understanding.
Pressing "accept" without comprehension is not engineering; it is hoping.

**Communicating requirements is programming under another name.**
Describing what a system should do precisely enough for AI — or any
engineer — to build it correctly requires thinking in terms of data,
control flow, edge cases, and interfaces.  The clearer your mental model
of how a program works, the better your prompts, your specifications, and
your ability to recognise when the result misses the mark.  Programming
knowledge does not become less relevant in this setting; it becomes the
lens through which all of it is done.

**Deep knowledge creates deep engagement.**
Students who understand algorithms, data structures, and how computers
actually work will extract far more value from AI tools than students who
treat them as black boxes.  They will know which suggestions are clever,
which are naive, and which tradeoffs matter for their particular problem.
Shallow users of AI consistently get shallow results.

**AI makes mistakes, and the mistakes are subtle.**
Current AI models can produce code that looks entirely plausible, compiles
without errors, passes basic tests — and is still wrong.  Off-by-one
errors, misunderstood requirements, incorrect assumptions about edge cases,
and latent security vulnerabilities are all real failure modes.  The most
reliable detector of these mistakes is a programmer who understands the
problem deeply.  Do not outsource your ability to spot errors to the same
system that introduced them.

**Ownership does not transfer to the tool.**
When AI-generated code ships and something goes wrong, a human is still
responsible.  That person needs enough expertise to have caught the problem
— or to explain convincingly why they could not.  The accountability stays
with the engineer, not the assistant.

**The tools will change; the fundamentals will not.**
The specific AI assistant available today will be superseded, retrained, or
replaced within a few years.  The ability to reason clearly about
computation — to decompose a problem, choose an appropriate data structure,
analyse an algorithm's behaviour — will remain useful for as long as
computers exist.  This course teaches those fundamentals.  The AI tools are
for you to use along the way; the understanding is what you keep.

**Human actuation and the limits of current AI.**
We do not rule out the possibility that Artificial General Intelligence
(AGI) — systems capable of autonomous reasoning and self-directed action
across arbitrary domains — may eventually change this picture.  That
remains an open question, and a subject of serious ongoing debate.  What
we can say about the present is more straightforward: today's AI systems,
including large language models and the agents built on top of them,
reliably perform well when a knowledgeable human is in the loop — setting
the goal, evaluating the output, catching errors, and deciding what to do
next.  They are tools that amplify human intent, not substitutes for it.
The human remains the prime mover: initiating the task, interpreting the
result, and taking responsibility for what gets built.  That is unlikely
to change soon, and it means that developing your own judgment, knowledge,
and critical eye is as important now as it has ever been.

Software Engineering, Automation, and Prototyping
--------------------------------------------------

The oldest promise in software engineering
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Software engineering has pursued the automation of software development
since the field began.  **CASE tools** — Computer-Aided Software
Engineering — emerged in the 1980s and 1990s with an ambitious promise:
draw your design in a formal diagram, and the tool generates the code.
Round-trip engineering would keep diagrams and implementation in sync.
Formal specification languages would compile directly to running systems.
The vision was that the drudgery of coding would be automated away,
freeing engineers to think at a higher level.

It largely did not work — not because the vision was wrong, but because
the hard part of building software was never the typing.  It was knowing
what to build, expressing requirements with enough precision that the gap
between intent and implementation could be closed, and recognising when
the result did or did not match the original need.  CASE tools could
automate the transcription of a design; they could not supply the design
itself.

AI agents and LLMs are, in many ways, the first genuine realisation of
what CASE tools were reaching for.  For the first time, a tool can take
an imprecise natural-language description and produce working code at a
level of fluency that earlier automation never approached.  The promise
is finally, partially, coming true.

But the lesson from four decades of software engineering is that this
makes the non-automatable parts *more* important, not less.  Those parts
are: knowing what you want, expressing it clearly, and verifying that
what you got is what you asked for.  None of those things can be done for
you by a tool, because they require understanding the problem in the
first place.

Requirements before code
^^^^^^^^^^^^^^^^^^^^^^^^^

Good software engineering practice has always held that you should know
what you want to build before you build it.  This sounds obvious but is
routinely ignored.  The damage done by jumping straight to code —
building the wrong thing quickly, accumulating assumptions that harden
into bugs, discovering misunderstood requirements only after significant
investment — is one of the oldest recurring problems in the field.

**Prototyping** is the disciplined response: build the smallest thing
that tests your most important assumption, learn whether you are right as
fast as possible, and avoid investing heavily in a direction that turns
out to be wrong.  Fail fast, or succeed fast — either outcome is
valuable.  What you are trying to avoid is building a great deal before
you learn anything.

AI accelerates prototyping dramatically.  You can get from an idea to a
running sketch in minutes rather than hours.  This is genuinely useful.
But speed only helps if you know what you are testing.  Without clear
requirements thinking — without knowing what "correct" looks like before
you see the output — you are not prototyping.  You are just arriving at
wrong faster.

The authors of this book see coding as something you do *after* you know
what you want to do.  The thinking comes first: what is the problem,
what are the inputs and outputs, what are the edge cases, what does
success look like?  Code is the precise expression of answers to those
questions.  AI can help you write the expression.  It is unlikely to
answer the questions for you.

