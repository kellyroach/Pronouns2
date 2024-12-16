.. _Usage:

Usage
=====

In most usage examples, run ``python`` in the ``src``
subdirectory, so that ``python`` will find ``pronouns2.py``,
which ``from pronouns2 import *`` needs.  If you are already
in the ``src`` subdirectory, use ``python`` instead of
``cd src && python``.

Run Minimum Demos
-----------------

::

    $ cd src && python
    >>> from pronouns2 import *
    >>> demo("10.1")
    (10.1) John wants to give June a present, but he isn't sure she’ll like it.
    [['JohnD^PHID^heA', 'JuneB^sheA', 'presentB^itA']]
    >>> demo()
    (1.1) The boy who was fooling her kissed the girl who loved him.
    [['girlB^herA', 'boyB^himA']]
    ...
    (1.91) After John Adams woke up, he was hungry.
    [['JohnB^heA']]
    (1.92) That Oscar was unpopular didn't disturb him.
    [['OscarB^himA']]
    (1.93) For your brother to refuse to pay taxes would get him into trouble.
    [['brotherD^PHIB^himA']]
    (1.94) Anna's complaining about Peter infuriated him.
    [['PeterB^himA']]
    (1.95) The possibility that Fred will be unpopular doesn’t bother him.
    [['FredB^himA']]
    ...
    (10.1) John wants to give June a present, but he isn't sure she’ll like it.
    [['JohnD^PHID^heA', 'JuneB^sheA', 'presentB^itA']]
    ...
    >>> 

Create Minimum Docs
-------------------

::

    $ cd src && python
    >>> from pronouns2 import *
    >>> doc()
    '.../docs/Demo.tex'
    >>> doc(file_type=FileType.TXT)
    '.../docs/Demo.txt'
    >>> quit()
    $ cd ../docs
    $ make Demo.pdf
    ...
    $ open Demo.pdf
    ...
    $ open Demo.txt

(Windows users should use ``start`` instead of ``open``.)

Run Info Demo
-------------

::

    $ cd src && python
    >>> from pronouns2 import *
    >>> demo("10.1", info=True)
    
    ################################################################
    #
    #     (10.1) John wants to give June a present, but he isn't sure she’ll like it.
    #
    ################################################################
    
    _____________________________FEATURES____________________________
    !         !     !     !     !     !     !     !     !     !     !
    !         ! PNF ! FPF ! SPF ! TPF ! PLF ! GNF ! ANF ! RPF ! GEN !
    !    John !  -  !  -  !  -  !  +  !  -  !  -  !  +  !  -  !  -  !
    !     PHI !  +  !  ?  !  ?  !  ?  !  ?  !  ?  !  ?  !  -  !  -  !
    !    June !  -  !  -  !  -  !  +  !  -  !  +  !  +  !  -  !  -  !
    ! present !  -  !  -  !  -  !  +  !  -  !  ?  !  -  !  -  !  -  !
    !      he !  +  !  -  !  -  !  +  !  -  !  -  !  +  !  -  !  -  !
    !     she !  +  !  -  !  -  !  +  !  -  !  +  !  +  !  -  !  -  !
    !      it !  +  !  -  !  -  !  +  !  -  !  ?  !  -  !  -  !  -  !
    !_________!_____!_____!_____!_____!_____!_____!_____!_____!_____!
    
    ___________________________NODES___________________________
    !     !                                                   !
    !  1  ! (C, up:0, dn:2, lt:0, rt:0, th:2, nu:1)           !
    !  2  ! (S, up:1, dn:3, lt:0, rt:8, th:3, nu:2)           !
    !  3  ! (N, lit:John, ftr:[---+--+--], up:2, dn:0,        !
    !     !  lt:0, rt:4, th:4, np:3, ch:0, co:3A, ec:3D,      !
    !     !  pr:0, su:5, nu:3)                                !
    !  3A ! (E, sub:A, ftr:[---+--+--], np:3, ch:0, co:3B)    !
    !  3B ! (E, sub:B, ftr:[---+--+--], np:3, ch:9A, co:3C)   !
    !  3C ! (E, sub:C, ftr:[---+--+--], np:3, ch:5A, co:3D)   !
    !  3D ! (E, sub:D, ftr:[---+--+--], np:3, ch:5D, co:0)    !
    !  4  ! (S, up:2, dn:5, lt:3, rt:0, th:5, nu:4)           !
    !  5  ! (N, lit:PHI, ftr:[+??????--], up:4, dn:0,         !
    !     !  lt:0, rt:6, th:6, np:5, ch:0, co:5A, ec:5D,      !
    !     !  pr:3, su:6, nu:5)                                !
    !  5A ! (E, sub:A, ftr:[+??????--], np:5, ch:0, co:5B)    !
    !  5B ! (E, sub:B, ftr:[+--+-?---], np:5, ch:12A, co:5C)  !
    !  5C ! (E, sub:C, ftr:[+--+-++--], np:5, ch:11A, co:5D)  !
    !  5D ! (E, sub:D, ftr:[+--+--+--], np:5, ch:9A, co:0)    !
    !  6  ! (N, lit:June, ftr:[---+-++--], up:4, dn:0,        !
    !     !  lt:5, rt:7, th:7, np:6, ch:0, co:6A, ec:6B,      !
    !     !  pr:5, su:7, nu:6)                                !
    !  6A ! (E, sub:A, ftr:[---+-++--], np:6, ch:0, co:6B)    !
    !  6B ! (E, sub:B, ftr:[---+-++--], np:6, ch:11A, co:0)   !
    !  7  ! (N, lit:present, ftr:[---+-?---], up:4, dn:0,     !
    !     !  lt:6, rt:0, th:8, np:7, ch:0, co:7A, ec:7B,      !
    !     !  pr:6, su:9, nu:7)                                !
    !  7A ! (E, sub:A, ftr:[---+-?---], np:7, ch:0, co:7B)    !
    !  7B ! (E, sub:B, ftr:[---+-?---], np:7, ch:12A, co:0)   !
    !  8  ! (S, up:1, dn:9, lt:2, rt:0, th:9, nu:8)           !
    !  9  ! (N, lit:he, ftr:[+--+--+--], up:8, dn:0,          !
    !     !  lt:0, rt:10, th:10, np:9, ch:0, co:9A, ec:9A,    !
    !     !  pr:7, su:11, nu:9)                               !
    !  9A ! (E, sub:A, ftr:[+--+--+--], np:9, ch:0, co:0)     !
    ! 10  ! (S, up:8, dn:11, lt:9, rt:0, th:11, nu:10)        !
    ! 11  ! (N, lit:she, ftr:[+--+-++--], up:10, dn:0,        !
    !     !  lt:0, rt:12, th:12, np:11, ch:0, co:11A, ec:11A, !
    !     !  pr:9, su:12, nu:11)                              !
    ! 11A ! (E, sub:A, ftr:[+--+-++--], np:11, ch:0, co:0)    !
    ! 12  ! (N, lit:it, ftr:[+--+-?---], up:10, dn:0,         !
    !     !  lt:11, rt:0, th:0, np:12, ch:0, co:12A, ec:12A,  !
    !     !  pr:11, su:0, nu:12)                              !
    ! 12A ! (E, sub:A, ftr:[+--+-?---], np:12, ch:0, co:0)    !
    !_____!___________________________________________________!
    
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
    >>> 

Create Info Docs
----------------

::

    $ cd src && python
    >>> from pronouns2 import *
    >>> doc(info=True)
    '.../docs/Demo.tex'
    >>> doc(file_type=FileType.TXT, info=True)
    '.../docs/Demo.txt'
    >>> quit()
    $ cd ../docs
    $ make Demo.pdf
    ...
    $ open Demo.pdf
    ...
    $ open Demo.txt

This Demo.pdf should look like the originally checked in
Demo.pdf, except for the creation date.

Run Info+Detail Demo
--------------------

::

    $ cd src && python
    >>> from pronouns2 import *
    >>> demo("10.1", info=True, debug=True)
    ...

Create Info+Detail Docs
-----------------------

::

    $ cd src && python
    >>> from pronouns2 import *
    >>> doc(info=True, debug=True)
    '.../docs/Demo.tex'
    >>> doc(file_type=FileType.TXT, info=True, debug=True)
    '.../docs/Demo.txt'
    >>> quit()
    $ cd ../docs
    $ make Demo.pdf
    ...
    $ open Demo.pdf
    ...
    $ open Demo.txt


Adds intermediate tables and diagrams to the preceding Info Docs.

Run Info+Detail+Trace Demo
--------------------------

::

    $ cd src && python
    >>> from pronouns2 import *
    >>> demo("10.1", info=True, debug=True, trace=True)
    ...

Create Info+Detail+Trace Docs
-----------------------------

::

    $ cd src && python
    >>> from pronouns2 import *
    >>> doc(info=True, debug=True, trace=True)
    '.../docs/Demo.tex'
    >>> doc(file_type=FileType.TXT, info=True, debug=True, trace=True)
    '.../docs/Demo.txt'
    >>> quit()
    $ cd ../docs
    $ make Demo.pdf
    ...
    $ open Demo.pdf
    ...
    $ open Demo.txt


Adds intermediate tables and diagrams to the preceding Info Docs.

Create Docs for Single Example
------------------------------

::

    $ cd src && python
    >>> from pronouns2 import *
    >>> doc("10.1", info=True)
    '.../docs/Demo.tex'
    >>> doc("10.1", file_type=FileType.TXT, info=True)
    '.../docs/Demo.txt'
    >>> quit()
    $ cd ../docs
    $ make Demo.pdf
    ...
    $ open Demo.pdf
    ...
    $ open Demo.txt

Only Demo Chaining Tables
--------------------------

::

    $ cd src && python
    >>> from pronouns2 import *
    >>> chaining_tables = {'file_type': FileType.TXT,
                           'info': True,
                           'features_table': False,
                           'abstract_diagram': False,
                           'nodes_after_chaining': False,
                           'nodes_table': False,
                           'chaining_diagram': False,
                           'chaining_table': True,
                           'interpretations_table': False,
                           'summary_table': False,
                           'lexicon_table': False}
    >>> demo("10.1", **chaining_tables)
    >>> demo(**chaining_tables)
    ...

Only Doc Chaining Diagrams
--------------------------

::

    $ cd src && python
    >>> from pronouns2 import *
    >>> chaining_diagrams = {'file_type': FileType.TEX,
                             'info': True,
                             'features_table': False,
                             'abstract_diagram': False,
                             'nodes_after_chaining': False,
                             'nodes_table': False,
                             'chaining_diagram': True,
                             'chaining_table': False,
                             'interpretations_table': False,
                             'summary_table': False,
                             'lexicon_table': False}
    >>> doc("10.1", file="../docs/Demo_10p1.tex", **chaining_diagrams
    '.../docs/Demo_10p1.tex'
    >>> doc(**chaining_diagrams)
    '.../docs/Demo.tex'
    >>> quit()
    $ cd ../docs
    $ make Demo_10p1.pdf
    ...
    $ make Demo.pdf
    ...
    $ open Demo_10p1.pdf
    ...
    $ open Demo.pdf

Run Coverage Test
-----------------

::

    $ make coverage
    ...
    coverage run -m unittest discover -s tests -p "test_*.py"
    ...
    ----------------------------------------------------------------------
    Ran 140 tests in 14.261s
    
    OK
    coverage html
    Wrote HTML report to htmlcov/index.html
    ...
    $ open src/htmlcov/index.html

Make command ``make coverage`` is also available when connected
to either the repo's root directory (``.``) or tests subdirectory
(``src/tests``).  You will need to adjust ``open src/htmlcov/index.html``
in those two cases.

Create PDFs in Test Output Directory
------------------------------------

::

    $ cd src/tests && make coverage
    ...
    $ make output-pdfs
    ...
    $ cd output && ls -1 *.pdf
    test_abstract_diagram.pdf
    ...
    test_doc.pdf
    ...
    test_varying_rho.pdf
    $ open test_doc.pdf
    $ open test_varying_rho.pdf

Rebuild the HTML Documentation
------------------------------

If you aren't comfortable with Sphinx and RST, or you are
worried you might lose anything precious in your copy of the
repo, you can skip this section.  However, I think it is
important to mention how I rebuild the HTML documentation to
the unafraid.

::

    $ cd src/docs && make all


Jupyter Notebook
----------------

Jupyter notebook ``spread.ipynb`` is a freebie which isn't
essential to running the Pronouns2 Python code. However, it can
provide insight into how our Spreading Algorithm
(`spread.py <../../../../src/spread.py>`_)
helps to draw Pronouns2's pretty TikZ chaining diagrams.

- Connect to ``src`` directory in Terminal.app
- Execute ``jupyter notebook``
- In Jupyter notebook, running in your web browser, double-click
  ``spread.ipynb`` in the **Files** tab.
- Press **Restart the kernel and run all the cells** button

  .. image:: ./run_all_cells.png
     :align: center
     :alt: Restart the kernel and run all the cells button

  in opened ``spread.ipynb`` Jupyter notebook.
- The ``spread.ipynb`` Jupyter notebook imports ``pronouns2``:

  .. image:: ./notebook_imports.png
     :align: center
     :alt: Jupyter notebook imports

  and runs Python code in all the Jupyter notebook cells,
  creating many plots like:

  .. image:: ./plot_0p50.png
     :align: center
     :alt: Example plot generated by spread.ipynb Python code

  demonstrating the Spreading Algorithm. Our document
  `VaryingRho.pdf <../../../../docs/VaryingRho.pdf>`_
  goes into greater
  detail about how this algorithm is used to tune the placement
  of arrowheads in Pronouns2's TikZ chaining diagrams.

lexicon.py Exercises
--------------------

::

    $ python
    >>> from pronouns2 import *
    >>> node = lexicon_lookup("Algernon")
    >>> node
    <globals.Node object at 0x1094f3a90>
    >>> txt_nodes([node])
    _________________________NODES_________________________
    !    !                                                !
    ! 1  ! (N, lit:Algernon, ftr:[---+--+--], up:0, dn:0, !
    !    !  lt:0, rt:0, th:0, np:1, ch:0, co:0, ec:0,     !
    !    !  pr:0, su:0, nu:1)                             !
    !____!________________________________________________!
    >>> node.ftr_str
    '---+--+--'
    >>> lexicon_select(node.ftr_str)
    ['Algernon', 'Bernie', 'Bill', 'Bob', 'Ernie', 'Fred', 'Harry',
    'Jack', 'John', 'Oscar', 'Peter', 'asshole', 'blame', 'boy',
    'brother', 'camel', 'cat', 'dad', 'embezzler', 'father', 'fish',
    'gambler', 'grandfather', 'man', 'mosquito', 'neighbor', 'pig',
    'pilot', 'sheep', 'son', 'student', 'toy', 'uncle']
    >>> lexicon_select(lexicon_lookup("supper").ftr_str)
    ['Las Vegas', 'Mig', 'blame', 'candy', 'complaining', 'flower',
    'hat', 'home', 'house', 'interest', 'lawn', 'pen',
    'possibility', 'present', 'problem', 'smokescreen', 'solution',
    'supper', 'tax', 'toy', 'trouble']
    >>> lexicon_select('mom')
    ['Anna', 'Janet', 'Jill', 'June', 'Linda', 'Mary', 'Penelope',
    'Sandy', 'Sue', 'asshole', 'aunt', 'blame', 'camel', 'cat',
    'daughter', 'embezzler', 'fish', 'gambler', 'girl',
    'grandmother', 'mosquito', 'mom', 'mother', 'neighbor', 'pig',
    'pilot', 'sheep', 'sister', 'student', 'toy']
    >>> 

(10.1) Walkthrough
------------------

::

    $ python
    >>> from pronouns2 import *
    >>> ex = example("10.1")
    >>> ex
    ["John wants to give June a present, but he isn't sure she’ll
        like it.", ['C', ['S', 'John', ['S', 'PHI', 'June', 'present']],
        ['S', 'he', ['S', 'she', 'it']]]]
    >>> sentence, csn = ex
    >>> sentence
    "John wants to give June a present, but he isn't sure she’ll like it."
    >>> csn
    ['C', ['S', 'John', ['S', 'PHI', 'June', 'present']], ['S',
        'he', ['S', 'she', 'it']]]
    >>> Node.set_tree(parse(csn))
    >>> nodes = tree_nodes(Node.tree())
    >>> nodes
    [<globals.Node object at 0x10f824250>, <globals.Node object at
        0x10f93e940>, <globals.Node object at 0x10f93ea30>,
        <globals.Node object at 0x10f93e910>, <globals.Node object at
        0x10f93eac0>, <globals.Node object at 0x10f93efa0>,
        <globals.Node object at 0x10f93ea60>, <globals.Node object at
        0x10f93ed30>, <globals.Node object at 0x10f7a6a90>,
        <globals.Node object at 0x10f7a6a60>, <globals.Node object at
        0x110aaa6d0>, <globals.Node object at 0x110aaa100>]
    >>> txt_nodes(nodes)
    _________________________NODES_________________________
    !     !                                               !
    !  1  ! (C, up:0, dn:2, lt:0, rt:0, th:2, nu:1)       !
    !  2  ! (S, up:1, dn:3, lt:0, rt:8, th:3, nu:2)       !
    !  3  ! (N, lit:John, ftr:[---+--+--], up:2, dn:0,    !
    !     !  lt:0, rt:4, th:4, np:3, ch:0, co:0, ec:0,    !
    !     !  pr:0, su:0, nu:3)                            !
    !  4  ! (S, up:2, dn:5, lt:3, rt:0, th:5, nu:4)       !
    !  5  ! (N, lit:PHI, ftr:[+??????--], up:4, dn:0,     !
    !     !  lt:0, rt:6, th:6, np:5, ch:0, co:0, ec:0,    !
    !     !  pr:0, su:0, nu:5)                            !
    !  6  ! (N, lit:June, ftr:[---+-++--], up:4, dn:0,    !
    !     !  lt:5, rt:7, th:7, np:6, ch:0, co:0, ec:0,    !
    !     !  pr:0, su:0, nu:6)                            !
    !  7  ! (N, lit:present, ftr:[---+-?---], up:4, dn:0, !
    !     !  lt:6, rt:0, th:8, np:7, ch:0, co:0, ec:0,    !
    !     !  pr:0, su:0, nu:7)                            !
    !  8  ! (S, up:1, dn:9, lt:2, rt:0, th:9, nu:8)       !
    !  9  ! (N, lit:he, ftr:[+--+--+--], up:8, dn:0,      !
    !     !  lt:0, rt:10, th:10, np:9, ch:0, co:0, ec:0,  !
    !     !  pr:0, su:0, nu:9)                            !
    ! 10  ! (S, up:8, dn:11, lt:9, rt:0, th:11, nu:10)    !
    ! 11  ! (N, lit:she, ftr:[+--+-++--], up:10, dn:0,    !
    !     !  lt:0, rt:12, th:12, np:11, ch:0, co:0, ec:0, !
    !     !  pr:0, su:0, nu:11)                           !
    ! 12  ! (N, lit:it, ftr:[+--+-?---], up:10, dn:0,     !
    !     !  lt:11, rt:0, th:0, np:12, ch:0, co:0, ec:0,  !
    !     !  pr:0, su:0, nu:12)                           !
    !_____!_______________________________________________!
    >>> nnodes = tree_n_nodes(Node.tree())
    >>> txt_nodes(nnodes)
    _________________________NODES_________________________
    !     !                                               !
    !  3  ! (N, lit:John, ftr:[---+--+--], up:2, dn:0,    !
    !     !  lt:0, rt:4, th:4, np:3, ch:0, co:0, ec:0,    !
    !     !  pr:0, su:0, nu:3)                            !
    !  5  ! (N, lit:PHI, ftr:[+??????--], up:4, dn:0,     !
    !     !  lt:0, rt:6, th:6, np:5, ch:0, co:0, ec:0,    !
    !     !  pr:0, su:0, nu:5)                            !
    !  6  ! (N, lit:June, ftr:[---+-++--], up:4, dn:0,    !
    !     !  lt:5, rt:7, th:7, np:6, ch:0, co:0, ec:0,    !
    !     !  pr:0, su:0, nu:6)                            !
    !  7  ! (N, lit:present, ftr:[---+-?---], up:4, dn:0, !
    !     !  lt:6, rt:0, th:8, np:7, ch:0, co:0, ec:0,    !
    !     !  pr:0, su:0, nu:7)                            !
    !  9  ! (N, lit:he, ftr:[+--+--+--], up:8, dn:0,      !
    !     !  lt:0, rt:10, th:10, np:9, ch:0, co:0, ec:0,  !
    !     !  pr:0, su:0, nu:9)                            !
    ! 11  ! (N, lit:she, ftr:[+--+-++--], up:10, dn:0,    !
    !     !  lt:0, rt:12, th:12, np:11, ch:0, co:0, ec:0, !
    !     !  pr:0, su:0, nu:11)                           !
    ! 12  ! (N, lit:it, ftr:[+--+-?---], up:10, dn:0,     !
    !     !  lt:11, rt:0, th:0, np:12, ch:0, co:0, ec:0,  !
    !     !  pr:0, su:0, nu:12)                           !
    !_____!_______________________________________________!
    >>> txt_features(nnodes)
    _____________________________FEATURES____________________________
    !         !     !     !     !     !     !     !     !     !     !
    !         ! PNF ! FPF ! SPF ! TPF ! PLF ! GNF ! ANF ! RPF ! GEN !
    !    John !  -  !  -  !  -  !  +  !  -  !  -  !  +  !  -  !  -  !
    !     PHI !  +  !  ?  !  ?  !  ?  !  ?  !  ?  !  ?  !  -  !  -  !
    !    June !  -  !  -  !  -  !  +  !  -  !  +  !  +  !  -  !  -  !
    ! present !  -  !  -  !  -  !  +  !  -  !  ?  !  -  !  -  !  -  !
    !      he !  +  !  -  !  -  !  +  !  -  !  -  !  +  !  -  !  -  !
    !     she !  +  !  -  !  -  !  +  !  -  !  +  !  +  !  -  !  -  !
    !      it !  +  !  -  !  -  !  +  !  -  !  ?  !  -  !  -  !  -  !
    !_________!_____!_____!_____!_____!_____!_____!_____!_____!_____!
    >>> chaining(nnodes)
    >>> nodes = tree_nodes(Node.tree())
    >>> txt_nodes(nodes)
    ___________________________NODES___________________________
    !     !                                                   !
    !  1  ! (C, up:0, dn:2, lt:0, rt:0, th:2, nu:1)           !
    !  2  ! (S, up:1, dn:3, lt:0, rt:8, th:3, nu:2)           !
    !  3  ! (N, lit:John, ftr:[---+--+--], up:2, dn:0,        !
    !     !  lt:0, rt:4, th:4, np:3, ch:0, co:3A, ec:3D,      !
    !     !  pr:0, su:5, nu:3)                                !
    !  3A ! (E, sub:A, ftr:[---+--+--], np:3, ch:0, co:3B)    !
    !  3B ! (E, sub:B, ftr:[---+--+--], np:3, ch:9A, co:3C)   !
    !  3C ! (E, sub:C, ftr:[---+--+--], np:3, ch:5A, co:3D)   !
    !  3D ! (E, sub:D, ftr:[---+--+--], np:3, ch:5D, co:0)    !
    !  4  ! (S, up:2, dn:5, lt:3, rt:0, th:5, nu:4)           !
    !  5  ! (N, lit:PHI, ftr:[+??????--], up:4, dn:0,         !
    !     !  lt:0, rt:6, th:6, np:5, ch:0, co:5A, ec:5D,      !
    !     !  pr:3, su:6, nu:5)                                !
    !  5A ! (E, sub:A, ftr:[+??????--], np:5, ch:0, co:5B)    !
    !  5B ! (E, sub:B, ftr:[+--+-?---], np:5, ch:12A, co:5C)  !
    !  5C ! (E, sub:C, ftr:[+--+-++--], np:5, ch:11A, co:5D)  !
    !  5D ! (E, sub:D, ftr:[+--+--+--], np:5, ch:9A, co:0)    !
    !  6  ! (N, lit:June, ftr:[---+-++--], up:4, dn:0,        !
    !     !  lt:5, rt:7, th:7, np:6, ch:0, co:6A, ec:6B,      !
    !     !  pr:5, su:7, nu:6)                                !
    !  6A ! (E, sub:A, ftr:[---+-++--], np:6, ch:0, co:6B)    !
    !  6B ! (E, sub:B, ftr:[---+-++--], np:6, ch:11A, co:0)   !
    !  7  ! (N, lit:present, ftr:[---+-?---], up:4, dn:0,     !
    !     !  lt:6, rt:0, th:8, np:7, ch:0, co:7A, ec:7B,      !
    !     !  pr:6, su:9, nu:7)                                !
    !  7A ! (E, sub:A, ftr:[---+-?---], np:7, ch:0, co:7B)    !
    !  7B ! (E, sub:B, ftr:[---+-?---], np:7, ch:12A, co:0)   !
    !  8  ! (S, up:1, dn:9, lt:2, rt:0, th:9, nu:8)           !
    !  9  ! (N, lit:he, ftr:[+--+--+--], up:8, dn:0,          !
    !     !  lt:0, rt:10, th:10, np:9, ch:0, co:9A, ec:9A,    !
    !     !  pr:7, su:11, nu:9)                               !
    !  9A ! (E, sub:A, ftr:[+--+--+--], np:9, ch:0, co:0)     !
    ! 10  ! (S, up:8, dn:11, lt:9, rt:0, th:11, nu:10)        !
    ! 11  ! (N, lit:she, ftr:[+--+-++--], up:10, dn:0,        !
    !     !  lt:0, rt:12, th:12, np:11, ch:0, co:11A, ec:11A, !
    !     !  pr:9, su:12, nu:11)                              !
    ! 11A ! (E, sub:A, ftr:[+--+-++--], np:11, ch:0, co:0)    !
    ! 12  ! (N, lit:it, ftr:[+--+-?---], up:10, dn:0,         !
    !     !  lt:11, rt:0, th:0, np:12, ch:0, co:12A, ec:12A,  !
    !     !  pr:11, su:0, nu:12)                              !
    ! 12A ! (E, sub:A, ftr:[+--+-?---], np:12, ch:0, co:0)    !
    !_____!___________________________________________________!
    >>> txt_chaining(nnodes)
    _________________________________CHAINING________________________________
    !            !           !            !              !     !      !     !
    ! John       ! PHI       ! June       ! present      ! he  ! she  ! it  !
    ! JohnA      ! PHIA      ! JuneA      ! presentA     ! heA ! sheA ! itA !
    ! JohnB^heA  ! PHIB^itA  ! JuneB^sheA ! presentB^itA !     !      !     !
    ! JohnC^PHIA ! PHIC^sheA !            !              !     !      !     !
    ! JohnD^PHID ! PHID^heA  !            !              !     !      !     !
    !____________!___________!____________!______________!_____!______!_____!
    >>> interps = interpret(nnodes)
    >>> interps
    [[[<globals.Node object at 0x110aaa9d0>, <globals.Node object at
        0x110aaa9a0>, <globals.Node object at 0x110aaa970>],
        [<globals.Node object at 0x110aaa910>, <globals.Node object at
        0x110aaa850>], [<globals.Node object at 0x110aaa880>,
        <globals.Node object at 0x110aaa7f0>]]]
    >>> view_interps(interps)
    [['JohnD^PHID^heA', 'JuneB^sheA', 'presentB^itA']]
    >>> view_interpretations(interps)
    [['JohnD^PHID^heA    JuneB^sheA    presentB^itA']]
    >>> txt_interpretations(interps)
    ________________INTERPRETATIONS_________________
    !                                              !
    ! JohnD^PHID^heA    JuneB^sheA    presentB^itA !
    !______________________________________________!
    >>> 

Locate and View PDF Documentation
---------------------------------

::

    $ cd docs
    $ ls -1 *.pdf
    Demo.pdf
    Demo_10p1.pdf
    Pronouns2Modula2.pdf
    Pronouns2Python.pdf
    RelatedLiterature.pdf
    VaryingRho.pdf
    $ open Pronouns2Python.pdf
    $ 

Locate and View HTML Documentation
----------------------------------

::

    $ open src/docs/build/html/index.htm
    $ # OR
    $ cd src/docs/build/html
    $ ls -1 *.htm
    abstract.htm
    chaining.htm
    demo.htm
    ...
    usage.htm
    varying_rho.htm
    view.htm
    $ open index.htm

You might want to create an alias on your desktop or add the
opened URL to your web browser's favorites if you intend to
visit the HTML documentation often.  I can help you get started
with that.  Click the following link: :ref:`Pronouns2`.

