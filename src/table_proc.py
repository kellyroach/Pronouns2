################################################################
#
#    table_proc.py
#
################################################################

"""Elaborates given syntax trees with chained E-nodes, creating chaining diagrams."""

from abstract import *
from chaining import *
from latex import *
from parse_proc import *
from secondary_uty import *
from txt import *

def chaining(nnodes: list[Node]) -> None:
    """Creates a chaining table by first initializing E-nodes
    under all N-nodes, then processing pronouns in reverse
    order.

    Args:
        nnodes (list[Node]): List of N-nodes from the syntax tree
    """
    try:
        trc_enter(f"chaining")
        init_table(nnodes)
        for n1 in reversed(nnodes):
            # For each N-node n1 that is a pronoun, call
            # procedure chaining_n.
            if n1.ftr[FeatureIndex.PNF] == Feature.PLUS:
                chaining_n(nnodes, n1)
    finally:
        trc_exit(f"chaining:~exiting")
        trc_end()
        pass

def init_table(nnodes: list[Node]) -> None:
    """Initializes the chaining table by creating an E-node
    (subscript 'A') under each N-node, copying features and
    setting pred/succ links.

    Args:
        nnodes (list[Node]): List of N-nodes to initialize table for
    """
    trc_enter(f"init@table")
    last = None
    for n in nnodes:
        n.col_link = new_e_node()
        n.col_link.ftr = n.ftr.copy()
        n.col_link.np_link = n
        n.col_link.sub = 'A'
        n.end_col_link = n.col_link
        n.pred_link = last
        if last is not None:
            last.succ_link = n
        last = n
    if Manager.debug and Manager.init_table:
        nodes = tree_nodes(Node.tree())
        nnodes = tree_n_nodes(Node.tree())
        trc_end()
        table_proc_write_chaining_diagram(nnodes)
        table_proc_write_chaining_table(nnodes)
        table_proc_write_nodes_table(nodes)
    trc_exit(f"init@table:~exiting")

def chaining_n(nnodes: list[Node], n1: Node) -> None:
    """Routes a pronominal N-node to either reflexive or
    non-reflexive chaining based on its RPF (Reflexive Pronoun
    Feature).

    Args:
        nnodes (list[Node]): List of all N-nodes
        n1 (Node): Pronominal N-node to process
    """
    trc_enter(f"chaining@n({long_label(n1)})")
    if n1.ftr[FeatureIndex.RPF] == Feature.PLUS:
        # Inputted pronoun N-node n1 is reflexive.
        refl_chaining(n1)
    elif n1.ftr[FeatureIndex.RPF] == Feature.MINUS:
        # Inputted pronoun N-node n1 isn't reflexive.
        non_refl_chaining(nnodes, n1)
    else:
        raise ValueError("Unexpected QUESTION feature for RPF")
    trc_exit(f"chaining@n:~exiting")

def non_refl_chaining(nnodes: list[Node], n1: Node) -> None:
    """Attempts to chain a non-reflexive pronoun to all preceding N-nodes except itself.

    Args:
        nnodes (list[Node]): List of all N-nodes
        n1 (Node): Non-reflexive pronominal node to process
    """
    trc_enter(f"non@refl@chaining({long_label(n1)})")
    for n2 in reversed(nnodes):
        if n2 != n1:
            chaining_n_to_n(n1, n2)
    trc_exit(f"non@refl@chaining:~exiting")

def refl_chaining(n1: Node) -> None:
    """Attempts to chain a reflexive pronoun only to N-nodes
    that precede it within its simplex.

    Args:
        n1 (Node): Reflexive pronominal node to process
    """
    trc_enter(f"refl@chaining({long_label(n1)})")
    n2 = simplex_pred(n1)
    while n2 is not None:
        if n2 != n1:
            chaining_n_to_n(n1, n2)
        n2 = simplex_pred(n2)
    trc_exit(f"refl@chaining:~exiting")

def simplex_pred(n1: Node) -> Node:
    """Finds the preceding N-node in the same simplex by
    following left_links until reaching an N-node or None.

    Args:
        n1 (Node): Node to find predecessor for
    Returns:
        Node: Predecessor N-node in same simplex, or None
    """
    trc_enter(f"simplex@pred({long_label(n1)})")
    answer = n1
    while True:
        answer = answer.left_link
        if answer is None or answer.id == NodeId.N_NODE:
            trc_exit(f"simplex@pred:~{long_label(answer)}")
            return answer

def chaining_n_to_n(n1: Node, n2: Node) -> None:
    """Attempts to establish chains between E-nodes under n1 and
    n2 if they satisfy sc(), agr(), and rnr() constraints.

    Args:
        n1 (Node): Source N-node (typically pronominal)
        n2 (Node): Target N-node (potential antecedent)
    """
    trc_enter(f"chaining@n@to@n({long_label(n1)},~{long_label(n2)})")
    if not sc(n1, n2) or not agr(n1, n2) or not rnr(n1, n2):
        trc_exit(f"chaining@n@to@n:~exiting")
        return
    old_end_col_link = n1.end_col_link
    e1 = n1
    while e1 != old_end_col_link:
        e1 = e1.col_link
        if e1 is not None:
            chaining_e_to_n(e1, n2)
    trc_exit(f"chaining@n@to@n:~exiting")

def chaining_e_to_n(e1: Node, n2: Node) -> None:
    """Creates a new chain if E-node e1 agrees in features with N-node n2.

    Args:
        e1 (Node): Source E-node
        n2 (Node): Target N-node to potentially chain to
    """
    trc_enter(f"chaining@e@to@n({long_label(e1)},~{long_label(n2)})")
    if agr(e1, n2):
        new_chain(e1, n2)
    trc_exit(f"chaining@e@to@n:~exiting")

def new_chain(e1: Node, n2: Node) -> None:
    """Creates a new E-node copy of n2, links it to e1 via
    chain_link, and inherits non-syntactic features from e1.

    Args:
        e1 (Node): Source E-node to chain from
        n2 (Node): Target N-node to copy and chain to
    """
    trc_enter(f"new@chain({long_label(e1)},~{long_label(n2)})")
    n = new_e_node()
    n.np_link = n2
    n.chain_link = e1
    n.sub = chr(ord(n2.end_col_link.sub) + 1)
    # n2 nonsyntactic QUESTION (?) features replaced by corresponding e1 features
    for i in range(N_FEATURES):
        if n2.ftr[i] == Feature.QUESTION and i != FeatureIndex.RPF:
            n.ftr[i] = e1.ftr[i]
        else:
            n.ftr[i] = n2.ftr[i]
    n2.end_col_link.col_link = n
    n2.end_col_link = n
    if Manager.debug and Manager.new_chain:
        trc_write(f"new@chain:~create~{long_label(n)}")
        hat = "^" if (Manager.file_type == FileType.TXT) else "\\symbol{94}"
        trc_write(f"new@chain:~create~{long_label(n)}" + hat + f"{long_label(e1)}")
        nodes = tree_nodes(Node.tree())
        nnodes = tree_n_nodes(Node.tree())
        trc_end()
        table_proc_write_chaining_diagram(nnodes)
        table_proc_write_chaining_table(nnodes)
        table_proc_write_nodes_table(nodes)
    trc_exit(f"new@chain:~exiting")

def table_proc_write_nodes_table(nodes: list[Node]):
    if Manager.debug and Manager.nodes_table:
        if Manager.file_type == FileType.TXT:
            Manager.write("\n")
            txt_nodes(nodes)
        elif Manager.file_type == FileType.TEX:
            try:
                Manager.write("\n")
                latex_nodes(nodes)
            finally:
                trc_end()
                pass

def table_proc_write_chaining_diagram(nnodes: list[Node]):
    if Manager.debug and Manager.chaining_diagram:
        if Manager.file_type == FileType.TEX:
            try:
                Manager.write("\n")
                chaining_diagram(nnodes)
            finally:
                trc_end()
                pass

def table_proc_write_chaining_table(nnodes: list[Node]):
    if Manager.debug and Manager.chaining_table:
        if Manager.file_type == FileType.TXT:
            Manager.write("\n")
            txt_chaining(nnodes)
        elif Manager.file_type == FileType.TEX:
            try:
                Manager.write("\n")
                latex_chaining(nnodes)
            finally:
                trc_end()
                pass
