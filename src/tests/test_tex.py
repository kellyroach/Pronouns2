################################################################
#
#    test_tex.py
#
################################################################

import os
from pathlib import Path
from unittest import TestCase
from pronouns2 import *

def run_test_tex_file() -> None:
    """Subroutine for testing function tex_escape_file."""
    # File paths
    input_dir = Path(".")
    input_name = "globals.py"
    input_file = input_dir / input_name
    tests_dir = Path("tests")
    output_dir = tests_dir / "output"
    expected_dir = tests_dir / "expected"
    # Create test directories
    output_dir.mkdir(parents=True, exist_ok=True)
    expected_dir.mkdir(parents=True, exist_ok=True)
    # Define output and expected files
    output_name = "globals.txt"
    output_file = output_dir / output_name
    expected_file = expected_dir / output_name
    # Generate output_file using function tex_escape_file
    tex_escape_file(input_file, output_file, TexMode.CODE)
    # Compare the generated output with the expected output
    with open(output_file, "r", encoding="utf-8") as out, \
         open(expected_file, "r", encoding="utf-8") as exp:
        output_content = out.read()
        expected_content = exp.read()
    # Assert that the generated content matches the expected content
    if output_content != expected_content:
        print("")
        print("################################################################")
        print("# NOTE: 'FAIL: test_tex_file (test_tex.TestTexEscape)' is usually")
        print("# caused by code changes to globals.py.  If test_tex_file is operating")
        print("# correctly, just update src/tests/expected/globals.txt to match")
        print("# src/tests/output/globals.txt.  Then test_tex_file will pass again.")
        print("################################################################")
    assert output_content == expected_content, \
        f"Content mismatch:\nOutput file: {output_file}\nExpected file: {expected_file}"

class TestTexEscape(TestCase):
    def test_tex_file(self):
        """Test doc with mode=TexMode.CODE."""
        run_test_tex_file()

    def test_tex_escape_str_text(self):
        """Test tex_escape_str in TEXT mode."""
        self.assertEqual(tex_escape_str("Hello & % world!", mode=TexMode.TEXT), "Hello \\& \\% world!")
        self.assertEqual(tex_escape_str("Line with $pecial characters #", mode=TexMode.TEXT), "Line with \\$pecial characters \\#")
        self.assertEqual(tex_escape_str("Plain text", mode=TexMode.TEXT), "Plain text")

    def test_tex_escape_str_code(self):
        """Test tex_escape_str in CODE mode."""
        self.assertEqual(tex_escape_str("Hello & % world!", mode=TexMode.CODE), 'Hello~\\symbol{38}~\\symbol{37}~world!')
        self.assertEqual(tex_escape_str("Code with $peculiar chars #", mode=TexMode.CODE), 'Code~with~\\symbol{36}peculiar~chars~\\symbol{35}')
        self.assertEqual(tex_escape_str(" ", mode=TexMode.CODE), "~")  # Check space mapping

    def test_tex_escape_str_math(self):
        """Test tex_escape_str in MATH mode."""
        self.assertEqual(tex_escape_str("Math & symbols $ #", mode=TexMode.MATH), "Math \\text{\\&} symbols \\text{\\$} \\text{\\#}")
        self.assertEqual(tex_escape_str("2 < 3 & 4 > 1", mode=TexMode.MATH), "2 < 3 \\text{\\&} 4 > 1")

    def test_tex_escape_str_use_symbol(self):
        """Test tex_escape_str with use_symbol=True."""
        self.assertEqual(tex_escape_str("Special % characters", mode=TexMode.TEXT, use_symbol=True), "Special \\symbol{37} characters")
        self.assertEqual(tex_escape_str("Dollar $ sign", mode=TexMode.CODE, use_symbol=True), 'Dollar~\\symbol{36}~sign')

    def test_tex_escape_str_edge_cases(self):
        """Test edge cases for tex_escape_str."""
        self.assertEqual(tex_escape_str("", mode=TexMode.TEXT), "")  # Empty string
        self.assertEqual(tex_escape_str("~ ^ \\ ", mode=TexMode.TEXT), "\\textasciitilde{} \\textasciicircum{} \\textbackslash{} ")
        self.assertEqual(tex_escape_str("Line\nBreak", mode=TexMode.TEXT), "Line\nBreak")  # Ensure newlines are preserved
