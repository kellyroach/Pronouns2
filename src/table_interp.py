################################################################
#
#    table_interp.py
#
################################################################

"""Determines all valid interpretations (sets of pronoun chains) for given tree."""

from view import *

def interpret(nnodes: list[Node]) -> list[list[list[Node]]]:
    """Determines all valid interpretations (sets of pronoun
    chains) for a list of N-nodes, following binding
    constraints.
    
    Args:
        nnodes (list[Node]): List of N-nodes from a parse tree
    Returns:
        list[list[list[Node]]]: List of valid interpretations,
        where each interpretation is a list of chains
    """
    nnode_dict = interpret_dict(nnodes)
    # Put pronouns first, then non-pronouns in unseen list
    unseen = ([nnode.number for nnode in nnodes if nnode.ftr[FeatureIndex.PNF] == Feature.PLUS] +
              [nnode.number for nnode in nnodes if nnode.ftr[FeatureIndex.PNF] == Feature.MINUS])
    # Start interpret_recurse with empty partials and empty seen list
    return interpret_recurse([], unseen, [], nnode_dict)

def interpret_dict(nnodes: list[Node]) -> dict[int, list[list[Node]]]:
    # Return dict[int, list[list[Node]]] mapping each N-node number
    # to a list of chains
    result = {nnode.number: [] for nnode in nnodes
             if nnode.ftr[FeatureIndex.PNF] == Feature.PLUS}
    # Process each nnode in forward order, allowing interpret_dict_node to modify result
    for nnode in nnodes:
        interpret_dict_node(nnode, result)
    return result

def interpret_dict_node(nnode: Node, result: dict[int, list[list[Node]]]) -> None:
    # Only process chains if the starting node isn't a
    # third person or reflexive pronominal noun.
    if (nnode.ftr[FeatureIndex.PNF] == Feature.MINUS
        or (nnode.ftr[FeatureIndex.TPF] == Feature.MINUS
            and nnode.ftr[FeatureIndex.RPF] == Feature.MINUS)):
        chains = interpret_chains(nnode)
        for chain in chains:
            # For each E-node in the chain
            for enode in chain:
                # If the E-node is a pronoun
                if enode.ftr[FeatureIndex.PNF] == Feature.PLUS:
                    # Get its np_link number and add the chain to that bucket
                    number = enode.np_link.number
                    result[number].append(chain)

def interpret_chains(nnode: Node) -> list[list[Node]]:
    # The "chains" beginning with E-nodes underneath N-node "nnode".
    chains = []
    # Traverse the column of E-nodes hanging from the given N-node
    current = nnode.col_link
    while current:
        # Get the complete chain starting from the current node
        chain = interpret_chain(current)
        chains.append(chain)
        # Move to the next node in the column
        current = current.col_link
    return chains

def interpret_chain(node: Node) -> list[Node]:
    # The "chain" starting with E-node "node" and continued by
    # following "chain_link"s.
    chain = []
    current = node
    while current:
        chain.append(current)
        current = current.chain_link
    return chain

def interpret_recurse(partials, unseen, seen, nnode_dict):
    if not unseen:  # base case
        return partials
    noun = unseen[0]
    # If noun isn't in dictionary, we've hit non-pronouns - just return partials
    if noun not in nnode_dict:
        return partials
    # Process chains for this noun
    chains = nnode_dict[noun]
    return [interp for chain in chains
            for interp in interpret_recurse_chain(chain, partials, unseen, seen, nnode_dict)]

def interpret_recurse_chain(chain, partials, unseen, seen, nnode_dict):
    nouns = interpret_numbers(chain)
    if any(n in seen for n in nouns):
        return []
    partials = [partial + [chain] for partial in (partials or [[]])]
    unseen = [n for n in unseen if n not in nouns]
    seen = seen + nouns
    return interpret_recurse(partials, unseen, seen, nnode_dict)

def interpret_numbers(nodes: list[Node]) -> list[int]:
    # Return list of N-node numbers for all nodes
    return [node.np_link.number for node in nodes]
