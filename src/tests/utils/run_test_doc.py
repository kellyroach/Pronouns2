################################################################
#
#    run_test_doc.py
#
################################################################

import os
from pathlib import Path
from unittest import TestCase
from pronouns2 import *

def run_test_doc(numbers = None, file: str = "test_doc", **kwargs) -> None:
    """Shared subroutine for testing function doc.

    Args:
        numbers (optional): None, str, or list[str] of keys in example_dict
        file (str, optional): File name. Defaults to "test_doc".
    """
    # File paths
    tests_dir = Path("tests")
    output_dir = tests_dir / "output"
    expected_dir = tests_dir / "expected"
    output_dir.mkdir(parents=True, exist_ok=True)
    expected_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / file
    expected_file = expected_dir / file
    # Generate output_file using function doc .
    doc(numbers=numbers, file=output_file, **kwargs)
    # Compare the generated output with the expected output
    with open(output_file, "r", encoding="utf-8") as out:
        with open(expected_file, "r", encoding="utf-8") as exp:
            output_content = out.read()
            expected_content = exp.read()
    # Assert that the generated content matches the expected content
    assert output_content == expected_content, \
        f"Content mismatch:\nOutput file: {output_file}\nExpected file: {expected_file}"
