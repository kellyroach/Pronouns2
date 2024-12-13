# Makefile for Sphinx documentation

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

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SPHINXAPIDOC  ?= sphinx-apidoc
SOURCEDIR     = source
BUILDDIR      = build
PROJECTDIR    = ..

.PHONY: help Makefile clean html all apidoc distclean maintainer-clean

# Put it first so that "make" without argument is like "make help".
help:
	@echo "Available targets:"
	@echo "  help              - Print this help"
	@echo "  view              - Build everything; view HTML doc"
	@echo "  all               - Clean everything and rebuild HTML documentation"
	@echo "  apidoc            - Generate API documentation"
	@echo "  linkcheck         - Check external links for integrity"
	@echo "  html              - Generate HTML documentation"
	@echo "  clean             - Remove intermediate build files"
	@echo "  distclean         - Remove non-shipping files, including the build directory"
	@echo "  maintainer-clean  - Remove all generated files, including shipped HTML files"

# Build everything; view HTML doc
view: all clean
	$(OPEN) "$(BUILDDIR)/html/index.htm"

# Main target - clean everything and rebuild
all: clean html

# Make API documentation
apidoc:
	@$(SPHINXAPIDOC) -f -o ./$(SOURCEDIR) $(PROJECTDIR)

# Check external links for integrity
linkcheck: apidoc
	@$(SPHINXBUILD) -M linkcheck "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Make HTML documentation
html: apidoc
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Sphinx clean HTML documentation
clean:
	@$(SPHINXBUILD) -M clean "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Remove non-shipping files, but keep shipping HTML files
distclean:
	$(RMDIR) "$(BUILDDIR)/doctrees"

# Remove all generated files, including shipped HTML files
maintainer-clean: distclean
	@#NOT: $(RMDIR) "$(SOURCEDIR)/_static"
	@#NOT: $(RMDIR) "$(SOURCEDIR)/_templates"
	$(RM) "$(BUILDDIR)/html/index.htm"
	$(RMDIR) "$(BUILDDIR)/*"
