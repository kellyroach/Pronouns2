################################################################
#
#    test_trc.py
#
################################################################

import os
from pathlib import Path
from unittest import TestCase
from pronouns2 import *

def fib(n: int) -> int:
    """Compute the nth Fibonacci number recursively, instrumented with tracing."""
    trc_enter(f"fib({n})")
    if n <= 1:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)
    trc_exit(f"fib({n}) = {result}")
    return result

def run_test_trc(file: str, file_type: FileType) -> None:
    """Shared subroutine for testing Fibonacci tracing output.

    Args:
        file (str): File name.
        file_type (FileType): File type to be used for tracing output (TXT or TEX).
    """
    # File paths
    base_dir = Path("tests")
    output_dir = base_dir / "output"
    expected_dir = base_dir / "expected"
    output_dir.mkdir(parents=True, exist_ok=True)
    expected_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / file
    expected_file = expected_dir / file
    # Redirect Manager to output file
    with open(output_file, "w", encoding="utf-8") as stream:
        with Manager.manager:
            # Update the state of the singleton Manager
            Manager.set_state(file_type=file_type, stream=stream)
            trc(True)  # Enable tracing
            fib(5)  # Compute Fibonacci(5) with tracing
            trc_end()  # Ensure trace output is closed properly
    # Compare the generated output with the expected output
    with open(output_file, "r", encoding="utf-8") as out, open(expected_file, "r", encoding="utf-8") as exp:
        output_content = out.read()
        expected_content = exp.read()
    # Assert that the generated content matches the expected content
    assert output_content == expected_content, (
        f"({output_file}) does not match ({expected_file})."
    )

class TestTrc(TestCase):
    def test_trc_txt(self):
        """Test tracing Fibonacci to TXT file."""
        run_test_trc(file="test_trc.txt", file_type=FileType.TXT)
    def test_trc_tex(self):
        """Test tracing Fibonacci to TEX file."""
        run_test_trc(file="test_trc_tex.txt", file_type=FileType.TEX)
