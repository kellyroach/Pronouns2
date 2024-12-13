################################################################
#
#    parser.py
#
################################################################

"""Converts nested list/string representations to syntax trees built from Node's."""

from lexicon import *

# Global counter for node numbering in preorder traversal
parse_prev_node = None

def parse(csn) -> Node:
    """Converts a nested list/string representation into a
    syntax tree with C, S, and N nodes, establishing node links
    and threading.
    
    Args:
        csn: Either a string (for N-nodes) or a list starting
        with "C" or "S" followed by child nodes

    Returns:
        Node: Root node of the constructed syntax tree
    """
    global parse_prev_node
    node_proc_reset()
    parse_prev_node = None
    answer = parse_recurse(csn)
    return answer

def parse_recurse(csn) -> Node:
    """Called by parse."""
    global parse_prev_node
    # Case 1: String represents an N-node
    if isinstance(csn, str):
        node = lexicon_lookup(csn)
        parse_thread(node)
        return node
    # Case 2: List represents a C-node or S-node
    if not isinstance(csn, list) or len(csn) < 1:
        raise ValueError("Invalid parse object")
    # Create appropriate node type
    if csn[0] == "C":
        node = new_c_node()
    elif csn[0] == "S":
        node = new_s_node()
    else:
        raise ValueError(f"Unknown node type: {csn[0]}")
    parse_thread(node)
    # Process children
    first_child = None
    prev_child = None
    for child in csn[1:]:
        child = parse_recurse(child)
        # Set up links
        child.up_link = node
        if first_child is None:
            first_child = child
        else:
            prev_child.right_link = child
            child.left_link = prev_child
        prev_child = child
    # Set down_link to first child
    node.down_link = first_child
    return node

def parse_thread(node: Node):
    global parse_prev_node
    if parse_prev_node is not None:
        parse_prev_node.thread_link = node
    parse_prev_node = node

def tree_nodes(tree: Node) -> list[Node]:
    """Return a list of all nodes in preorder traversal order.

    Args:
        tree: Root node of the parse tree.

    Returns:
        List of nodes in preorder traversal order.
    """
    nodes = []
    _tree_nodes_collect(tree, nodes)
    return nodes

def _tree_nodes_collect(node: Node, nodes: list[Node]) -> None:
    """Helper function to collect nodes in preorder traversal order.

    Args:
        node: Current node being processed.
        nodes: List to accumulate nodes.
    """
    if node is None:
        return
    nodes.append(node)
    if node.id == NodeId.N_NODE or node.id == NodeId.E_NODE:
        _tree_nodes_collect(node.col_link, nodes)
    else:
        _tree_nodes_collect(node.down_link, nodes)
    child = node.down_link
    while child is not None:
        next_child = child.right_link
        if next_child is not None:
            _tree_nodes_collect(next_child, nodes)
        child = next_child

def tree_n_nodes(tree: Node) -> list[Node]:
    """Return a list of N-nodes in preorder traversal order, one per unique lit value.
    
    Args:
        tree: Root node of the parse tree
        
    Returns:
        List of N-nodes, with only the first occurrence of each lit value
    """
    seen_lits = set()
    seen = []
    for node in tree_nodes(tree):
        if node.id == NodeId.N_NODE and node.lit not in seen_lits:
            seen_lits.add(node.lit)
            seen.append(node)
    return seen
