Make Targets
============

Command ``make`` automates the building of target files by reading
instructions from ``Makefile``\s.

Root Directory
--------------

The top directory of the Pronouns2 project repo.

The following make targets are available:

Root Directory Commands
^^^^^^^^^^^^^^^^^^^^^^^

- ``make help``              - Print this help
- ``make install``           - Install Python dependencies
- ``make update``            - Update Python dependencies
- ``make view``              - Build everything; view test coverage, HTML doc, and Demo.pdf

Build Commands Broadcast to Subdirectories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``make all``               - Build everything (documentation and run tests)
- ``make demos``             - Generate Demo.min, Demo.txt, and Demo.tex
- ``make test``              - Run Python unit tests
- ``make coverage``          - Run tests with coverage report
- ``make html``              - Build HTML documentation
- ``make xxx.pdf``           - Generate specific PDF in docs directory
- ``make clean``             - Clean intermediate files in all subdirectories
- ``make distclean``         - Remove all non-shipping generated files
- ``make maintainer-clean``  - Remove all generated files for a pristine state

docs Directory
--------------

The ``docs`` directory contains LaTeX and related LaTeX support
files for the Pronouns2 project.

The following make targets are available:

- ``make help``              - Print this help
- ``make view``              - Build everything; view Demo.pdf
- ``make all``               - Process all LaTeX files in directory (except Pronouns2Macros.tex)
- ``make xxx``               - Process specific file (e.g., 'make Pronouns2Python')
- ``make xxx.pdf``           - Same as above, will process xxx.tex
- ``make clean``             - Remove intermediate LaTeX files
- ``make distclean``         - Remove all generated files except shipping PDFs
- ``make maintainer-clean``  - Remove all generated files, including shipping PDFs

src Directory
-------------

The ``src`` directory contains the Python source code and tests
for the project.

The following make targets are available:

- ``make help``              - Print this help
- ``make all``               - Run tests and generate analysis files
- ``make view``              - Build everything; view test coverage
- ``make demos``             - Generate ``../docs/Demo.txt`` and ``../docs/Demo.tex``
- ``make demo-txt``          - Generate ``../docs/Demo.txt``
- ``make demo-tex``          - Generate ``../docs/Demo.tex``
- ``make test``              - Run unit tests
- ``make coverage``          - Run tests with coverage and generate ``htmlcov/index.html``
- ``make clean``             - Remove intermediate files
- ``make distclean``         - Remove all non-distributed files
- ``make maintainer-clean``  - Remove all generated files for a pristine state

src/docs Directory
------------------

The following make targets are available:

- ``make help``              - Print this help
- ``make view``              - Build everything; view HTML doc
- ``make all``               - Clean everything and rebuild HTML documentation
- ``make apidoc``            - Generate API documentation
- ``make linkcheck``         - Check external links for integrity
- ``make html``              - Generate HTML documentation
- ``make clean``             - Remove intermediate build files
- ``make distclean``         - Remove non-shipping files, including the build directory
- ``make maintainer-clean``  - Remove all generated files, including shipped HTML files

src/tests Directory
-------------------

The following make targets are available:

- ``make help``              - Print this help
- ``make all``               - Make coverage and output-pdfs targets
- ``make view``              - Make all. View HTML coverage report
- ``make test``              - Run Python unit tests
- ``make coverage``          - Run tests and generate HTML coverage report
- ``make expected-pdfs``     - Process all LaTeX files in ./expected
- ``make output-pdfs``       - Process all LaTeX files in ./output
- ``make clean``             - Remove intermediate LaTeX files
- ``make distclean``         - Remove all generated files
- ``make maintainer-clean``  - Remove all generated files

src/tests/output Directory
--------------------------

The following make targets are available:

- ``make help``              - Print this help
- ``make all``               - Process all LaTeX files in directory
- ``make xxx``               - Process specific file
- ``make xxx.pdf``           - Same as above, will process xxx.tex
- ``make clean``             - Remove intermediate LaTeX files
- ``make distclean``         - Remove all generated files
- ``make maintainer-clean``  - Remove all generated files

src/tests/expected Directory
----------------------------

Exactly like ``src/tests/output``.
