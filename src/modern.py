################################################################
#
#    modern.py
#
################################################################

"""Middle layer functions which convert TXT values to LaTeX values."""

import re
from tex import *
from view import *

################################################################
# modern_nodes_str
#   modern_token
# modern_interp
#   modern_chain
# modern_label
#   modern_token
# modern_short_label
#   modern_token
#     modern_base_subscript
# modern_token_width
#   modern_base_subscript
################################################################

def modern_nodes_str(s: str) -> str:
    """Convert Node row string by replacing patterns with LaTeX equivalents.
    
    Args:
        s (str): Input string containing colon-prefixed labels and "lit:" long labels.
        
    Returns:
        str: String with patterns replaced by LaTeX using modern_token.

    Examples:
        >>> modern_nodes_str("x:12A, y:15, z:12B"),
        '\\texttt{x:${\\textrm{12}_{\\textrm{a}}}$, y:15, z:${\\textrm{12}_{\\textrm{b}}}$}'
        >>> modern_nodes_str("(N, lit:PHI1 , ftr:[+??????--], up:3, dn:0,"),
        '\\texttt{(N, lit:${\\phi_{\\textrm{1}}}$, ftr:[+??????--], up:3, dn:0,}'
    """
    # Match colon-prefixed substrings not containing square brackets
    # Matches content after ':' until ',' or ')' but skips '[' and ']'
    pattern = r'(?<=:)([^,\)\[\]]+)'
    def replace(match):
        token = match.group(1).strip()
        return modern_token(token, code=False)
    # Perform replacements using the existing modern_token function
    s = re.sub(pattern, replace, s)
    # Apply \texttt style and return answer.
    return f"\\texttt{{{s}}}"

def modern_interp(interp: str, bold: bool = False, code: bool = False) -> str:
    """Convert an interpretation (multiple chains) to LaTeX, using \qquad as separator.
    
    Args:
        interp (str): String of chains joined by "~~~~"
        
    Returns:
        str: LaTeX string with each chain converted and rejoined by "\\qquad "
        bold (bool): Whether to apply \textbf style
        code (bool): Whether to apply \texttt style
        
    Examples:
        >>> modern_interp("PHI1A\\symbol{94}interestB")
        '${\\phi_{\\textrm{1a}}}$\\symbol{94}${\\textrm{interest}_{\\textrm{b}}}$'
        >>> modern_interp("gamblersA\\qquad PHI1")
        '${\\texttt{gamblers}_{a}}$\\qquad ${\\phi_{1}}$'
    """
    # Special case "NONE", meaning no interpretations were found.
    if interp == "NONE":
        return interp
    # Split interp into chains
    chains = interp.split("~~~~")
    # Convert each chain to LaTeX
    modern_chains = [modern_chain(chain, bold=bold, code=code) for chain in chains]
    # Join back together with \qquad
    answer = "\\qquad ".join(modern_chains)
    return answer

def modern_chain(chain: str, bold: bool = False, code: bool = False) -> str:
    """Convert a chain of tokens to LaTeX, using \symbol{94} as separator.
    
    Args:
        chain (str): String of tokens joined by \symbol{94}
        
    Returns:
        str: LaTeX string with each token converted and rejoined
        bold (bool): Whether to apply \textbf style
        code (bool): Whether to apply \texttt style
        
    Examples:
        >>> modern_chain("PHI1A\\symbol{94}interestB")
        '${\\phi_{1a}}$\\symbol{94}${\\texttt{interest}_{b}}$'
        >>> modern_chain("12B\\symbol{94}PHI2")
        '${\\texttt{12}_{b}}$\\symbol{94}${\\phi_{2}}$'
    """
    # Split chain into tokens
    hat = "\\symbol{94}"
    tokens = chain.split(hat)
    # Convert each token to LaTeX
    modern_tokens = [modern_token(token, bold=bold, code=code) for token in tokens]
    # Apply code style to base if requested
    if code:
        hat = f"\\texttt{{{hat}}}"
    # Apply bold style to base and subscript if requested
    if bold:
        hat = f"\\textbf{{{hat}}}"
    # Join back together with hat
    return hat.join(modern_tokens)

def modern_short_label(node: Node, bold: bool = False, code: bool = False) -> str:
    """Convert a Node's short label to LaTeX with optional styling.
    
    Args:
        node (Node): Node whose short label to convert
        bold (bool): Whether to apply \textbf style
        code (bool): Whether to apply \texttt style to base
        
    Returns:
        str: LaTeX math string for node's short label
    """
    return modern_token(view_short_label(node), bold=bold, code=code)

def modern_token(token: str, bold: bool = False, code: bool = False) -> str:
    """Convert token to LaTeX math with optional bold and code styling.
    
    Args:
        token (str): Input string to convert
        bold (bool): Whether to apply \textbf style to base and subscript
        code (bool): Whether to apply \texttt style to base
        
    Returns:
        str: LaTeX math string
        
    Examples:
        >>> modern_token("gamblers")
        'gamblers'
        >>> modern_token("gamblersD")
        '${\\textrm{gamblers}_{\\textrm{d}}}$'
        >>> modern_token("gamblersD", code=True)
        '${\\texttt{gamblers}_{\\texttt{d}}}$'
        >>> modern_token("interest", bold=True)
        '\\textbf{interest}'
        >>> modern_token("interestA", bold=True)
        '${\\textbf{\\textrm{interest}}_{\\textbf{\\textrm{a}}}}$'
        >>> modern_token("PHI")
        '$\\phi$'
        >>> modern_token("PHI1A")
        '${\\phi_{\\textrm{1a}}}$'
        >>> modern_token("PHI1A", bold=True, code=True)
        '${\\bm{\\phi}_{\\textbf{\\texttt{1a}}}}$'
    """
    # Special case empty string
    if token == "":
        return ""
    # Split token into base and subscript
    base, subscript = modern_base_subscript(token)
    # Convert PHI to phi if present
    if base == "PHI":
        base = "\\phi"
    # Make subscript lowercase
    subscript = subscript.lower()
    # Use math mode?
    math = (base == "\\phi") or (subscript != "")
    # Apply code style to base if requested
    if code:
        style = "\\texttt"
    elif math:
        style = "\\textrm"
    else:
        style = ""
    if style != "":
        if base != "\\phi":
            base = f"{style}{{{base}}}"
        if subscript:
            subscript = f"{style}{{{subscript}}}"
    # Apply bold style to base and subscript if requested
    if bold:
        if base == "\\phi":
            base = f"\\bm{{{base}}}"
        else:
            base = f"\\textbf{{{base}}}"
        if subscript:
            subscript = f"\\textbf{{{subscript}}}"
    # Return final LaTeX math string
    if not math:
        return base
    elif not subscript:
        return f"${base}$"
    else:
        return f"${{{base}_{{{subscript}}}}}$"

def modern_token_width(token: str) -> float:
    """Calculate the display width of a token when rendered in LaTeX.
    
    Width is calculated as base width plus subscript width divided by 1.2.
    
    Args:
        token (str): Input string to measure
        
    Returns:
        float: Estimated display width when rendered
        
    Examples:
        >>> modern_token_width("PHI1A")  # \phi width + ("1A" width / 1.2)
        >>> modern_token_width("12B")    # "12" width + ("B" width / 1.2)
        >>> modern_token_width("test2A") # "test" width + ("2A" width / 1.2)
    """
    base, subscript = modern_base_subscript(token)
    if base == "PHI":
        # When finally rendered into LaTeX, the width of "\phi" isn't
        # very different from "p", but our tex_str_width doesn't
        # handle "\phi".  Substitute "p" as an acceptable workaround.
        base = "p"
    return tex_str_width(base) + (tex_str_width(subscript) / 1.2)

def modern_base_subscript(token: str) -> list[str]:
    """Split a token into [base, subscript] components where token == base + subscript.
    
    Args:
        token (str): Input string to split
        
    Returns:
        list[str]: [base, subscript] where token == base + subscript
        
    Examples:
        >>> modern_base_subscript("PHI1A")
        ["PHI", "1A"]
        >>> modern_base_subscript("interestA")
        ["interest", "A"]
        >>> modern_base_subscript("gamblersD")
        ["gamblers", "D"]
        >>> modern_base_subscript("12B")
        ["12", "B"]
        >>> modern_base_subscript("x2")
        ["x", "2"]
        >>> modern_base_subscript("test2A")
        ["test", "2A"]
    """
    # Special case for PHI
    if token.startswith("PHI"):
        return ["PHI", token[3:]]
    # Initially set base to full token and empty subscript
    base = token
    subscript = ""
    # While base has more than 1 character and ends with capital letter or digit,
    # move that character to the front of subscript, BUT only move digits if
    # the base doesn't start with a digit
    while len(base) > 1:
        if base[-1].isupper():
            subscript = base[-1] + subscript
            base = base[:-1]
        elif base[-1].isdigit() and not base[0].isdigit():
            subscript = base[-1] + subscript
            base = base[:-1]
        else:
            break
    return [base, subscript]
