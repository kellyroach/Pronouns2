# Makefile for docs directory

# Tools
PDFLATEX = pdflatex
BIBER = biber
MAKEINDEX = makeindex

# Platform-specific commands
ifeq ($(OS),Windows_NT)
    RM = del /Q
    OPEN = start
    # Windows findstr alternative to grep
    check_complex = findstr /R /C:"\\print\(bibliography\|index\)" $(1) >nul 2>&1
    # Windows way to get basename
    basename = $(basename $(1) .tex)
else
    RM = rm -f
    OPEN = open
    check_complex = grep -q "\\\\print\\(bibliography\\|index\\)" $(1) 2>/dev/null
    basename = $$(basename $(1) .tex)
endif

# File lists
TEX_FILES = $(filter-out Pronouns2Macros.tex,$(wildcard *.tex))
SHIPPING_PDFS = Demo.pdf Pronouns2Modula2.pdf Pronouns2Python.pdf RelatedLiterature.pdf VaryingRho.pdf

.PHONY: all help clean distclean maintainer-clean

help:
	@echo "Available targets:"
	@echo "  help              - Print this help"
	@echo "  view              - Build everything; view Demo.pdf"
	@echo "  all               - Process all LaTeX files in directory (except Pronouns2Macros.tex)"
	@echo "  xxx               - Process specific file (e.g., 'make Pronouns2Python')"
	@echo "  xxx.pdf           - Same as above, will process xxx.tex"
	@echo "  clean             - Remove intermediate LaTeX files"
	@echo "  distclean         - Remove all generated files except shipping PDFs"
	@echo "  maintainer-clean  - Remove all generated files, including shipping PDFs"

# Build everything; view Demo.pdf
view: all clean
	$(OPEN) Demo.pdf
	$(OPEN) Pronouns2Python.pdf

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
	@if [ "$<" = "Pronouns2Macros.tex" ]; then \
		echo "Pronouns2Macros.tex is an include file and cannot be processed directly."; \
		exit 1; \
	fi
	@if $(call check_complex,$<); then \
		echo "Processing complex LaTeX file $<..." && \
		$(PDFLATEX) -interaction=nonstopmode $< && \
		$(PDFLATEX) -interaction=nonstopmode $< && \
		$(BIBER) $* && \
		$(MAKEINDEX) $* && \
		$(PDFLATEX) -interaction=nonstopmode $< && \
		$(PDFLATEX) -interaction=nonstopmode $<; \
	else \
		echo "Processing simple LaTeX file $<..." && \
		$(PDFLATEX) -interaction=nonstopmode $<; \
	fi

# Rule for .pdf targets
%.pdf: %.tex
	@$(MAKE) $*

# Rule to handle .txt files
%.txt:
	@echo "Text files are pre-built and cannot be processed."
	@exit 0

# Rule to handle .bib files
%.bib:
	@echo "Bibliography files are pre-built and cannot be processed."
	@exit 0

# Clean intermediate files
clean:
	$(RM) *.aux *.bbl *.bcf *.blg *.idx *.ilg *.ind *.log *.out *.run.xml *.toc *~ \#*\#
	@echo "Intermediate files cleaned."

# Clean intermediate files and non-shipping PDFs
distclean: clean
ifeq ($(OS),Windows_NT)
	for %%f in (*.pdf) do @if not exist $(SHIPPING_PDFS) del %%f
else
	rm -f $(filter-out $(SHIPPING_PDFS), $(wildcard *.pdf))
endif
	@echo "Non-shipping PDFs cleaned."

# Clean all files, including shipping PDFs
maintainer-clean: distclean
	$(RM) $(SHIPPING_PDFS)
	@echo "All generated files, including shipping PDFs, cleaned."
