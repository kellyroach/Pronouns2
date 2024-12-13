################################################################
#
#    test_new_chain_nodes_table.py
#
################################################################

from unittest import TestCase
from tests.utils.run_test_doc import *
from pronouns2 import *

def run_test_new_chain_nodes_table(file: str, **kwargs) -> None:
    """Shared subroutine for testing new_chain table_proc_write_nodes_table.

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
                   'inittable': False,
                   'new_chain': True})
    run_test_doc(file=file, **kwargs)

class TestInitTableNodesTable(TestCase):
    def test_new_chain_nodes_table_txt(self):
        """Test doc with file_type=FileType.TXT, trace=False."""
        run_test_new_chain_nodes_table(file="test_new_chain_nodes_table.txt",
                                       file_type=FileType.TXT,
                                       trace=False)
    def test_new_chain_nodes_table_tex(self):
        """Test doc with file_type=FileType.TEX, trace=False."""
        run_test_new_chain_nodes_table(file="test_new_chain_nodes_table.tex",
                                       file_type=FileType.TEX,
                                       trace=False)
    def test_new_chain_nodes_table_txt(self):
        """Test doc with file_type=FileType.TXT, trace=True."""
        run_test_new_chain_nodes_table(file="test_new_chain_nodes_table_trace.txt",
                                       file_type=FileType.TXT,
                                       trace=True)
    def test_new_chain_nodes_table_tex(self):
        """Test doc with file_type=FileType.TEX, trace=True."""
        run_test_new_chain_nodes_table(file="test_new_chain_nodes_table_trace.tex",
                                       file_type=FileType.TEX,
                                       trace=True)
