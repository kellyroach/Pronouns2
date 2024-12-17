FAQ
===

**Frequently Asked Questions (FAQ)**.  Our ANSWER's to some of the
best QUESTION's about each of Pronoun2's Python modules.

.. NOTE:
    Relative paths to the root directory:
        src/docs/build/html/faq.htm
        docs/VaryingRho.pdf
    Hence RST
        `docs/VaryingRho.pdf <../../../../docs/VaryingRho.pdf>`_
    is an RST "external link" which finds docs/VaryingRho.pdf .
    Similarly, we can create hyperlinks for all *.py mentions
    in faq.rst.  Relative path to the root directory:
        src/varying_rho.py
    Hence RST
        `varying_rho.py <../../../../src/varying_rho.py>`_
    is an RST "external link" which finds src/varying_rho.py .

globals.py
----------

**QUESTION:** Is there a specific linguistic framework or theory
this `globals.py <../../../../src/globals.py>`_'s syntax tree
data structures are based on?  The ``Node`` class has many
different types of links (``up``, ``down``, ``left``, ``right``,
``thread``, ``np``, ``chain``, ``col``, etc.) - are these used
for different purposes depending on the node type (``C``, ``S``,
``N``, ``E``)?  The ``Features`` list seems focused on pronoun
and agreement features - is this primarily for handling pronoun
binding and agreement in syntax?

**ANSWER:** The linguistic framework is in my 1980 M.S. thesis
`Pronouns <https://authors.library.caltech.edu/records/mf427-dra49>`_.
accepted by my school, Caltech, in 1980.  There are 36
References in my M.S. thesis' bibliography and I'm building
quite a bit on what other researchers then or earlier had
written about pronouns and anaphora in journals like Linguistic
Inquiry and scholarly books.  ``C`` = conjoined sentence, ``S``
= sentence, ``N`` = noun phrase, ``E`` = is an elaborated copy
of an N-node.  You are right, the ``Features`` list helps
constrain pronoun resolution possibilities.

abstract.py
-----------

**QUESTION:** I notice
`abstract.py <../../../../src/abstract.py>`_ deals with creating
abstract syntax tree diagrams using LaTeX/TikZ. Are these
TikZ diagrams specifically for visualizing the ``C``, ``S``,
``N``, and ``E`` nodes we saw in
`globals.py <../../../../src/globals.py>`_?  Do you use these
diagrams alongside the actual syntax tree implementation, or are
they mainly for documentation/visualization purposes?  Would it
be helpful to mention in other function documentation when they
interact with these diagram generation capabilities?

**ANSWER:** These particular TikZ diagrams only contain
``C``, ``S``, ``N`` nodes, abstract representations of parse
trees of English sentences.  Mainly some visualization and
understanding of the parse trees for human viewers.

chaining.py
-----------

**QUESTION:** Are `chaining.py <../../../../src/chaining.py>`_'s
chain diagrams showing relationships between different instances
of the N-nodes in a parse tree?

**ANSWER:** The chaining diagram hangs E-nodes in columns
beneath the N-nodes of a parse tree of an English sentence.
There are ``chain_link``'s amongst E-nodes between anaphors and
their antecedents (or referents).  The N-nodes and E-nodes can
be representing head nouns, pronouns, and deletion sites.  A
list of all E-nodes encountered by following ``chain_link``'s is
referred to as a "chain".

demo.py
-------

**QUESTION:** In `demo.py <../../../../src/demo.py>`_, what's
the relationship between ``Manager.info`` and ``Manager.debug``
flags, and how do they control what gets included in the output?
I see lots of if-statements checking these flags in different
combinations.

**ANSWER:** Python module
`globals.py <../../../../src/globals.py>`_ defines ``class
Manager``.  ``Manager`` is a singleton class for managing
output streams and file types.  There are two types of
``Manager`` flags:

* Level: ``Manager.info``, ``Manager.debug``, ``Manager.trace``
* Function: ``Manager.abstract_diagram``, ``Manager.features_table``,
  ``Manager.abstract_diagram``, ``Manager.init_table``, ``Manager.new_chain``,
  etc.

Every ``Manager`` flag in a branch of the following tree must be
``True`` before the output functions guarded by those flags are
allowed to ``Manager.write`` anything::

    .
    ├── info
    │   ├── abstract_diagram
    │   ├── features_table
    │   ├── abstract_diagram
    │   ├── nodes_after_chaining
    │   │   └── nodes
    │   ├── chaining_diagram
    │   ├── chaining_table
    │   ├── interpretations_table
    │   ├── summary_table
    │   └── lexicon_table
    ├── debug
    │   ├── nodes_after_parse
    │   │   └── nodes
    │   ├── init_table
    │   │   ├── nodes
    │   │   ├── chaining_diagram
    │   │   └── chaining_table
    │   └── new_chain
    │       ├── nodes
    │       ├── chaining_diagram
    │       └── chaining_table
    └── trace
        └── message

For example, set of flags
{``Manager.debug``, ``Manager.new_chain``, ``Manager.chaining_diagram``}
guards any intermediate calls to function ``chaining_diagram`` while
being called from `table_proc.py <../../../../src/table_proc.py>`_'s
function ``new_chain``.

``Manager.info`` guards high-level function calls.
``Manager.debug`` guards intermediate-level function calls which
can be useful either for detailed appreciation of how the
Python code is performing its analysis or for debugging.
``Manager.trace`` enables `trc.py <../../../../src/trc.py>`_
entry and exit tracing of functions in
`secondary_uty.py <../../../../src/secondary_uty.py>`_ and
`table_proc.py <../../../../src/table_proc.py>`_ .  The
``message`` is not a ``Manager`` flag, but the ``str`` message.
Function ``trc_write`` doesn't print empty ``message``\s.

``Manager`` supports Python's ``with`` statement by maintaining
a ``stack`` of states, allowing nested state management with
automatic state restoration.  ``Manager`` also provides
class-level methods and properties for accessing and updating
its ``state``.

``Manager`` flags usage are exemplified by unit tests and test
outputs such as:

* `test_doc.py <../../../../src/tests/test_doc.py>`_
* `test_doc_debug_trace.pdf <../../../../src/tests/expected/test_doc_debug_trace.pdf>`_

analyzing 109 sentence examples in the same meticulous detail
as do Chapters 8-10 Table Processor I-III of
`Pronouns, Second Edition <../../../../docs/Pronouns2Python.pdf>`_
for sentence (10.1).

doc.py
------

**QUESTION:** Why does `doc.py <../../../../src/doc.py>`_'s
``doc()`` function return a full file path string instead of
writing directly to ``../docs/Demo.tex`` or
``../docs/Demo.txt``? I see it's creating all these analysis
outputs but I want to know where they actually went.

**ANSWER:** The analysis outputs go to the file identified by
``doc``'s return value.  Since doc's input argument ``file``
merely defaults to ``str = "../docs/Demo"``, ``doc()``'s file
isn't required to be ``../docs/Demo.tex`` or
``../docs/Demo.txt`` .  The user can override this default by
supplying a ``file`` argument.

According to `doc.py <../../../../src/doc.py>`_'s ``doc()``'s
code, the ``file_type`` (``FileType.TXT`` or ``FileType.TEX``
corresponding to ``".txt"`` or ``".tex"``), is either supplied
in the ``**kwargs`` passed to ``doc``
(e.g. ``doc(file_type=FileType.TXT)``) or defaults to
``FileType.TEX``. ``FileType.TEX`` is usually the best choice
because PDF output is prettier.

Function ``doc`` writes analysis outputs to a file, but this
file isn't the best documentation, just analytic details of how
all the interpretations of 109 different example sentences were
derived.  The document which explains this type of analysis is
`docs/Pronouns2Python.pdf <../../../../docs/Pronouns2Python.pdf>`_
AKA ``Pronouns, Second Edition (Python Version)`` which is a
2024 LaTeX-formatted version of the `Kelly Roach <https://www.kellyroach.com>`_’s original 1980
Caltech M.S. thesis,
`Pronouns <https://authors.library.caltech.edu/records/mf427-dra49>`_.

examples.py
-----------

**QUESTION:** I notice some
`examples.py <../../../../src/examples.py>`_'s examples are
prefixed with ``*`` (like ``"*John killed herself"``) - are these
meant to indicate ungrammatical sentences?

**ANSWER:** Correct.  S.O.P. for linguists.  Also, ``?`` is a
questionable sentence, and there are some other notations which
my 1980 M.S. thesis
`Pronouns <https://authors.library.caltech.edu/records/mf427-dra49>`_
mentions in its ``Chapter 1, Fundamentals``.

latex.py
--------

**QUESTION:** In `latex.py <../../../../src/latex.py>`_'s LaTeX
output, do `latex.py <../../../../src/latex.py>`_'s tables
appear in a specific order to help readers understand how the
system derives its interpretations step by step?

**ANSWER:** A close examination of
`demo.py <../../../../src/demo.py>`_'s function ``demo_example`` and
functions ``demo_example`` calls in `demo.py <../../../../src/demo.py>`_
will reveal that output functions ``abstract_diagram``,
``xxx_features``, ``xxx_nodes``, ``chaining_diagram``, and
``xxx_interpretations``, where in all cases ``xxx`` is either
``txt`` or ``latex``, are called in a very specific sequence.
This sequence can be fairly said to correspond to the same
sequence required by ``demo_example`` to derive "interpretations" of an
English sentence example.  Our ``demo_example`` is documenting what it
does via these output routines as ``demo_example`` does its processing.

lexicon.py
----------

**QUESTION:** Can you explain what `lexicon.py <../../../../src/lexicon.py>`_'s
function ``lexicon_select`` does?

**ANSWER:** Function ``lexicon_select`` is documented as::

    def lexicon_select(feature_str: str) -> list[str]:
        """Returns list of words in lexicon_dict whose Features match feature_str.
    
        Args:
            feature_str (str): feature string or known lexicon word
            (e.g., '---+-++--' or 'mom')
         
        Returns:
            answer: list[str] of compatible words in lexicon_dict
        """

For example::

    >>> lexicon_select('+--+??+--')
    ['PHI', 'all', 'another', 'any', 'each', 'he', 'her', 'him',
    'none', 'one', 'oneself', 'other', 'she', 'some', 'somebody',
    'that', 'them', 'these', 'they', 'this', 'those', 'what',
    'which', 'who', 'whom']
    >>> lexicon_select('mom')
    ['Anna', 'Janet', 'Jill', 'June', 'Linda', 'Mary', 'Penelope',
    'Sandy', 'Sue', 'asshole', 'aunt', 'blame', 'camel', 'cat',
    'daughter', 'embezzler', 'fish', 'gambler', 'girl',
    'grandmother', 'mosquito', 'mom', 'mother', 'neighbor', 'pig',
    'pilot', 'sheep', 'sister', 'student', 'toy']
    >>> 

modern.py
---------

**QUESTION:** How does `modern.py <../../../../src/modern.py>`_
bridge the gap between raw textual input and LaTeX-ready output?

**ANSWER:** `modern.py <../../../../src/modern.py>`_ serves as a
middle layer in the project's LaTeX output generation code,
translating raw TXT-style strings (e.g., ``"PHI"`` or ``"4A"``) into
LaTeX-friendly representations (e.g., ``"\\phi"`` and
``"${\\texttt{4}_{\\texttt{a}}}$"``). The
`modern.py <../../../../src/modern.py>`_ middle layer allows
LaTeX and TikZ outputs generated by
`abstract.py <../../../../src/abstract.py>`_,
`chaining.py <../../../../src/chaining.py>`_,
`latex.py <../../../../src/latex.py>`_ code to receive
consistent attractive formatting by
`doc.py <../../../../src/doc.py>`_'s LaTeX document generation
code.

node_proc.py
------------

**QUESTION:** Since
`node_proc.py <../../../../src/node_proc.py>`_'s E-nodes are
elaborated copies of N-nodes, does ``new_e_node()`` copy any of
the original N-node's features when creating the E-node?

**ANSWER:** We'll see init_table and new_chain functions in
`table_proc.py <../../../../src/table_proc.py>`_ later on which
call ``new_e_node`` creating E-node's such as ``n``.  Every
E-node n has an ``np_link`` back to the N-node from which ``n``
gets most of its information.  E-node's hang in columns below
N-node's via ``col_link``'s.  There can be more than one E-node
in a column hanging below an N-node.  However, not all the
information that an E-node represents can be discovered by
inspecting its ``np_link`` N-node.  The E-node's ``ftr`` field
may be more filled out with fewer QUESTION marks because the
E-node may ``chain_link`` to and inherit additional feature
information from another E-node.  For example, a deletion site
(``"PHI"``) has lots of ``QUESTION`` marks as an N-node, but
gets many features filled in as an E-node because the deletion
site ``chain_link``'s to another E-node (e.g. ``"John"``) with
many features which are known to be ``PLUS`` or ``MINUS``
(``"John"`` is ``TPF``, not ``PLF``, is ``ANF``, etc.).

parser.py
---------

**QUESTION:** Do the thread_links created during
`parser.py <../../../../src/parser.py>`_'s parsing help with
later traversal of the tree when establishing chains between
nodes?

**ANSWER:** I don't see thread_link being used in any important way
by my Python implementation.  It is hard to guess if it was ever
really important in my Modula-2 implementation I created in
1980, 44 years ago.  The ``thread_link`` is documented in my
M.S. thesis
`Pronouns <https://authors.library.caltech.edu/records/mf427-dra49>`_
as::

    The thread_link field of a C-node, S-node, or N-node links to
    the first node traversed after the C-node, S-node, or N-node in
    a preorder traversal of the C-S-N tree in which it occurs.

We might charitably say we honestly described the implementation
as a P.O.C. prototype and if the ``thread_link`` isn't useful yet,
it might be useful later on if we continued development further
into the future.  "Be Prepared" as the Boy Scouts of America
say.  It costs `parser.py <../../../../src/parser.py>`_'s
``parse`` next to nothing to create the ``Node`` ``thread_link``'s.

primary_uty.py
--------------

**QUESTION:** Since `primary_uty.py <../../../../src/primary_uty.py>`_'s
functions handle both N-nodes and E-nodes by using ``np_link`` to
get back to the original N-node, are these relationships
primarily about syntactic structure rather than specific word
instances?

**ANSWER:** Your perception is correct.  The
`primary_uty.py <../../../../src/primary_uty.py>`_
functions are relationships primarily about syntactic structure
rather than specific word instances.  You will see something
else in `secondary_uty.py <../../../../src/secondary_uty.py>`_ .

secondary_uty.py
----------------

**QUESTION:** Are
`secondary_uty.py <../../../../src/secondary_uty.py>`_'s
secondary utilities what ultimately determine whether a
potential pronoun-antecedent binding is valid, after the primary
structural relationships have been established?

**ANSWER:** Functions in
`table_proc.py <../../../../src/table_proc.py>`_ call functions
in `secondary_uty.py <../../../../src/secondary_uty.py>`_ and
layer on some additional logic that help determine whether a
potential pronoun-antecedent binding is valid.  I will also
point out that "a potential pronoun-antecedent binding is valid"
might not hold up in the context of a complete sentence in which
all such bindings must be put together in a complete
interpretation.  Remember,
`table_interp.py <../../../../src/table_interp.py>`_'s
``interpret`` needs to return interpretations which partitions the
nouns found in a sentence.  Not every chain discovered by the
chaining algorithm which gets put into the chaining table
necessarily survives and get used by ``interpret`` in a sentence
interpretation.

spread.py
---------

**QUESTION:** Can you explain the Spreading Algorithm defined by
`spread.py <../../../../src/spread.py>`_'s function ``spread``?  How
is this algorithm used in your project?

**ANSWER:** The Spreading Algorithm takes a list of angles on
the unit circle and a spreading factor ``rho ∈ [0,1]``, and
outputs a new list of angles that are more evenly distributed
while preserving their relative order. For ``rho < 1``, the algorithm:

1. Unrolls the unit circle onto the real line, mapping the
   angles to positions in ``[0, 2π]``
2. Computes ``delta = 2π*rho/((1-rho)*n)`` where ``n`` is the
   number of angles
3. For each mapped position:

   - Inserts ``(1-α)*delta`` padding before the position
   - Inserts ``α*delta`` padding after the position

   where ``α`` is determined by the "average angle's" relative
   position between its two nearest neighbors
4. Scales this expanded line (now length ``2π + n*delta``) back to
   length ``2π``
5. Rolls the line back into a circle, yielding the spread-out angles

The Spreading Algorithm ensures the "average angle" (angle of the average
of the points on the unit circle) remains fixed. When ``rho=0``,
angles remain unchanged; as ``rho`` approaches ``1``, angles approach
even spacing; and ``rho = 1`` corresponds to the limit, where angles
reaching even spacing.

The Spreading Algorithm helps position arrows around nodes in
`chaining.py <../../../../src/chaining.py>`_'s Tikz diagrams,
preventing arrows from overlapping while maintaining their
general directional relationships.

spread.ipynb
------------

**QUESTION:** Is there an interactive way to explore how the
Spreading Algorithm works in Pronouns2?

**ANSWER:** Jupyter notebook `spread.ipynb` is a freebie which
isn't essential to running the Pronouns2 Python code.  However,
it can provide insight into how our Spreading Algorithm
`spread.py <../../../../src/spread.py>`_ helps to draw
Pronouns2's pretty Tikz chaining diagrams.

Our document `VaryingRho.pdf <../../../../docs/VaryingRho.pdf>`_
goes into greater detail about how this algorithm is used to
tune the placement of arrowheads in Pronouns2's Tikz chaining
diagrams.

For details about how to run and use Jupyter notebook `spread.ipynb`,
see the ``src`` directory's ``README.md`` .

table_interp.py
---------------

**QUESTION:** Looking at both the code and docstring, am I correct
that each "interpretation" in
`table_interp.py <../../../../src/table_interp.py>`_ represents one
possible way that all pronouns in the sentence could be bound to
their antecedents?

**ANSWER:** Correct. An interpretation can be viewed as a partition
of the set of head nouns, pronouns, deletion sites into
equivalence classes.  The equivalence classes happen also to be
adorned with a bit of ``chain_link`` information amounting to a
total ordering on each equivalence class in an interpretation,
called a chain.

table_proc.py
-------------

**QUESTION:** I notice `table_proc.py
<../../../../src/table_proc.py>`_'s ``init_table`` creates only
initial ``"A"`` E-nodes, while new_chain increments subscripts for
additional E-nodes (``"B"``, ``"C"``, etc.) - does this help track
the sequence in which binding possibilities were discovered?

**ANSWER:** In a column of E-nodes beneath an N-node, the entire
column connected by ``col_link``'s, the E-nodes in that column
successively receive subscripts ``"A"``, ``"B"``, ``"C"``,
``"D"``, etc.  In the ``demo_example`` output for a given input English
sentence, it is easy to understand labels, such as ``"JohnD"``,
as referring back to specific E-nodes created during the
analysis of the input English sentence.  The labels, such as
``"JohnD"`` appear later in the ``chaining_diagram`` output, the
``"Chaining"`` table, and the ``"Interpretations"`` table
outputted by ``demo_example`` when ``file_type`` is equal to
``FileType.TXT`` or ``FileType.TEX``.  Here is a portion of ``demo_example``
``FileType.TXT`` output for an example input English sentence::

    (10.1) John wants to give June a present, but he isn't sure she’ll like it.
    
    _________________________________CHAINING________________________________
    !            !           !            !              !     !      !     !
    ! John       ! PHI       ! June       ! present      ! he  ! she  ! it  !
    ! JohnA      ! PHIA      ! JuneA      ! presentA     ! heA ! sheA ! itA !
    ! JohnB^heA  ! PHIB^itA  ! JuneB^sheA ! presentB^itA !     !      !     !
    ! JohnC^PHIA ! PHIC^sheA !            !              !     !      !     !
    ! JohnD^PHID ! PHID^heA  !            !              !     !      !     !
    !____________!___________!____________!______________!_____!______!_____!
    
    ________________INTERPRETATIONS_________________
    !                                              !
    ! JohnD^PHID^heA    JuneB^sheA    presentB^itA !
    !______________________________________________!
    
Chains ``JohnB^heA``, ``JohnC^PHIA``, ``PHIB^itA``,
``PHIC^sheA`` have all been discarded by the ``interpret``
function which couldn't fit these chains into any legitimate
interpretation of the sentence (10.1).

tex.py
------

**QUESTION:** Since `tex.py <../../../../src/tex.py>`_'s
function ``tex_string_width`` is used for TikZ diagram spacing,
does it need to be particularly precise because the diagrams
show chains with arrows and need to avoid visual overlaps?

**ANSWER:** Some of our TikZ diagrams are drawing line segments
between adjacent nouns on the same horizontal line.  These
Tikz diagrams can use the best affordable ``tex_string_width``
function I can create to get these horizontal line segments to
start and end close to the TikZ nodes representing noun
strings, but not too close and not overlap the TikZ nodes
representing noun strings.  Function ``tex_string_width`` does a
good enough approximation of what LaTeX will calculate when
LaTeX converts our Tikz source code into actual Tikz PDF
diagrams.

trc.py
------

**QUESTION:** Python module `trc.py <../../../../src/trc.py>`_
defines trace functions, but I see many trace call sites are
commented out in the code - was this helpful during development
but now mainly kept for future debugging if needed?

**ANSWER:** Yes, `trc.py <../../../../src/trc.py>`_ function
calls are useful for debugging Python code while developing
Python code.  If a Python module is stable, I can simply comment
out the trace function calls in that Python module while
possibly leaving trace function calls still turned on for
unstable Python modules that I am debugging.  Or, if I discover
a bug, I may want the option of rapidly uncommenting existing
previously well chosen and thought out trace function calls in a
Python module suspected of containing the root cause of that
bug.

txt.py
------

**QUESTION:** The `txt.py <../../../../src/txt.py>`_ output
functions seem to handle table formatting with ASCII characters
(like ``!`` for borders) - was this chosen to make the output
readable in any terminal/console environment?

**ANSWER:** The ``_`` and ``!`` characters in TXT versions of our
tables are visually recognizable as table borders to the human eye
because the repeating horizontal and vertical patterns of these
characters in our TXT-friendly Python REPL and also in ``Demo.txt``
files.  The borders are much more beautiful to the human eye in
the ``Demo.pdf`` created from ``Demo.tex`` when LaTeX versions of
our tables are created, replacing ``_`` and ``!`` with ``\hrule``'s and
``\vrule``'s or whatever LaTeX tabular's are doing under the hood.
However, LaTeX source code isn't friendly reading in a Python
REPL.

varying_rho.py
--------------

**QUESTION:** What is the purpose of having
`varying_rho.py <../../../../src/varying_rho.py>`_ inside your
project?  Function ``varying_rho_doc`` isn't being called by
anything else in your project.

**ANSWER:** The bit of code in
`varying_rho.py <../../../../src/varying_rho.py>`_, function
``varying_rho_doc`` included, can be used to recreate the chaining
diagrams in `docs/VaryingRho.pdf <../../../../docs/VaryingRho.pdf>`_ .
`docs/VaryingRho.pdf <../../../../docs/VaryingRho.pdf>`_
illustrates how varying the input rho passed to the Spreading
Algorithm varies the position of arrows around nodes in
`chaining.py <../../../../src/chaining.py>`_'s Tikz diagrams
applied to example sentence (10.1).  Ultimately, we settled on
using ``rho=0.5`` which is a nice compromise between direct flight
arrows and completely spread out arrows.  The
`varying_rho.py <../../../../src/varying_rho.py>`_ code plays no
role in pronoun resolution, today in 2024, nor did any similar
Modula-2 code exist back in 1980.  It's here purely to demo the
Spreading Algorithm in `spread.py <../../../../src/spread.py>`_,
which itself only exists in the project to make modern day 2024
LaTeX Tikz chaining diagrams look prettier.  Code
`spread.py <../../../../src/spread.py>`_, nor anything like it,
existed back in 1980 either.

view.py
-------

**QUESTION:** Are the `view.py <../../../../src/view.py>`_
functions the core string conversion layer that both
`latex.py <../../../../src/latex.py>`_ and
`txt.py <../../../../src/txt.py>`_ build upon for their
different output formats?

**ANSWER:** Yes, the `view.py <../../../../src/view.py>`_
functions are a core string conversion layer that both
`latex.py <../../../../src/latex.py>`_ and
`txt.py <../../../../src/txt.py>`_ build upon for their
different output formats.  Two things are being accomplished:

First, the `view.py <../../../../src/view.py>`_ functions map
implementation-specific ``Node`` and ``Feature`` data structure
information into a much more neutral and beautiful space of
Python lists of strings and Python lists of lists of strings
which can be considered to be beautiful vectors and matrices of
strings.  The `txt.py <../../../../src/txt.py>`_ and
`latex.py <../../../../src/latex.py>`_ functions, on the other
hand, receive beautiful vectors and matrices of strings and
produce necessary but much obscurer TXT and LaTeX output.  The
`view.py <../../../../src/view.py>`_ code doesn't have to be
complicated by awareness of the obscure TXT and LaTeX outputs.
The `txt.py <../../../../src/txt.py>`_ and
`latex.py <../../../../src/latex.py>`_ code doesn't have to be
complicated by awareness of the equally obscure
implementation-specific ``Node`` and ``Feature`` data structures.
In each case, TXT and TEX modes, there are pipelines of workers
specialized to their own tasks that don't need to be educated to
handle the arcane knowledge which the other workers must know
and use.  This pipeline coding approach is a useful coding model
which all good AI chatbots and humans should learn themselves if
they want to write excellent code instead of spaghetti code.

Second, `txt.py <../../../../src/txt.py>`_ and
`latex.py <../../../../src/latex.py>`_ benefit by sharing use of
`view.py <../../../../src/view.py>`_ .  There is less
duplication if `view.py <../../../../src/view.py>`_ can do this
job of converting ``Node`` and ``Feature`` information for both
`txt.py <../../../../src/txt.py>`_ and
`latex.py <../../../../src/latex.py>`_ because
`view.py <../../../../src/view.py>`_ factors out the common
complexity into a single Python module reducing that complexity
to very simple inputs it hands off to
`txt.py <../../../../src/txt.py>`_ and
`latex.py <../../../../src/latex.py>`_ .
