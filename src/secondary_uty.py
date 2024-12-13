################################################################
#
#    secondary_uty.py
#
################################################################

"""Secondary utility functions sc, agr, eq_feat, and rnr."""

from primary_uty import *
from modern import *
from lexicon import *

def sc(n1: Node, n2: Node) -> bool:
    """Checks if basic syntactic conditions for pronoun binding
    are met, particularly the Precedes and Commands Rule.

    Args:
        n1 (Node): Node representing the pronoun
        n2 (Node): Node representing potential antecedent
    Returns:
        bool: True if syntactic conditions for binding are satisfied
    """
    trc_enter("")
    answer = not (precede(n1, n2) and (command(n1, n2) or separate(n1, n2)))
    trc_exit("")
    trc_write(f"sc({long_label(n1)},~{long_label(n2)})~=~{answer}")
    return answer

def agr(n1: Node, n2: Node) -> bool:
    """Verifies agreement between nodes for person, number, gender, and animacy features.

    Args:
        n1 (Node): First node to check agreement
        n2 (Node): Second node to check agreement
    Returns:
        bool: True if all relevant features agree between nodes
    """
    trc_enter("")
    ftr1 = n1.ftr
    ftr2 = n2.ftr
    answer = (eq_feat(ftr1[FeatureIndex.FPF], ftr2[FeatureIndex.FPF]) and
              eq_feat(ftr1[FeatureIndex.SPF], ftr2[FeatureIndex.SPF]) and
              eq_feat(ftr1[FeatureIndex.TPF], ftr2[FeatureIndex.TPF]) and
              eq_feat(ftr1[FeatureIndex.PLF], ftr2[FeatureIndex.PLF]) and
              eq_feat(ftr1[FeatureIndex.GNF], ftr2[FeatureIndex.GNF]) and
              eq_feat(ftr1[FeatureIndex.ANF], ftr2[FeatureIndex.ANF]))
    trc_exit("")
    trc_write(f"agr({long_label(n1)},~{long_label(n2)})~=~{answer}")
    return answer

# NOTE: "def eq_feat" has been moved to lexicon.py .

def rnr(n1: Node, n2: Node) -> bool:
    """Implements the Reflexive/Nonreflexive Rule for pronoun binding in simplexes.
    
    Args:
        n1 (Node): Node representing the pronoun
        n2 (Node): Node representing potential antecedent
    Returns:
        bool: True if reflexive/nonreflexive binding constraints are satisfied
    """
    trc_enter("")
    n1 = n1.np_link
    n2 = n2.np_link
    ftr1 = n1.ftr
    ftr2 = n2.ftr
    if ftr2[FeatureIndex.GEN] == Feature.PLUS:
        answer = False
    elif ftr1[FeatureIndex.RPF] == Feature.PLUS:
        answer = (n1.up_link == n2.up_link) and (ftr1[FeatureIndex.GEN] == Feature.MINUS)
    elif ftr1[FeatureIndex.RPF] == Feature.MINUS:
        answer = (n1.up_link != n2.up_link) or (ftr1[FeatureIndex.GEN] != Feature.MINUS)
    else:  # ftr1[FeatureIndex.RPF] == Feature.QUESTION
        raise ValueError("Unexpected QUESTION feature for RPF")
    trc_exit("")
    trc_write(f"rnr({long_label(n1)},~{long_label(n2)})~=~{answer}")
    return answer

def long_label(node: Node) -> str:
    """Node long label in TXT/TEX according to Manager.file_type
    
    Args:
        node (Node): Node whose long label is required
        
    Returns:
        str: long label in TXT/TEX according to Manager.file_type
    """
    label = view_label(node)
    if Manager.file_type == FileType.TEX:
        label = modern_token(label, bold=False, code=True)
    return label
