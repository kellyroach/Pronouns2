################################################################
#
#     doc.py
#
################################################################

"""Writes demo output for all examples to file."""

import os
from demo import *

def doc(numbers = None, file: str = "../docs/Demo", **kwargs) -> str:
    """Output file containing example sentences with their analyses.

    Args:
        numbers (optional): None, str, or list[str] of keys in example_dict
        file (str, optional): File name. Defaults to "../docs/Demo".
        kwargs: other key-value arguments accepted by Manager.set_state

    Returns:
        str: The full path to the generated file.
    """
    # Set default file_type if not in kwargs
    if 'file_type' not in kwargs:
        kwargs['file_type'] = FileType.TEX
    full_path = doc_full_path(kwargs['file_type'], file)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    # Open the file and write content
    with open(full_path, "w", encoding='utf-8') as stream:
        kwargs['stream'] = stream
        with Manager.manager:
            # Update the state of the singleton Manager
            Manager.set_state(**kwargs)
            # Write documentation content
            doc_begin()
            demo(numbers, **kwargs)
            doc_end()
    return full_path

def doc_full_path(file_type: FileType, file: str) -> str:
    """Generates a documentation file containing all example sentences and their analyses.

    Args:
        file_type (FileType, optional): Output file_type (TXT or TEX).
        file (str, optional): Output file name.

    Returns:
        str: The full path for generated file.
    """
    # Add the appropriate file extension if missing
    if not os.path.splitext(file)[1]:
        file += file_type.file_ext
    # Ensure the directory for the file exists
    full_path = os.path.abspath(file)
    return full_path

def doc_begin():
    if Manager.file_type == FileType.TXT:
        doc_begin_txt()
    elif Manager.file_type == FileType.TEX:
        doc_begin_latex()

def doc_begin_txt():
    """Write TXT document opening boilerplate if Manager.file_type = FileType.TXT."""
    file_with_ext = os.path.basename(Manager.stream.name)
    Manager.write("################################################################\n")
    Manager.write("#\n")
    Manager.write(f"#     {file_with_ext}\n")
    Manager.write("#\n")
    Manager.write("################################################################\n")

def doc_begin_latex():
    """Write LaTeX document opening boilerplate if Manager.file_type = FileType.TEX."""
    file_with_ext = os.path.basename(Manager.stream.name)
    file_without_ext = os.path.splitext(file_with_ext)[0]
    Manager.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
    Manager.write("%\n")
    Manager.write(f"%     {file_without_ext}.tex\n")
    Manager.write("%\n")
    Manager.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
    Manager.write("\\documentclass{article}\n")
    Manager.write("\\input Pronouns2Macros.tex\n")
    Manager.write("\n")
    Manager.write("\\begin{document}\n")
    Manager.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
    Manager.write("%\n")
    Manager.write("%     Title\n")
    Manager.write("%\n")
    Manager.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
    Manager.write("\n")
    title = tex_escape_str(file_without_ext)
    Manager.write(f"\\title{{\\textbf{{{title}}}}}\n")
    Manager.write("\\maketitle\n")

def doc_end():
    """Write LaTeX document closing boilerplate if Manager.file_type = FileType.TEX."""
    if Manager.file_type == FileType.TEX:
        Manager.write("\n")
        Manager.write("\\end{document}\n")
