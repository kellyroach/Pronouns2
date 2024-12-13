################################################################
#
#    primary_uty.py
#
################################################################

"""Primary utility functions precede, dominate, command, and separate."""

from trc import *

def precede(n1: Node, n2: Node) -> bool:
    """Determines if n1 precedes n2 in preorder traversal, given neither node dominates the other.

    Args:
        n1 (Node): First node to compare
        n2 (Node): Second node to compare
    Returns:
        bool: True if n1 precedes n2 in traversal order
    """
    return n1.number < n2.number

def dominate(n1: Node, n2: Node) -> bool:
    """Determines if n1 dominates n2 in the syntax tree (i.e., n1 is an ancestor of n2).

    Args:
        n1 (Node): Potential dominating node
        n2 (Node): Potential dominated node
    Returns:
        bool: True if n1 dominates n2
    """
    if n1.number == n2.number:
        return True
    child = n1.down_link
    while child is not None:
        if dominate(child, n2):
            return True
        child = child.right_link
    return False

def command(n1: Node, n2: Node) -> bool:
    """Determines if n1 commands n2 by checking if n1's immediate S-node parent dominates n2.

    Args:
        n1 (Node): Potential commanding node
        n2 (Node): Potential commanded node
    Returns:
        bool: True if n1 commands n2
    """
    return dominate(n1.up_link, n2)

def separate(n1: Node, n2: Node) -> bool:
    """Determines if n1 is separate from n2 by checking if their lowest common ancestor is a C-node.
    
    Args:
        n1 (Node): First node to check
        n2 (Node): Second node to check
    Returns:
        bool: True if n1 is separate from n2
    """
    parent = n1.up_link
    while not dominate(parent, n2):
        parent = parent.up_link
    return parent.id == NodeId.C_NODE
