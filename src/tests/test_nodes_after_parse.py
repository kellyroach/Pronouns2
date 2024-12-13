################################################################
#
#    test_nodes_after_parse.py
#
################################################################

from unittest import TestCase
from tests.utils.run_test_doc import *
from pronouns2 import *

def run_test_nodes_after_parse(file: str, **kwargs) -> None:
    """Shared subroutine for testing demo_write_nodes_after_chaining.

    Args:
        file (str): File name.
    """
    kwargs.update({'info': True,
                   'features_table': False,
                   'abstract_diagram': False,
                   'nodes_after_chaining': False,
                   'nodes_table': True,
                   'chaining_diagram': False,
                   'chaining_table': False,
                   'interpretations_table': False,
                   'summary_table': False,
                   'lexicon_table': False,
                   'debug': True,
                   'nodes_after_parse': True,
                   'init_table': False,
                   'new_chain': False,
                   'trace': False})
    run_test_doc(file=file, **kwargs)

class TestNodesAfterParse(TestCase):
    def test_nodes_after_parse_txt(self):
        """Test doc with file_type=FileType.TXT."""
        run_test_nodes_after_parse(file="test_nodes_after_parse.txt", file_type=FileType.TXT)
    def test_nodes_after_parse_tex(self):
        """Test doc with file_type=FileType.TEX."""
        run_test_nodes_after_parse(file="test_nodes_after_parse.tex", file_type=FileType.TEX)
