################################################################
#
#    tex.py
#
################################################################

"""TeX-related utility functions such as measuring string widths.""" 

from pathlib import Path
from enum import Enum

TEX_LINE_HEIGHT = 0.39051

# Global dictionary to store character widths
tex_char_widths = {}

# character width_data in points, gathered from pdflatex
def tex_init():
    """Initialize the character width lookup table with predefined measurements."""
    global tex_char_widths
    # Dictionary mapping characters to their CMR10 LaTeX widths
    width_data = {
        ' ': 5.2778, '!': 2.77779, '"': 5.00002, '#': 8.33336,
        '%': 8.33336, '&': 7.7778, '\'': 2.77779, ')': 3.8889,
        '*': 5.00002, '+': 7.7778, ',': 2.77779, '-': 3.33333,
        '.': 2.77779, '/': 5.00002, '0': 5.00002, '1': 5.00002,
        '2': 5.00002, '3': 5.00002, '4': 5.00002, '5': 5.00002,
        '6': 5.00002, '7': 5.00002, '8': 5.00002, '9': 5.00002,
        ':': 2.77779, ';': 2.77779, '<': 2.77779, '=': 7.7778,
        '>': 4.72223, '?': 4.72223, '@': 7.7778, 'A': 7.50002,
        'B': 7.08336, 'C': 7.22223, 'D': 7.6389, 'E': 6.80557,
        'F': 6.5278, 'G': 7.84723, 'H': 7.50002, 'I': 3.61111,
        'J': 5.1389, 'K': 7.7778, 'L': 6.25002, 'M': 9.16669,
        'N': 7.50002, 'O': 7.7778, 'P': 6.80557, 'Q': 7.7778,
        'R': 7.36111, 'S': 5.55557, 'T': 7.22223, 'U': 7.50002,
        'V': 7.50002, 'W': 10.2778, 'X': 7.50002, 'Y': 7.50002,
        'Z': 6.11111, '[': 2.77779, '\\': 5.00002, ']': 2.77779,
        '^': 5.00002, '_': 3.6, '`': 2.77779, 'a': 5.00002,
        'b': 5.55557, 'c': 4.44444, 'd': 5.55557, 'e': 4.44444,
        'f': 3.05557, 'g': 5.00002, 'h': 5.55557, 'i': 2.77779,
        'j': 3.05557, 'k': 5.2778, 'l': 2.77779, 'm': 8.33336,
        'n': 5.55557, 'o': 5.00002, 'p': 5.55557, 'q': 5.27779,
        'r': 3.91667, 's': 3.94444, 't': 3.8889, 'u': 5.55557,
        'v': 5.2778, 'w': 7.22223, 'x': 5.2778, 'y': 5.2778,
        'z': 4.44444, '{': 5.00002, '|': 10.00002, '~': 5.2778,
        '}': 5.00002
    }
    tex_char_widths.update(width_data)

# In centimeters, friendly to Tikz .  OW, a \texttt char
# would be 5pt x 11.1111pt .
# The approximate conversion is 1 point = 0.035146 cm .
def tex_char_width(char: str) -> float:
    """
    Get the width of a single character in LaTeX units.
    
    Args:
        char: A single character
    Returns:
        The width of the character
    Raises:
        ValueError: If char is not a single character
        KeyError: If char width is not known
    """
    if len(char) != 1:
        raise ValueError("Input must be a single character")
    return 0.035146 * tex_char_widths[char]

def tex_str_width(s: str) -> float:
    """Calculates the total width of a string in LaTeX units by
    summing predefined character widths, used for spacing in
    TikZ-CD diagrams.

    Args:
        s (str): Input string to measure
    Returns:
        float: Width of string in centimeters (approximately 0.035146 cm per point)
    Raises:
        TypeError: If input is not a string
        ValueError: If string contains characters with unknown widths
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    try:
        total_width = sum(tex_char_width(c) for c in s)
    except KeyError as e:
        raise ValueError(f"Illegal character in string: {e}")
    return total_width

class TexMode(Enum):
    TEXT = "text"
    CODE = "code"
    MATH = "math"

TEX_ESCAPE_MAP = {
    TexMode.TEXT: {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}',
        '\\': r'\textbackslash{}',
    },
    TexMode.CODE: {
        ' ': '~',
        '&': r'\symbol{38}',
        '%': r'\symbol{37}',
        '$': r'\symbol{36}',
        '#': r'\symbol{35}',
        '_': r'\symbol{95}',
        '{': r'\symbol{123}',
        '}': r'\symbol{125}',
        '~': r'\symbol{126}',
        '^': r'\symbol{94}',
        '\\': r'\symbol{92}',
    },
    TexMode.MATH: {
        '&': r'\text{\&}',
        '%': r'\text{\%}',
        '$': r'\text{\$}',
        '#': r'\text{\#}',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\text{\textasciitilde{}}',
        '^': r'\text{\textasciicircum{}}',
        '\\': r'\backslash',
    }
}

def tex_escape_file(input_file: str,
                    output_file: str,
                    mode: TexMode = TexMode.TEXT,
                    use_symbol: bool = False) -> None:
    """Applies tex_escape_str to every line of the input file and writes to output file.

    Args:
        input_file (str): Path to the input file to process.
        output_file (str): Path to write the processed output.
        mode (TexMode): Output mode (TexMode.TEXT, TexMode.CODE,
        TexMode.MATH). Defaults to TexMode.TEXT.
        use_symbol (bool): Whether to prefer `\\symbol` syntax. Defaults to False.
    """
    try:
        # Convert output_file to Path object for directory creation
        output_path = Path(output_file)
        # Create output directory if it doesn't exist
        output_path.parent.mkdir(parents=True, exist_ok=True)
        # Read all lines from the input file
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        # Apply tex_escape_str to each line
        escaped_lines = [tex_escape_str(line.rstrip('\n'),
                                      mode=mode,
                                      use_symbol=use_symbol)
                        for line in lines]
        # Write processed content to output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(escaped_lines) + '\n')
    except Exception as e:
        raise IOError(f"Error processing files - Input: {input_file}, Output: {output_file}: {e}")

def tex_escape_str(element: str, mode: TexMode = TexMode.TEXT, use_symbol: bool = False) -> str:
    """Converts TXT-biased element to a TeX-safe string based on mode.

    Args:
        element (str): Input string to convert.
        mode (TexMode): Output mode (TexMode.TEXT, TexMode.CODE,
        TexMode.MATH). Defaults to TexMode.TEXT.
        use_symbol (bool): Whether to prefer `\symbol` syntax. Defaults to False.

    Returns:
        str: TeX-compatible string.
    """
    if mode not in TEX_ESCAPE_MAP:
        raise ValueError(f"Unsupported mode: {mode}. Supported modes are: {list(TexMode)}.")
    escape_map = TEX_ESCAPE_MAP[mode]
    if use_symbol and (mode != TexMode.CODE):
        # Dynamically replace escape_map with \symbol syntax for all characters.
        escape_map = {char: f"\\symbol{{{ord(char)}}}" for char in escape_map}
    return ''.join(escape_map.get(char, char) for char in element)

def tex_code(element: str) -> str:
    """Converts TXT-biased element to a TexMode.CODE TeX-safe string.

    Args:
        element (str): Input string to convert.

    Returns:
        str: TeX-compatible string.
    """
    return tex_escape_str(element, TexMode.CODE)

tex_init()
