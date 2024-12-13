################################################################
#
#    view.py
#
################################################################

"""Functions mapping Node and Feature structures to simpler Python lists of strings."""

from typing import Any
from lexicon import *

################################################################
#view_nodes
################################################################

def view_nodes(nodes: list[Node]) -> list[list[str]]:
    """Generates rows representing node properties and links in tabular format.

    Args:
        nodes (list[Node]): Nodes to display
    Returns:
        list[list[str]]: List of rows where each row is [node_number, properties_str]
    """
    rows = []
    for node in nodes:
        rows.extend(view_nodes_row(node))
    return rows

def view_nodes_row(node: Node) -> list[list[str]]:
    """Generates a list of lists of strings for a given Node."""
    # Get the multiline string representation from view_node_str
    node_str = view_node_str(node)
    # Split the string at '\n    ' to get individual lines
    lines = node_str.split('\n    ')
    # Create the list of lists
    rows = []
    for i, line in enumerate(lines):
        # For the first line, use the node number as the first element
        if i == 0:
            label = view_short_label(node)
            if label and label[-1].isdigit():
                label += " "
            rows.append([label, line])
        else:
            # For subsequent lines, use an empty string as the first element
            rows.append(["", line])
    return rows

def view_node_str(node: Node) -> str:
    """Generates a formatted string representation of the given node."""
    node_type = node.id.name[0]  # First letter of the enum name
    base_info = f"({node_type}, "
    if node.id in [NodeId.C_NODE, NodeId.S_NODE]:
        return (f"{base_info}"
                f"up:{view_short_label(node.up_link)}, "
                f"dn:{view_short_label(node.down_link)}, "
                f"lt:{view_short_label(node.left_link)}, "
                f"rt:{view_short_label(node.right_link)}, "
                f"th:{view_short_label(node.thread_link)}, "
                f"nu:{view_short_label(node)})")
    elif node.id == NodeId.N_NODE:
        line1 = (f"{base_info}lit:{node.lit}, "
                 f"ftr:[{node.ftr_str}], "
                 f"up:{view_short_label(node.up_link)}, "
                 f"dn:{view_short_label(node.down_link)},")
        line2 = (f"lt:{view_short_label(node.left_link)}, "
                 f"rt:{view_short_label(node.right_link)}, "
                 f"th:{view_short_label(node.thread_link)}, "
                 f"np:{view_short_label(node.np_link)}, "
                 f"ch:{view_short_label(node.chain_link)}, "
                 f"co:{view_short_label(node.col_link)}, "
                 f"ec:{view_short_label(node.end_col_link)},")
        line3 = (f"pr:{view_short_label(node.pred_link)}, "
                 f"su:{view_short_label(node.succ_link)}, "
                 f"nu:{view_short_label(node)})")
        return f"{line1}\n     {line2}\n     {line3}"
    elif node.id == NodeId.E_NODE:
        return (f"{base_info}sub:{node.sub}, "
                f"ftr:[{node.ftr_str}], "
                f"np:{view_short_label(node.np_link)}, "
                f"ch:{view_short_label(node.chain_link)}, "
                f"co:{view_short_label(node.col_link)})")

################################################################
#view_features
################################################################

def view_features(nnodes: list[Node]) -> list[list[str]]:
    """Generates feature matrix rows with +/-/? indicators for each feature type.

    Args:
        nnodes (list[Node]): N-nodes to display features for
    Returns:
        list[list[str]]: Header row plus feature rows for each node
    """
    # Create header row
    header = [""] + [feature.name for feature in FeatureIndex]
    if HIDE_GEN:
        header = header[:-1]
    # Convert each node to a row
    node_write = [view_features_row(node) for node in nnodes]
    # Combine header and node rows
    return [header] + node_write

def view_features_row(node: Node) -> list[str]:
    """Convert a single N-node into a row of strings for the Features table.
    
    Args:
        node: An N-node whose features are to be converted
        
    Returns:
        List of strings: node's lit value followed by feature symbols
    """
    row = [node.lit]
    for feature in node.ftr:
        if feature == Feature.PLUS:
            row.append("+")
        elif feature == Feature.MINUS:
            row.append("-")
        else:  # Feature.QUESTION
            row.append("?")
    if HIDE_GEN:
        row = row[:-1]
    return row

################################################################
#view_chaining
################################################################

def view_chaining(nnodes: list[Node]) -> list[list[str]]:
    """Generates rows showing E-nodes and their chains under each N-node.

    Args:
        nnodes (list[Node]): N-nodes to show chains for
    Returns:
        list[list[str]]: Rows showing N-nodes and their E-node chains
    """
    columns = view_chaining_columns(nnodes)
    rows = view_transpose(columns)
    return rows

def view_transpose(columns: list[list[str]]) -> list[list[str]]:
    """Transposes columns to rows, filling empty spaces with empty strings.
    
    Args:
        columns (list[list[str]]): Columns to transpose
    Returns:
        list[list[str]]: Transposed rows with empty string padding
    """
    return view_transpose_any(columns, fill_value="")

def view_transpose_any(columns: list[list[Any]], fill_value: Any = None) -> list[list[Any]]:
    """Generic transpose that works with any type, using specified fill value.
    
    Args:
        columns (list[list[Any]]): Columns to transpose
        fill_value (Any, optional): Value to use for padding. Defaults to None
    Returns:
        list[list[Any]]: Transposed rows with fill_value padding
    """
    # Find the maximum length among all columns
    max_len = max(len(column) for column in columns)
    # Pad each column with the specified fill_value to match the max length
    padded_columns = [column + [fill_value] * (max_len - len(column)) for column in columns]
    # Transpose the padded columns to get rows
    rows = [list(row) for row in zip(*padded_columns)]
    return rows

def view_chaining_columns(nnodes: Node) -> list[list[str]]:
    """Return a columns of strings corresponding to N-Node nnodes"""
    return [view_chaining_column(nnode) for nnode in nnodes]

def view_chaining_column(nnode: Node) -> list[str]:
    """Return a column of strings corresponding to N-Node nnode"""
    column = [nnode.lit]
    enode = nnode.col_link
    while enode is not None:
        element = view_chaining_label(enode)
        chain = enode.chain_link
        if chain is not None:
            element = element + "^" + view_chaining_label(chain)
        column.append(element)
        enode = enode.col_link
    return column

def view_chaining_label(node: Node) -> str:
    return node.np_link.lit + node.sub

################################################################
#view_interpretations
################################################################

def view_interpretations(interps: list[list[list[Node]]]) -> list[list[str]]:
    """Generates rows showing valid binding interpretations found for the sentence.

    Args:
        interps (list[list[list[Node]]]): Valid interpretations to display
    Returns:
        list[list[str]]: Rows showing each valid interpretation
    """
    interps = view_interps(interps)
    rows = [view_interpretations_row(interp) for interp in interps]
    if len(rows) == 0:
        rows = [["NONE"]]
    return rows

def view_interpretations_row(interp: list[list[str]]) -> list[str]:
    # Join chains in interp.
    answer = ["    ".join(interp)]
    return answer

################################################################
#view_summary
################################################################

def view_summary() -> list[list[str]]:
    """Generates rows representing demo_all Summary in tabular format.

    Returns:
        list[list[str]]: List of rows where each row is [node_number, properties_str]
    """
    score = 100.0 * (1.0 if (Summary.total == 0) else (Summary.correct / Summary.total))
    rows = [["Meaningless", f"{Summary.meaningless}"],
            ["Meaningful", f"{Summary.meaningful}"],
            ["Ambiguous", f"{Summary.ambiguous}"],
            ["Correct", f"{Summary.correct}"],
            ["Total", f"{Summary.total}"],
            ["Score", f"{score:.1f}%"]]
    return rows

################################################################
#view_lexicon
################################################################

def view_lexicon() -> list[list[str]]:
    """Generates feature matrix rows with +/-/? indicators for each feature type.

    Returns:
        list[list[str]]: Header row plus feature rows for each
        entry in the lexicon_dict
    """
    nnodes = [lexicon_lookup(lit) for lit in lexicon_dict.keys()]
    return view_features(nnodes)

################################################################
#Support table_interp.py
################################################################

def view_interps(interps: list[list[list[Node]]]) -> list[list[list[str]]]:
    """Converts list of interpretations into string representation.
    
    Args:
        interps (list[list[list[Node]]]): Interpretations to convert
    Returns:
        list[list[list[str]]]: String representation of interpretations
    """
    return [view_chains(interp) for interp in interps]

def view_dict(dict: dict[int, list[list[Node]]]) -> dict[int, list[str]]:
    """Converts dictionary mapping node numbers to chains into string representation.
    
    Args:
        dict (dict[int, list[list[Node]]]): Dictionary to convert
    Returns:  
        dict[int, list[str]]: String representation of node-to-chains mapping
    """
    return {k: view_chains(v) for k, v in dict.items()}

def view_chains(chains: list[list[Node]]) -> list[str]:
    """Converts list of chains into list of string representations.
    
    Args:
        chains (list[list[Node]]): Chains to convert
    Returns:
        list[str]: String representations of chains
    """
    return [view_chain(chain) for chain in chains if (len(chain) > 1)]

def view_chain(chain: list[Node]) -> str:
    """Converts single chain into string representation with '^' between nodes.
    
    Args:
        chain (list[Node]): Chain to convert
    Returns:
        str: String representation of chain using '^' separator
    """
    return "^".join([view_label(node) for node in chain])

def view_label(node: Node) -> str:
    """Creates string label for a node, combining np_link's lit value with sub if present.
    
    Args:
        node (Node): Node to create label for
    Returns:
        str: Node's label (e.g. "JohnB")
    """
    if node is None:
        return ""
    if node.id in [NodeId.C_NODE, NodeId.S_NODE]:
        node_type = node.id.name[0]  # First letter of the enum name
        label = f"{node_type}{node.number}"
    else:
        label = node.np_link.lit
        if node.sub != " ":
            label = label + node.sub
    return label

def view_short_label(node: Node) -> str:
    """Creates string short label for a node, combining np_link's number value with sub if present.
    
    Args:
        node (Node): Node to create label for
    Returns:
        str: Node's short label (e.g. "3B")
    """
    if node is None:
        return "0"
    if node.id == NodeId.E_NODE:
        label = f"{node.np_link.number}"
    else:
        label = f"{node.number}"
    if node.sub != " ":
        label = label + node.sub
    return label
