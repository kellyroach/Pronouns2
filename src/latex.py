################################################################
#
#    latex.py
#
################################################################

"""LaTeX output functions for FileType.LATEX Manager.stream."""

from modern import *

################################################################
#latex_features
################################################################

def latex_features(nodes: list[Node], title: str = "Features") -> None:
    """Generates a LaTeX tabular displaying the feature matrix
    (PNF, FPF, etc.) for each node in the syntax tree.  The
    output is split into chunks of 40 data rows each (plus
    header row) to improve LaTeX processing.
    
    Args:
        nodes (list[Node]): List of nodes to display features for
        title (str, optional): Title for the feature matrix. Defaults to "Features".
    """
    rows = view_features(nodes)  # Collect rows from all nodes
    latex_features_rows(rows, title=title)

def latex_features_rows(rows: list[list[str]], title: str = "Features") -> None:
    if len(rows) <= 41:  # If we have 40 or fewer data rows (plus header)
        latex_features_write(rows, title)
        return
    # Split into chunks of 40 data rows each, but keep header row for each chunk
    header_row = rows[0]
    data_rows = rows[1:]
    chunk_size = 40
    for i in range(0, len(data_rows), chunk_size):
        # Create chunk with header + next set of data rows
        chunk = [header_row] + data_rows[i:i + chunk_size]
        # Write this chunk
        latex_features_write(chunk, title)
        # Add spacing between chunks (except after the last chunk)
        if i + chunk_size < len(data_rows):
            Manager.write("\\bigbreak\n")

def latex_features_write(rows: list[list[str]], title: str) -> None:
    """Generate LaTeX tabular showing features from rows of data.

    Args:
        rows: List of rows, each representing features of a node.
    """
    row0 = rows[0]
    n = len(row0)
    # Prolog: Start the LaTeX table
    Manager.write("\\bigbreak\n")
    Manager.write("\\begin{minipage}{\\textwidth}\n")
    Manager.write("  \\makebox[\\textwidth][c]{\n")
    Manager.write(f"  \\begin{{tabular}}{{|r|{'c|' * (n - 1)}}}\n")
    Manager.write("    \\hline\n")
    Manager.write(f"    \\multicolumn{{{n}}}{{|c|}}{{\\textbf{{{title}}}}} \\\\\n")
    Manager.write("    \\hline\n")
    # Header row
    Manager.write(f"   ")
    for i, feature in enumerate(row0[1:], 1):
        if i % 2 == 0:
            Manager.write("\n   ")
        Manager.write(f" & \\textbf{{\\texttt{{{feature}}}}}")
    Manager.write(" \\\\\n")
    # Data rows
    for row in rows[1:]:
        token = modern_token(row[0], bold=True, code=True)
        Manager.write(f"    {token}")
        for i, feature in enumerate(row[1:], 1):
            if i % 2 == 0:
                Manager.write("\n   ")
            Manager.write(f" & \\texttt{{{feature}}}")
        Manager.write(" \\\\\n")
    # Epilog: Close the LaTeX table
    Manager.write("    \\hline\n")
    Manager.write("  \\end{tabular}\n")
    Manager.write("  }\n")
    Manager.write("\\end{minipage}\n")
    Manager.write("\\bigbreak\n")

################################################################
#latex_nodes
################################################################

def latex_nodes(nodes: list[Node]) -> None:
    """Generates a LaTeX tabular displaying all nodes in the
    syntax tree with their identifiers and properties.
    
    Args:
        nodes (list[Node]): List of nodes to display
    """
    rows = view_nodes(nodes)  # Convert nodes to LaTeX-compatible rows
    latex_nodes_write(rows)   # Write rows to Manager.stream

def latex_nodes_write(rows: list[list[str]]) -> None:
    """Generates LaTeX source code from the provided rows of node data.

    Args:
        rows (list[str]): List of rows, each a list of two strings.
    """
    # Prolog: Start the LaTeX table
    Manager.write("\\bigbreak\n")
    Manager.write("\\begin{minipage}{\\textwidth}\n")
    Manager.write("  \\makebox[\\textwidth][c]{\n")
    Manager.write("  \\begin{tabular}{|r|l|}\n")
    Manager.write("    \\hline\n")
    Manager.write("    \\multicolumn{2}{|c|}{\\textbf{Nodes}} \\\\\n")
    Manager.write("    \\hline\n")
    # Iterate over the rows and write each one to Manager.stream
    for row in rows:
        Manager.write(f"    ")
        # Unpack the two elements of each row
        first, second = row
        first = tex_code(first)
        # Remove trailing tilde and add phantom Z if present
        if first and first.endswith('~'):
            first = first[:-1] + "Z"
        if first:
            # If it’s the first line with a non-empty first element.
            # Subsequent lines have an empty first element.
            first = modern_token(first, bold=True)
            first = first.replace("_{\\textbf{\\textrm{z}}}","_{\\phantom{z}}")
            Manager.write(f"{first} ")
        second = tex_code(second)
        second = modern_nodes_str(second)
        Manager.write(f"& \\texttt{{{second}}} \\\\\n")
    # Epilog: Close the LaTeX table
    Manager.write("    \\hline\n")
    Manager.write("  \\end{tabular}\n")
    Manager.write("  }\n")
    Manager.write("\\end{minipage}\n")
    Manager.write("\\bigbreak\n")

################################################################
#latex_chaining
################################################################

def latex_chaining(nnodes: list[Node]) -> None:
    """Generates a LaTeX tabular showing the binding chains
    between N-nodes and their associated E-nodes.
    
    Args:
        nnodes (list[Node]): List of N-nodes to display chains for
    """
    rows = view_chaining(nnodes)  # Collect rows from all nnodes
    latex_chaining_write(rows)

def latex_chaining_write(rows: list[list[str]]) -> None:
    """Generate LaTeX Chaining tabular showing chains from rows of data.

    Args:
        rows: List of rows, each representing features of a node.
    """
    row0 = rows[0]
    n = len(row0)
    # Prolog: Start the LaTeX table
    Manager.write("\\bigbreak\n")
    Manager.write("\\begin{minipage}{\\textwidth}\n")
    Manager.write("  \\makebox[\\textwidth][c]{\n")
    Manager.write(f"  \\begin{{tabular}}{{|{'l|' * n}}}\n")
    Manager.write("    \\hline\n")
    Manager.write(f"    \\multicolumn{{{n}}}{{|c|}}{{\\textbf{{Chaining}}}} \\\\\n")
    Manager.write("    \\hline\n")
    # Header row
    Manager.write(f"    ")
    for i, chain in enumerate(row0, 0):
        if i > 0:
            if i % 2 == 0:
                Manager.write("\n   ")
            Manager.write(" & ")
        chain = modern_chain(chain, bold=True, code=True)
        Manager.write(f"{chain}")
    Manager.write(" \\\\\n")
    # Data rows
    for row in rows[1:]:
        Manager.write(f"    ")
        for i, chain in enumerate(row, 0):
            if i > 0:
                if i % 2 == 0:
                    Manager.write("\n   ")
                Manager.write(" & ")
            chain = tex_code(chain)
            chain = modern_chain(chain, code=True)
            Manager.write(f"{chain}")
        Manager.write(" \\\\\n")
    # Epilog: Close the LaTeX table
    Manager.write("    \\hline\n")
    Manager.write("  \\end{tabular}\n")
    Manager.write("  }\n")
    Manager.write("\\end{minipage}\n")
    Manager.write("\\bigbreak\n")

################################################################
#latex_interpretations
################################################################

def latex_interpretations(interps: list[list[list[Node]]]) -> None:
    """Generates a LaTeX tabular displaying all valid pronoun
    binding interpretations found for the sentence.
    
    Args:
        interps (list[list[list[Node]]]): List of valid interpretations to display
    """
    rows = view_interpretations(interps)  # Collect rows from all nnodes
    latex_interpretations_write(rows)

def latex_interpretations_write(rows: list[str]) -> None:
    """Generate LaTeX Interpretations tabular showing rows.

    Args:
        rows: List of rows, each row representing an interpretation.
    """
    # Prolog: Start the LaTeX table
    Manager.write("\\bigbreak\n")
    Manager.write("\\begin{minipage}{\\textwidth}\n")
    Manager.write("  \\makebox[\\textwidth][c]{\n")
    Manager.write(f"  \\begin{{tabular}}{{|c|}}\n")
    Manager.write("    \\hline\n")
    Manager.write(f"    \\multicolumn{{1}}{{|c|}}{{\\textbf{{Interpretations}}}} \\\\\n")
    Manager.write("    \\hline\n")
    # Data rows
    for row in rows:
        row = tex_code(row[0])
        if len(row) == 0:
            # This happens if there are no pronouns nor PHI's.  The other
            # branch of this "if" statement would just print a blank line
            # which, for a while, confused us.  Now we'll print ${\cdot}$
            # which is distinguishable from a blank line and reminds us.
            Manager.write("    ${\\cdot}$ \\\\\n")
        else:
            row = modern_interp(row, code=True)
            Manager.write(f"    {row} \\\\\n")
        Manager.write("    \\hline\n")
    # Epilog: Close the LaTeX table
    Manager.write("  \\end{tabular}\n")
    Manager.write("  }\n")
    Manager.write("\\end{minipage}\n")
    Manager.write("\\bigbreak\n")

################################################################
#latex_summary
################################################################

def latex_summary() -> None:
    """Generates a LaTeX table displaying demo Summary."""
    rows = view_summary()
    latex_summary_write(rows)

def latex_summary_write(rows: list[str]) -> None:
    """Generate LaTeX Summary tabular showing rows.

    Args:
        rows: List of rows, each row presenting a demo statistic.
    """
    # Prolog: Start the LaTeX table
    Manager.write("\\bigbreak\n")
    Manager.write("\\begin{minipage}{\\textwidth}\n")
    Manager.write("  \\makebox[\\textwidth][c]{\n")
    Manager.write(f"  \\begin{{tabular}}{{|r|r|}}\n")
    Manager.write("    \\hline\n")
    Manager.write(f"    \\multicolumn{{2}}{{|c|}}{{\\textbf{{Summary}}}} \\\\\n")
    Manager.write("    \\hline\n")
    # Data rows
    for row in rows:
        Manager.write(f"    {row[0]} & {tex_code(row[1])} \\\\\n")
    Manager.write("    \\hline\n")
    # Epilog: Close the LaTeX table
    Manager.write("  \\end{tabular}\n")
    Manager.write("  }\n")
    Manager.write("\\end{minipage}\n")
    Manager.write("\\bigbreak\n")

################################################################
#latex_lexicon
################################################################

def latex_lexicon() -> None:
    """Generates a LaTeX tabular displaying the feature matrix
    (PNF, FPF, etc.) for each entry in lexicon_dict."""
    rows = view_lexicon()
    latex_features_rows(rows, title="Lexicon")
