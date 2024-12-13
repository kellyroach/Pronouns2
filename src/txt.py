################################################################
#
#    txt.py
#
################################################################

"""TXT output functions for FileType.TXT Manager.stream."""

from view import *

################################################################
#txt_nodes
################################################################

def txt_nodes(nodes: list[Node]) -> None:
    """Generates a plain text table displaying all nodes in the
    syntax tree with their identifiers and properties.
    
    Args:
        nodes (list[Node]): List of nodes to display
    """
    rows = view_nodes(nodes)  # Collect rows from all nnodes
    txt_table("NODES", rows, "|r|l|")

################################################################
#txt_features
################################################################

def txt_features(nnodes: list[Node]) -> None:
    """Generates a plain text table displaying the feature
    matrix (PNF, FPF, etc.) for each node in the syntax tree.
    
    Args:
        nnodes (list[Node]): List of nodes to display features for
    """
    rows = view_features(nnodes)  # Collect rows from all nnodes
    n = len(rows[0])
    align = f"|r|{'c|' * (n - 1)}"
    txt_table("FEATURES", rows, align)

################################################################
#txt_chaining
################################################################

def txt_chaining(nnodes: list[Node]) -> None:
    """Generates a plain text table showing the binding chains
    between N-nodes and their associated E-nodes.
    
    Args:
        nnodes (list[Node]): List of N-nodes to display chains for
    """
    rows = view_chaining(nnodes)  # Collect rows from all nnodes
    n = len(rows[0])
    align = f"|{'l|' * n}"
    txt_table("CHAINING", rows, align)

################################################################
#txt_interpretations
################################################################

def txt_interpretations(interps: list[list[list[Node]]]) -> None:
    """Generates a plain text table displaying all valid pronoun
    binding interpretations found for the sentence.
    
    Args:
        interps (list[list[list[Node]]]): List of valid interpretations to display
    """
    rows = view_interpretations(interps)  # Collect rows from all nnodes
    txt_table("INTERPRETATIONS", rows, "|c|")

################################################################
#txt_summary
################################################################

def txt_summary() -> None:
    """Generates a plain text table displaying demo Summary."""
    rows = view_summary()
    align = f"|r|r|"
    txt_table("SUMMARY", rows, align)

################################################################
#txt_lexicon
################################################################

def txt_lexicon() -> None:
    """Generates a plain text table displaying the feature
    matrix (PNF, FPF, etc.) for each entry in lexicon_dict."""
    rows = view_lexicon()
    n = len(rows[0])
    align = f"|r|{'c|' * (n - 1)}"
    txt_table("LEXICON", rows, align)

################################################################
#txt_table
################################################################

def txt_table(title: str, rows: list[list[str]], align: str) -> None:
    columns = view_transpose(rows)
    widths = txt_view_widths(columns)
    total_width = txt_view_total_width(columns, align)
    top1 = txt_str_align(title, total_width, "c").replace(" ","_")
    n = len(rows[0])
    top2 = txt_row([""] * n, widths, align)
    hline = top2.replace(" ","_")
    txt = txt_rows(rows, widths, align)
    Manager.write(f"{top1}\n")
    Manager.write(f"{top2}\n")
    txt_table_write(txt)
    Manager.write(f"{hline}\n")

def txt_table_write(txt: list[list[str]]) -> None:
    for row in txt:
        Manager.write(f"{row}\n")

################################################################
#Support txt.py
################################################################

def txt_rows(rows: list[list[str]], widths: list[int], align: str) -> list[str]:
    return [txt_row(row, widths, align) for row in rows]

def txt_row(row: list[str], widths: list[int], align: str) -> str:
    answer = ""
    p = 0  # Pointer to the row and widths elements
    for i, char in enumerate(align):
        if char in {"l", "c", "r"}:
            # Extract the pth element and width
            element = row[p] if p < len(row) else ""
            width = widths[p] if p < len(widths) else 0
            # Append the aligned string
            answer += txt_str_align(element, width, char)
            p += 1
        elif char == "|":
            # Determine the correct translation for "|"
            if i == 0:
                answer += "! "
            elif i == len(align) - 1:
                answer += " !"
            else:
                answer += " ! "
    return answer

def txt_str_align(element: str, width: int, align: str = "l") -> str:
    if align == "l":
        return element.ljust(width)
    elif align == "c":
        return element.center(width)
    elif align == "r":
        return element.rjust(width)
    else:
        raise ValueError("Invalid alignment option; use 'l', 'c', or 'r'")

def txt_view_total_width(view: list[list[str]], align: str) -> int:
    # Calculate widths of each column
    column_widths = txt_view_widths(view)
    total_width = sum(column_widths)
    # Calculate additional width from "|" characters in align
    for i, char in enumerate(align):
        if char == "|":
            # Check if "|" is at the start or end of the align string
            if i == 0 or i == len(align) - 1:
                total_width += 2  # "| " or " |" at ends
            else:
                total_width += 3  # " | " in the middle
    return total_width

def txt_view_widths(view: list[list[str]]) -> list[int]:
    return [txt_column_width(column) for column in view]

def txt_column_width(column: list[str]) -> int:
    return max(len(item) for item in column)
