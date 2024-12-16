# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('./../..'))


# -- Project information -----------------------------------------------------

project = 'Pronouns2'
copyright = '2024, Kelly Roach'
author = 'Kelly Roach'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinxcontrib.bibtex',
]

html_static_path = ["_static"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Pronouns2'
copyright = '©2024, Kelly Roach'
author = 'Kelly Roach'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Hints for sphinx-apidoc ----------------------------------------------

# autodoc_typehints = "description" moves type hints into the
# function description instead of keeping them in the signature.
autodoc_typehints = "description"

# autodoc_preserve_defaults = True keeps the Python default values
# in their original form when possible.
autodoc_preserve_defaults = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# NOTE: ./themes/pronouns2/layout.html
html_theme = 'pronouns2'
html_theme_path = ["themes"]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# SEE: "HTML theming support"
# https://www.sphinx-doc.org/en/master/usage/theming.html

html_theme_options = {
    "footerbgcolor": "#FFFFFF",
    "sidebarbgcolor": "#339933",
    "relbarbgcolor": "#339933",
    "relbartextcolor": "#FFFFFF",
    "headbgcolor": "#339933",
    "headtextcolor": "#FFFFFF",
    "bodyfont": "Verdana, Geneva, Arial, helvetica, sans-serif;",
    "headfont": "Verdana, Geneva, Arial, helvetica, sans-serif;"
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# This is the file name suffix for generated HTML files. The default is ".html".
# http://www.sphinx-doc.org/en/stable/config.html
html_file_suffix = ".htm"

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Pronouns2doc'


# -- Options for LaTeX output ---------------------------------------------

# NOTE: Possibly latex_elements is for LaTeX output ONLY, not for "math::"
# imgmath appearing inside our *.htm .  Only the imgmath_xxx commands below
# seem to matter for our *.htm .

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    'preamble': r'''
\usepackage{tikz-cd}
''',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Same as \magnification = \magstep 2

# Bibliography Files and Encoding
# https://sphinxcontrib-bibtex.readthedocs.io/en/latest/usage.html

# Math support for HTML outputs in Sphinx
# https://www.sphinx-doc.org/en/master/usage/extensions/math.html
#  pip install sphinxcontrib-bibtex
# We vote 'label' with cite:t and cite:p are the most acceptable.

bibtex_bibfiles = []
# bibtex_encoding = 'latin'
# NOTE: The default for bibtex_encoding is 'utf-8-sig'.  The distinction
# between 'latin' and 'utf-8-sig' affects whether the *.bib file should
# mention "\'e" or "é".  It turns out, we want the default 'utf-8-sig'
# since we are using "é".  sphinxcontrib-bibtex doesn't offer complete
# support for TeX *.bib so we prefer the alternative just so we don't end
# up writing Latin characters two different ways, one for *.rst and one
# for *.bib.  We can see the difference with "François Garillot"
#
# https://sphinxcontrib-bibtex.readthedocs.io/en/latest/usage.html
#
# label, author_year, super, \supercite
# label
#    cite:t: == Davenport et al. [DST88]
#    cite:p: == [DST88]
#    cite:label: == DST88
# author_year
#    cite:t: == Davenport et al. [1988]
#    cite:p: == [Davenport et al., 1988]
#    cite:label: == DST88
# super
#    cite:t: == Davenport et al.^DST88
#    cite:p: == ^DST88
#    cite:label: == DST88
bibtex_reference_style = 'label'

# The command name with which to invoke LaTeX. The default is 'latex';
# you may need to set this to a full path if latex is not in the executable
# search path.
imgmath_latex = '/Users/kellyroach/bin/latex'

# The command name to invoke dvipng. The default is 'dvipng'; you may need
# to set this to a full path if dvipng is not in the executable search path.
# This option is only used when imgmath_image_format is set to 'png'.
imgmath_dvipng = '/Users/kellyroach/bin/dvipng'

# Additional LaTeX code to put into the preamble of the LaTeX files
# used to translate the math snippets. This is left empty by default.
imgmath_latex_preamble = '\\mag=1440\r\n'

# The font size (in pt) of the displayed math. The default value is 12.
# It must be a positive integer.
imgmath_font_size = 10

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Pronouns2.tex', 'Pronouns2',
     'Planet Pronouns2', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'pronouns2', 'Pronouns2',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Pronouns2', 'Pronouns2',
     author, 'Pronouns2', 'One line description of project.',
     'Miscellaneous'),
]


