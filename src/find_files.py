################################################################
#
#    find_files.py
#
################################################################

"""Find files in a directory matching a given pattern.""" 

import os
from glob import glob

def find_files(directory: str, pattern: str = "*") -> list[str]:
    """Find files in a directory matching the given pattern.
    
    Args:
        directory (str): Path to the directory to search.
        pattern (str): Glob pattern to match files against. Defaults to "\\*".
                      Examples:
                      - "\\*.txt" for text files
                      - "\\*.py" for Python files
                      - "\\*\\*/\\*.md" for markdown files in all subdirectories
                      - "data\\_\\*.csv" for CSV files starting with "data\\_"
                      - "log_[0-9].txt" for log files with single digit
                      - "\\*.[tj]s" for JavaScript/TypeScript files
    
    Returns:
        list[str]: List of file paths matching the pattern.
    
    Raises:
        ValueError: If the directory doesn't exist or isn't accessible.
    """
    # Expand user directory if needed (e.g., "~/documents")
    directory = os.path.expanduser(directory)
    # Convert to absolute path
    abs_dir = os.path.abspath(directory)
    # Verify directory exists and is accessible
    if not os.path.isdir(abs_dir):
        raise ValueError(f"The directory {directory} does not exist or is not accessible.")
    # Construct the full pattern path
    pattern_path = os.path.join(abs_dir, pattern)
    # Use glob to find matching files
    matches = glob(pattern_path, recursive=True)
    # Filter to ensure we only return files (not directories)
    return [path for path in matches if os.path.isfile(path)]
