################################################################
#
#    test_trace.py
#
################################################################

from unittest import TestCase
from tests.utils.run_test_doc import *
from pronouns2 import *

def run_test_trace(file: str, **kwargs) -> None:
    """Shared subroutine for testing trace.

    Args:
        file (str): File name.
    """
    kwargs.update({'info': False,
                   'debug': False,
                   'trace': True})
    run_test_doc(file=file, **kwargs)

class TestTrace(TestCase):
    def test_trace_txt(self):
        """Test doc with file_type=FileType.TXT."""
        run_test_trace(file="test_trace.txt", file_type=FileType.TXT)
    def test_trace_tex(self):
        """Test doc with file_type=FileType.TEX."""
        run_test_trace(file="test_trace.tex", file_type=FileType.TEX)
