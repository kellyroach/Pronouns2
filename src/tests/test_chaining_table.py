################################################################
#
#    test_chaining_table.py
#
################################################################

from unittest import TestCase
from tests.utils.run_test_doc import *
from pronouns2 import *

def run_test_chaining_table(file: str, **kwargs) -> None:
    """Shared subroutine for testing demo_write_chaining_table.

    Args:
        file (str): File name.
    """
    kwargs.update({'info': True,
                   'features_table': False,
                   'abstract_diagram': False,
                   'nodes_after_chaining': False,
                   'nodes_table': False,
                   'chaining_diagram': False,
                   'chaining_table': True,
                   'interpretations_table': False,
                   'summary_table': False,
                   'lexicon_table': False,
                   'trace': False})
    run_test_doc(file=file, **kwargs)

class TestChainingTable(TestCase):
    def test_chaining_table_txt(self):
        """Test chaining_table for file_type=FileType.TXT, info=True, debug=False."""
        run_test_chaining_table(file="test_chaining_table.txt", file_type=FileType.TXT, debug=False)
    def test_chaining_table_debug_txt(self):
        """Test chaining_table for file_type=FileType.TXT, info=True, debug=True."""
        run_test_chaining_table(file="test_chaining_table_debug.txt", file_type=FileType.TXT, debug=True)
    def test_chaining_table_tex(self):
        """Test chaining_table for file_type=FileType.TEX, info=True, debug=False."""
        run_test_chaining_table(file="test_chaining_table.tex", file_type=FileType.TEX, debug=False)
    def test_chaining_table_debug_tex(self):
        """Test chaining_table for file_type=FileType.TEX, info=True, debug=True."""
        run_test_chaining_table(file="test_chaining_table_debug.tex", file_type=FileType.TEX, debug=True)


