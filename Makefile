# Root directory Makefile

PYTHON = python
PIP = pip

# Subdirectories with makefiles
DOCS_DIR = docs
SRC_DIR = src
SPHINX_DIR = src/docs
TESTS_DIR = src/tests

# Platform-specific commands
ifeq ($(OS),Windows_NT)
    CD = cd /d
    RETURN = cd ..
    CHECKFILE = if exist
else
    CD = pushd
    RETURN = popd
    CHECKFILE = test -f
endif

.PHONY: all clean distclean maintainer-clean help install update test coverage html demos

help:
	@echo "Root directory make targets:"
	@echo "  help              - Print this help"
	@echo "  install           - Install Python dependencies"
	@echo "  update           - Update Python dependencies"
	@echo "  view             - Build everything; view test coverage, HTML doc, and Demo.pdf"
	@echo "  all              - Build everything (documentation and run tests)"
	@echo "  demos            - Generate Demo.txt and Demo.tex"
	@echo "  test             - Run Python unit tests"
	@echo "  coverage         - Run tests with coverage report"
	@echo "  html             - Build HTML documentation"
	@echo "  xxx.pdf          - Generate specific PDF in docs directory"
	@echo "  clean            - Clean intermediate files in all subdirectories"
	@echo "  distclean        - Remove all non-shipping generated files"
	@echo "  maintainer-clean - Remove all generated files for a pristine state"
	@echo
	@echo "Note: Basic functionality (install, test, coverage) works on all platforms."
	@echo "Some advanced features may be limited on Windows."
	@echo
	@echo "See individual subdirectory README.md files for more detailed commands"

# Python package management
install:
	$(PIP) install -r requirements.txt

update:
	$(PIP) install --upgrade -r requirements.txt

# Build and view everything
view:
	@echo "Building and view everything..."
	@$(CD) "$(SRC_DIR)" && $(MAKE) view && $(RETURN)
	@$(CD) "$(SPHINX_DIR)" && $(MAKE) view && $(RETURN)
	@$(CD) "$(DOCS_DIR)" && $(MAKE) view && $(RETURN)

# Main build target
all:
	@echo "Building everything..."
	@$(CD) "$(SRC_DIR)" && $(MAKE) all && $(RETURN)
	@$(CD) "$(SPHINX_DIR)" && $(MAKE) all && $(RETURN)
	@$(CD) "$(DOCS_DIR)" && $(MAKE) all && $(RETURN)

# Source directory specific targets
test:
	@$(CD) "$(SRC_DIR)" && $(MAKE) test && $(RETURN)

coverage:
	@$(CD) "$(SRC_DIR)" && $(MAKE) coverage && $(RETURN)

demos:
	@$(CD) "$(SRC_DIR)" && $(MAKE) demos && $(RETURN)

# Sphinx documentation specific targets
html:
	@$(CD) "$(SPHINX_DIR)" && $(MAKE) html && $(RETURN)

# LaTeX documentation specific targets
%.pdf:
ifeq ($(OS),Windows_NT)
	@$(CHECKFILE) "$(DOCS_DIR)\$*.tex" ( \
		$(CD) "$(DOCS_DIR)" && $(MAKE) $@ && $(RETURN) \
	) else ( \
		echo "Unable to process $*.pdf: $(DOCS_DIR)\$*.tex not found" \
	)
else
	@if [ -f "$(DOCS_DIR)/$*.tex" ]; then \
		$(CD) "$(DOCS_DIR)" && $(MAKE) $@ && $(RETURN); \
	else \
		echo "Unable to process $*.pdf: $(DOCS_DIR)/$*.tex not found"; \
	fi
endif

# Clean intermediate files
clean:
	@echo "Cleaning intermediate files in subdirectories..."
	@$(CD) "$(SRC_DIR)" && $(MAKE) clean && $(RETURN)
	@$(CD) "$(DOCS_DIR)" && $(MAKE) clean && $(RETURN)
	@$(CD) "$(TESTS_DIR)" && $(MAKE) clean && $(RETURN)

# Remove all non-shipping generated files
distclean:
	@echo "Performing distclean in all subdirectories..."
	@$(CD) "$(SRC_DIR)" && $(MAKE) distclean && $(RETURN)
	@$(CD) "$(SPHINX_DIR)" && $(MAKE) distclean && $(RETURN)
	@$(CD) "$(DOCS_DIR)" && $(MAKE) distclean && $(RETURN)
	@$(CD) "$(TESTS_DIR)" && $(MAKE) distclean && $(RETURN)

# Remove all generated files for a pristine state
maintainer-clean:
	@echo "Performing maintainer-clean in all subdirectories..."
	@$(CD) "$(SRC_DIR)" && $(MAKE) maintainer-clean && $(RETURN)
	@$(CD) "$(SPHINX_DIR)" && $(MAKE) maintainer-clean && $(RETURN)
	@$(CD) "$(DOCS_DIR)" && $(MAKE) maintainer-clean && $(RETURN)
	@$(CD) "$(TESTS_DIR)" && $(MAKE) maintainer-clean && $(RETURN)
