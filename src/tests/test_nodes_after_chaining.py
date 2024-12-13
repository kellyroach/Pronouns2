################################################################
#
#    test_nodes_after_chaining.py
#
################################################################

from unittest import TestCase
from tests.utils.run_test_doc import *
from pronouns2 import *

def run_test_nodes_after_chaining(file: str, **kwargs) -> None:
    """Shared subroutine for testing demo_write_nodes_after_chaining.

    Args:
        file (str): File name.
    """
    kwargs.update({'info': True,
                   'features_table': False,
                   'abstract_diagram': False,
                   'nodes_after_chaining': True,
                   'nodes_table': True,
                   'chaining_diagram': False,
                   'chaining_table': False,
                   'interpretations_table': False,
                   'summary_table': False,
                   'lexicon_table': False,
                   'debug': False,
                   'trace': False})
    run_test_doc(file=file, **kwargs)

class TestNodesAfterChaining(TestCase):
    def test_nodes_after_chaining_txt(self):
        """Test doc with file_type=FileType.TXT."""
        run_test_nodes_after_chaining(file="test_nodes_after_chaining.txt", file_type=FileType.TXT)
    def test_nodes_after_chaining_tex(self):
        """Test doc with file_type=FileType.TEX."""
        run_test_nodes_after_chaining(file="test_nodes_after_chaining.tex", file_type=FileType.TEX)
