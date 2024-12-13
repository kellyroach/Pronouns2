# Makefile for src/tests directory

# Platform-specific commands
ifeq ($(OS),Windows_NT)
    CD = cd /d
    RETURN = cd ..
    RMDIR = rmdir /s /q
    OPEN = start
else
    CD = pushd
    RETURN = popd
    RMDIR = rm -rf
    OPEN = open
endif

.PHONY: all help clean distclean maintainer-clean

# Parent directory src with makefile
SRC_DIR = ..

# Subdirectories with makefiles
EXPECTED_DIR = expected
OUTPUT_DIR = output

help:
	@echo "Available targets:"
	@echo "  help              - Print this help"
	@echo "  all               - Make coverage and output-pdfs targets"
	@echo "  view              - Make all. View HTML coverage report"
	@echo "  test              - Run Python unit tests"
	@echo "  coverage          - Run tests and generate HTML coverage report"
	@echo "  expected-pdfs     - Process all LaTeX files in ./expected"
	@echo "  output-pdfs       - Process all LaTeX files in ./output"
	@echo "  clean             - Remove intermediate LaTeX files"
	@echo "  distclean         - Remove all generated files"
	@echo "  maintainer-clean  - Remove all generated files"

# Build everything; view test coverage
view: all
	$(OPEN) "$(SRC_DIR)/htmlcov/index.html"

# Main target to process all files
all: coverage output-pdfs
	@echo "Make coverage and ./output pdfs targets"

# Process all LaTeX files in ./expected
expected-pdfs:
	@$(CD) "$(EXPECTED_DIR)" && $(MAKE) all && $(RETURN)

# Process all LaTeX files in ./output
output-pdfs:
	@$(CD) "$(OUTPUT_DIR)" && $(MAKE) all && $(RETURN)

# Source directory specific targets
test:
	@$(CD) "$(SRC_DIR)" && $(MAKE) test && $(RETURN)

coverage:
	@$(CD) "$(SRC_DIR)" && $(MAKE) coverage && $(RETURN)

# Clean intermediate pdflatex generated files
clean:
	@echo "Cleaning intermediate files in all subdirectories..."
	@$(CD) "$(EXPECTED_DIR)" && $(MAKE) clean && $(RETURN)
	@$(CD) "$(OUTPUT_DIR)" && $(MAKE) clean && $(RETURN)

# Clean and ready for distribution
distclean: clean
        # Remove all files from ./expected except Makefile, *.txt, *.tex
        # Remove all files from ./output except Makefile
	@echo "Removing __pycache__ directories..."
	@$(RMDIR) __pycache__
	@$(RMDIR) utils/__pycache__
	@echo "Performing distclean in all subdirectories..."
	@$(CD) "$(EXPECTED_DIR)" && $(MAKE) distclean && $(RETURN)
	@$(CD) "$(OUTPUT_DIR)" && $(MAKE) distclean && $(RETURN)
	@echo "Removing *.txt and *.tex files from $(OUTPUT_DIR)..."
	@find "$(OUTPUT_DIR)" -type f \( -name "*.txt" -o -name "*.tex" \) -delete

# Clean all files
maintainer-clean: distclean
# Same as distclean.  If we could be certain that our QA team
# would approve (without manually inspecting) the entire content
# of ./output after "make all", then we would allow replacing
# ./expected by a copy of ./output which is followed by a
# "make distclean" in ./expected .  Instead, the process is to
# "make distclean" followed by a phone call to the QA Team who
# will take it from there.
