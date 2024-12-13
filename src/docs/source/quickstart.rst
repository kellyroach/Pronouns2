Quick Start
===========

In most quick start examples, run ``python`` in the ``src``
subdirectory, so that ``python`` will find ``pronouns2.py``,
which ``from pronouns2 import *`` needs.  If you are already
in the ``src`` subdirectory, use ``python`` instead of
``cd src && python``.

Windows users should use ``start`` instead of ``open``.

.. code-block:: bash

    # As a module in Python REPL
    $ cd src && python
    >>> from pronouns2 import *
    >>> demo("10.1")                    # Run specific demo
    >>> demo()                          # Run all demos
    >>> doc(file_type=FileType.TXT)     # Generate docs/Demo.txt
    >>> doc(file_type=FileType.TEX)     # Generate docs/Demo.tex
    >>> example("10.1")                 # See example (10.1)

    # As a command-line tool
    $ cd src && python pronouns2.py --info     # Analyze all examples
    Created: .../docs/Demo.tex
    $ cd src && python pronouns2.py --file_type=.txt --info     # TXT version
    Created: .../docs/Demo.txt
    $ cd src && python pronouns2.py "10.1" --file=../docs/Demo_10p1 --info     # Example (10.1)
    Created: .../docs/Demo_10p1.tex
    $ cd src && python pronouns2.py --file=../docs/Demo_debug --info --debug     # More detail
    Created: .../docs/Demo.tex
    $ cd src && python pronouns2.py "10.1" --file=../docs/Demo_10p1_debug --info --debug
    Created: .../docs/Demo_10p1.tex
    $ cd src && python pronouns2.py --file=../docs/Demo_trace --info --debug --trace
    Created: .../docs/Demo_trace.tex
    $ cd src && python pronouns2.py "10.1" --file=../docs/Demo_10p1_trace --info --debug --trace
    Created: .../docs/Demo_10p1_trace.tex
    $ cd docs && make all && make clean     # Create new/updated PDFs in docs directory
    ...

    # Print root directory's make's help
    $ make help
    # Build everything (documentation and run tests)
    $ make all
    # Build everything, view test coverage, HTML doc, and Demo.pdf
    $ make view
    # Read Kelly Roach's "Pronouns, Second Edition (Python Version)"
    $ open docs/Pronouns2Python.pdf
    # Read HTML documentation
    $ open src/docs/build/html/index.htm

    # Run unit tests
    $ cd src && make coverage; open htmlcov/index.html
    # OR
    $ cd src/tests; make coverage
    # OR also with PDFs created in src/tests/output
    $ cd src/tests; make coverage; make output-pdfs

    # Remove files most humans don't want to see
    $ make clean

See :ref:`Usage` for further examples.
