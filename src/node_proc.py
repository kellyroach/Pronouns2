################################################################
#
#    node_proc.py
#
################################################################

"""Four functions which create Node's in syntax trees."""

from trc import *

node_number = 0

def node_proc_reset() -> None:
    """Resets the global node counter used to assign unique identification numbers to new nodes."""
    global node_number
    node_number = 0

def new_node(id: NodeId) -> Node:
    global node_number
    answer = Node()
    node_number += 1
    answer.number = node_number
    answer.id = id
    return answer

def new_c_node() -> Node:
    """Creates a new conjoined sentence (C) node, initializing
    it with appropriate defaults for a C-node type.
    
    Returns:
        Node: A newly initialized C-node
    """
    answer = new_node(NodeId.C_NODE)
    return answer

def new_s_node() -> Node:
    """Creates a new sentence (S) node, initializing it with
    appropriate defaults for an S-node type.
    
    Returns:
        Node: A newly initialized S-node
    """
    answer = new_node(NodeId.S_NODE)
    return answer

def new_n_node() -> Node:
    """Creates a new noun phrase (N) node, initializing it with
    appropriate defaults for an N-node type.
    
    Returns:
        Node: A newly initialized N-node
    """
    answer = new_node(NodeId.N_NODE)
    answer.lit = ""
    answer.ftr = [Feature.QUESTION] * N_FEATURES
    answer.end_col_link = None
    answer.pred_link = None
    answer.succ_link = None
    answer.np_link = answer
    return answer

def new_e_node() -> Node:
    """Creates a new elaborated copy (E) node, initializing it
    with appropriate defaults for an E-node type.
    
    Returns:
        Node: A newly initialized E-node
    """
    answer = new_node(NodeId.E_NODE)
    answer.sub = ' '
    answer.ftr = [Feature.QUESTION] * N_FEATURES
    return answer
