################################################################
#
#    lexicon.py
#
################################################################

"""Defines lexicon_lookup and lexicon_dict to store lexical entries."""

from node_proc import *

# Global dictionary to store lexical entries
lexicon_dict = {}

def lexicon_init() -> None:
    """Initialize the lexicon with lexicon entries"""
    global lexicon_dict
    # Initial lexicon entries with feature strings
    lexicon_entries = {
        "Algernon":     "---+--+--",
        "Anna":         "---+-++--",
        "Bernie":       "---+--+--",
        "Bill":         "---+--+--",
        "Bob":          "---+--+--",
        "Ernie":        "---+--+--",
        "Fred":         "---+--+--",
        "Harry":        "---+--+--",
        "I":            "++---?+--",
        "Jack":         "---+--+--",
        "Janet":        "---+-++--",
        "Jill":         "---+-++--",
        "John":         "---+--+--",
        "June":         "---+-++--",
        "Las Vegas":    "---+-?---",
        "Linda":        "---+-++--",
        "Mary":         "---+-++--",
        "Mig":          "---+-?---",
        "Oscar":        "---+--+--",
        "PHI":          "+??????--",
        "Penelope":     "---+-++--",
        "Peter":        "---+--+--",
        "Sandy":        "---+-++--",
        "Sue":          "---+-++--",
        "all":          "+--+-??--",
        "another":      "+--+-??--",
        "any":          "+--+-??--",
        "asshole":      "---+-?+--",
        "aunt":         "---+-++--",
        "blame":        "---+-??--",
        "boy":          "---+--+--",
        "brother":      "---+--+--",
        "camel":        "---+-?+--",
        "candy":        "---+-?---",
        "cat":          "---+-?+--",
        "complaining":  "---+-?---",
        "dad":          "---+--+--",
        "daughter":     "---+-++--",
        "each":         "+--+-??--",
        "embezzler":    "---+-?+--",
        "father":       "---+--+--",
        "fish":         "---+??+--",
        "flower":       "---+-?---",
        "gambler":      "---+-?+--",
        "girl":         "---+-++--",
        "grandfather":  "---+--+--",
        "grandmother":  "---+-++--",
        "hat":          "---+-?---",
        "he":           "+--+--+--",
        "her":          "+--+-++-?",
        "hers":         "+--+-++-+",
        "herself":      "+--+-+++-",
        "him":          "+--+--+--",
        "himself":      "+--+--++-",
        "his":          "+--+--+-+",
        "home":         "---+-?---",
        "house":        "---+-?---",
        "interest":     "---+-?---",
        "it":           "+--+-?---",
        "its":          "+--+-?--+",
        "itself":       "+--+-?-+-",
        "lawn":         "---+-?---",
        "man":          "---+--+--",
        "me":           "++---?+--",
        "men":          "---++-+--",
        "mosquito":     "---+-?+--",
        "mom":          "---+-++--",
        "mother":       "---+-++--",
        "mine":         "++---?+-+",
        "my":           "++---?+-+",
        "myself":       "++---?++-",
        "neighbor":     "---+-?+--",
        "none":         "+--+-??--",
        "one":          "+--+-??--",
        "oneself":      "+--+-??--",
        "other":        "+--+-??--",
        "our":          "++--+?+-+",
        "ours":         "++--+?+-+",
        "ourselves":    "++--+?++-",
        "pen":          "---+-?---",
        "pig":          "---+-?+--",
        "pilot":        "---+-?+--",
        "possibility":  "---+-?---",
        "present":      "---+-?---",
        "problem":      "---+-?---",
        "she":          "+--+-++--",
        "sheep":        "---+??+--",
        "sister":       "---+-++--",
        "smokescreen":  "---+-?---",
        "solution":     "---+-?---",
        "some":         "+--+-??--",
        "somebody":     "+--+-?+--",
        "son":          "---+--+--",
        "student":      "---+-?+--",
        "supper":       "---+-?---",
        "tax":          "---+-?---",
        "that":         "+--+-??--",
        "their":        "+--++?+-+",
        "theirs":       "+--++?+-+",
        "them":         "+--++??--",
        "themselves":   "+--++??+-",
        "these":        "+--++?+--",
        "they":         "+--++?+--",
        "this":         "+--+-?+--",
        "those":        "+--++?+--",
        "toy":          "---+-??--",
        "trouble":      "---+-?---",
        "uncle":        "---+--+--",
        "us":           "++--+?+--",
        "you":          "+-+-??+--",
        "your":         "+-+-??+-+",
        "yours":        "+-+-??+-+",
        "yourself":     "+-+--?++-",
        "yourselves":   "+-+-+?++-",
        "we":           "++--+?+--",
        "what":         "+--+-??--",
        "which":        "+--+-??--",
        "who":          "+--+??+--",
        "whom":         "+--+??+--",
        "whose":        "+--+??+-+"
    }
    # Convert each entry to feature array and store in lexicon
    lexicon_dict = {
        lit: lexicon_feature_str_to_list(features)
        for lit, features in lexicon_entries.items()
    }

def lexicon_lookup(lit: str) -> 'Node':
    """Look up a lit in the lexicon and return a new N-node with appropriate features.
    
    Attempts several approaches before giving up:
    1. Direct lookup
    2. Remove trailing digit (e.g., "mother1" -> "mother")
    3. Remove "'s" and set genitive feature (e.g., "Janet's" -> "Janet")
    4. Remove "s" and set plural feature
    5. Remove "es" and set plural feature
    
    Args:
        lit: The literal string to look up
        
    Returns:
        A new N-node with appropriate features
        
    Raises:
        KeyError: If the lit cannot be handled by any approach
    """
    # Try direct lookup first
    if lit in lexicon_dict:
        node = new_n_node()
        node.lit = lit
        node.ftr = lexicon_dict[lit].copy()
        return node
    # Try removing trailing digit
    if lit and lit[-1].isdigit():
        prefix = lit[:-1]
        try:
            node = lexicon_lookup(prefix)
            node.lit = lit  # Keep original lit with digit
            return node
        except KeyError:
            pass
    # Try handling possessive "'s"
    if lit.endswith("'s"):
        prefix = lit[:-2]
        try:
            node = lexicon_lookup(prefix)
            node.lit = lit  # Keep original possessive form
            node.ftr[FeatureIndex.GEN] = Feature.PLUS
            return node
        except KeyError:
            pass
    # Try handling possessive "s'"
    if lit.endswith("s'"):
        prefix = lit[:-1]
        try:
            node = lexicon_lookup(prefix)
            node.lit = lit  # Keep original possessive form
            node.ftr[FeatureIndex.GEN] = Feature.PLUS
            return node
        except KeyError:
            pass
    # Try handling plural "s"
    if lit.endswith("s"):
        prefix = lit[:-1]
        if prefix in lexicon_dict:
            node = new_n_node()
            node.lit = lit  # Keep plural form
            node.ftr = lexicon_dict[prefix].copy()
            node.ftr[FeatureIndex.PLF] = Feature.PLUS
            return node
    # Try handling plural "es"
    if lit.endswith("es"):
        prefix = lit[:-2]
        if prefix in lexicon_dict:
            node = new_n_node()
            node.lit = lit  # Keep plural form
            node.ftr = lexicon_dict[prefix].copy()
            node.ftr[FeatureIndex.PLF] = Feature.PLUS
            return node
    # If all approaches fail, raise KeyError
    raise KeyError(f"'{lit}' not found in lexicon")

def lexicon_feature_str_to_list(feature_str: str) -> list:
    """Convert a feature string (e.g., '---+-++--') to a list of Features"""
    feature_map = {
        '+': Feature.PLUS,
        '-': Feature.MINUS,
        '?': Feature.QUESTION
    }
    return [feature_map[c] for c in feature_str]

def lexicon_select(feature_str: str) -> list[str]:
    """Returns list of words in lexicon_dict whose Features match feature_str.

    Args:
        feature_str (str): feature string or known lexicon word
        (e.g., '---+-++--' or 'mom')
     
    Returns:
        answer: list[str] of compatible words in lexicon_dict
    """
    answer = []
    if all(char in '+-?' for char in feature_str):
        features1 = lexicon_feature_str_to_list(feature_str)
        for lit, features2 in lexicon_dict.items():
            if eq_features(features1, features2):
                answer.append(lit)
    else:
        node = lexicon_lookup(feature_str)
        if isinstance(node, Node):
            answer = lexicon_select(node.ftr_str)
    return answer

def eq_features(features1: Features, features2: Features) -> bool:
    """Tests if two list of features are compatible.

    Args:
        features1 (Features): First Features to compare
        features2 (Features): Second Features to compare
    Returns:
        bool: True if they are compatible
    """
    answer = True
    for i in range(N_FEATURES):
        if not eq_feat(features1[i], features2[i]):
            answer = False
            break
    return answer

def eq_feat(f1: Feature, f2: Feature) -> bool:
    """Tests if two features are compatible, where only PLUS vs MINUS is considered incompatible.

    Args:
        f1 (Feature): First feature to compare
        f2 (Feature): Second feature to compare
    Returns:
        bool: True if features are compatible
    """
    if f1 == Feature.PLUS:
        answer = f2 != Feature.MINUS
    elif f1 == Feature.MINUS:
        answer = f2 != Feature.PLUS
    else:  # f1 == Feature.QUESTION
        answer = True
    return answer

lexicon_init()
