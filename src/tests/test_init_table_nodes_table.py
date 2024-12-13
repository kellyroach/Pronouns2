################################################################
#
#    test_init_table_nodes_table.py
#
################################################################

from unittest import TestCase
from tests.utils.run_test_doc import *
from pronouns2 import *

def run_test_init_table_nodes_table(file: str, **kwargs) -> None:
    """Shared subroutine for testing init_table table_proc_write_nodes_table.

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
                   'nodes_after_parse': False,
                   'init_table': True,
                   'new_chain': False,
                   'trace': False})
    run_test_doc(file=file, **kwargs)

class TestInitTableNodesTable(TestCase):
    def test_init_table_nodes_table_txt(self):
        """Test doc with file_type=FileType.TXT."""
        run_test_init_table_nodes_table(file="test_init_table_nodes_table.txt",
                                        file_type=FileType.TXT)
    def test_init_table_nodes_table_tex(self):
        """Test doc with file_type=FileType.TEX."""
        run_test_init_table_nodes_table(file="test_init_table_nodes_table.tex",
                                        file_type=FileType.TEX)
