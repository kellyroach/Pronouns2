Software Requirements
=====================

Git Clone
---------

.. code-block:: bash

    git clone https://github.com/kellyroach/Pronouns2

Python Requirements
-------------------

- Python 3.9 or later
- Required packages can be installed using:

  .. code-block:: bash

      make install   # First-time installation
      make update    # Update existing installation

  or manually with:

  .. code-block:: bash

      pip install -r requirements.txt

LaTeX Requirements
------------------

Recreating ``*.pdf`` from ``*.tex`` requires:

- `MikTeX <https://miktex.org>`_ 22.1 or compatible
- pdflatex 4.10.0 or compatible
- biber 2.20 or compatible
- makeindex 2.12 or compatible

Required LaTeX packages (managed by `MikTeX <https://miktex.org>`_):

- bm
- imakeidx
- bookmark
- courier
- indentfirst
- inputenc
- tikz-cd
- biblatex (with biber backend)
- setspace

Git Bash for Windows Users
--------------------------

See :ref:`GitBash` for explanation and instructions,
if you are using Microsoft Windows.
