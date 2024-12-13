# src/tests Directory

The src/tests directory contains the unit tests for the project.

## Directory Structure

- `__init__.py` - Initialize tests as a package
- `Makefile` - Used by `make` (see Make Commands below)
- `README.md` - This document
- `*.py` - Unit tests
- `expected/` - Expected *.txt, *.tex, and *.pdf files
- `output/` - Output *.txt, *.tex, and *.pdf files (`make test` or `make coverage`)
- `utils/` - Test utilities

## Make Commands

The following make targets are available:

- `make help`              - Print this help
- `make all`               - Make coverage and output-pdfs targets
- `make view`              - Make all. View HTML coverage report
- `make test`              - Run Python unit tests
- `make coverage`          - Run tests and generate HTML coverage report
- `make expected-pdfs`     - Process all LaTeX files in ./expected
- `make output-pdfs`       - Process all LaTeX files in ./output
- `make clean`             - Remove intermediate LaTeX files
- `make distclean`         - Remove all generated files
- `make maintainer-clean`  - Remove all generated files

## Coverage Testing

To run tests and view the HTML coverage report:
```bash
make view
```

To simply view the HTML coverage report:
```bash
open ../htmlcov/index.html
```

## Making Unit Test PDFs

To make PDFs in the src/tests/expected directory:
```bash
make expected-pdfs
```

To make PDFs in the src/tests/output directory:
```bash
make output-pdfs
```
after you've created required LaTeX inputs via `make test`
or `make coverage`

The `make all` command effectively runs `make coverage`
followed by `make output-pdfs`.  The `make all` command
doesn't `make expected-pdfs`.  If you want PDFs in the
src/tests/expected directory, use `make expected-pdfs`.

## src/tests/expected Directory Maintenance

If we could be certain that our QA team would approve (without
manually inspecting) the entire content of ./output after
"make all", then we would allow replacing ./expected by a copy
of ./output which is followed by a "make distclean" in
./expected .  Instead, the process is to "make distclean"
followed by a phone call to the QA Team who will take it from
there.

## src/tests/output README.md and Makefile

The src/tests/output README.md and Makefile are identical to
the src/tests/expected README.md and Makefile by design.
Even though they do say "expected" in their text and source
code, these duplicate files are applicable to and can be used
in the "output" directory.
