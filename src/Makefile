# Makefile for src directory

PYTHON = python
COVERAGE = coverage
UNITTEST = unittest
DOCS_DIR = ../docs

# Platform-specific commands
ifeq ($(OS),Windows_NT)
    RM = del /Q
    RMDIR = rmdir /s /q
    OPEN = start
else
    RM = rm -f
    RMDIR = rm -rf
    OPEN = open
endif

.PHONY: all test coverage clean demo-txt demo-tex demos help distclean maintainer-clean

help:
	@echo "Available targets:"
	@echo "  help              - Print this help"
	@echo "  all               - Run tests and generate analysis files"
	@echo "  view              - Make all. View test coverage"
	@echo "  demos             - Generate Demo.txt and Demo.tex"
	@echo "  demo-txt          - Generate Demo.txt"
	@echo "  demo-tex          - Generate Demo.tex"
	@echo "  test              - Run unit tests"
	@echo "  coverage          - Run tests with coverage and generate HTML report"
	@echo "  clean             - Remove intermediate files"
	@echo "  distclean         - Remove all non-distributed files"
	@echo "  maintainer-clean  - Remove all generated files for a pristine state"

# Build everything; view test coverage
view: all
	$(OPEN) htmlcov/index.html

# Main target - run everything
all: coverage demos

# Generate all documentation files
demos: demo-txt demo-tex

# Generate Demo.txt
demo-txt:
	$(PYTHON) pronouns2.py --file_type=.txt --info

# Generate Demo.tex
demo-tex:
	$(PYTHON) pronouns2.py --file_type=.tex --info

# Run unit tests
test:
	$(PYTHON) -m $(UNITTEST) discover -s tests -p "test_*.py"

# Run coverage analysis
coverage:
	$(COVERAGE) run -m $(UNITTEST) discover -s tests -p "test_*.py"
	$(COVERAGE) html

# Clean intermediate files
clean:
	# No steps required for clean in src

# Clean all non-distributed files
distclean: demos clean
	$(RMDIR) htmlcov
	$(RM) .coverage
	$(RMDIR) __pycache__

# Clean everything for a pristine state
maintainer-clean: distclean
	# No additional steps required for maintainer-clean in src

