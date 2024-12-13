################################################################
#
#    test_doc_10p1.py
#
################################################################

from unittest import TestCase
from tests.utils.run_test_doc import *
from pronouns2 import *

class TestDoc10p1(TestCase):
    def test_doc_txt(self):
        """Test doc with file_type=FileType.TXT."""
        run_test_doc("10.1", file="test_doc_10p1.txt", file_type=FileType.TXT, info=True)
    def test_doc_tex(self):
        """Test doc with file_type=FileType.TEX."""
        run_test_doc("10.1", file="test_doc_10p1.tex", file_type=FileType.TEX, info=True)
    def test_doc_debug_txt(self):
        """Test doc with file_type=FileType.TXT, debug=True."""
        run_test_doc("10.1", file="test_doc_debug_10p1.txt", file_type=FileType.TXT, info=True, debug=True)
    def test_doc_debug_tex(self):
        """Test doc with file_type=FileType.TEX, debug=True."""
        run_test_doc("10.1", file="test_doc_debug_10p1.tex", file_type=FileType.TEX, info=True, debug=True)
    def test_doc_debug_trace_txt(self):
        """Test doc with file_type=FileType.TXT, debug=True, trace=True."""
        run_test_doc("10.1", file="test_doc_debug_trace_10p1.txt", file_type=FileType.TXT, info=True, debug=True, trace=True)
    def test_doc_debug_trace_tex(self):
        """Test doc with file_type=FileType.TEX, debug=True, trace=True."""
        run_test_doc("10.1", file="test_doc_debug_trace_10p1.tex", file_type=FileType.TEX, info=True, debug=True, trace=True)
