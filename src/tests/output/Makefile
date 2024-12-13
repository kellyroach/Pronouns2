# Makefile for src/tests/expected directory

# Tools
PDFLATEX = pdflatex

# Platform-specific commands
ifeq ($(OS),Windows_NT)
    RM = del /Q
    # Windows way to get basename
    basename = $(basename $(1) .tex)
else
    RM = rm -f
    basename = $$(basename $(1) .tex)
endif

# List of .tex files in the current directory
TEX_FILES = $(wildcard *.tex)

.PHONY: all help clean distclean maintainer-clean

help:
	@echo "Available targets:"
	@echo "  help              - Print this help"
	@echo "  all               - Process all LaTeX files in directory"
	@echo "  xxx               - Process specific file"
	@echo "  xxx.pdf           - Same as above, will process xxx.tex"
	@echo "  clean             - Remove intermediate LaTeX files"
	@echo "  distclean         - Remove all generated files"
	@echo "  maintainer-clean  - Remove all generated files"

# Main target to process all files
all:
ifeq ($(OS),Windows_NT)
	@for %%f in ($(TEX_FILES)) do @( \
		echo Processing %%~nf... & \
		$(MAKE) %%~nf || echo Warning: Processing %%~nf failed, continuing... \
	)
else
	@for file in $(TEX_FILES); do \
		base=$$(basename $$file .tex); \
		echo "Processing $$base..."; \
		$(MAKE) $$base || echo "Warning: Processing $$base failed, continuing..."; \
	done
endif

# Pattern rule for .tex or no-extension targets
%: %.tex
	echo "Processing LaTeX file $<..." && \
	$(PDFLATEX) -interaction=nonstopmode $<

# Rule for .pdf targets
%.pdf: %.tex
	@$(MAKE) $*

# Rule to handle .txt files
%.txt:
	@echo "Text files are pre-built and cannot be processed."

# Clean intermediate pdflatex generated files
clean:
        # Keep Makefile, *.txt, *.tex, *.pdf
	@echo "Removing intermediate files"
	$(RM) *.aux *.log *~ \#*\#

# Clean all pdflatex generated files
distclean: clean
        # Ideal for shipping ./expected content
	@echo "Removing all PDF files"
	$(RM) *.pdf

# Clean all files
maintainer-clean: distclean
        # Ideal for shipping ./output content
	@echo "Removing all files except Makefile"
	$(RM) *.txt *.tex
