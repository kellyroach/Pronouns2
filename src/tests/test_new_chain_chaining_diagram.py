################################################################
#
#    test_new_chain_chaining_diagram.py
#
################################################################

from unittest import TestCase
from tests.utils.run_test_doc import *
from pronouns2 import *

def run_test_new_chain_chaining_diagram(file: str, **kwargs) -> None:
    """Shared subroutine for testing new_chain table_proc_write_chaining_diagram.

    Args:
        file (str): File name.
    """
    kwargs.update({'info': False,
                   'features_table': False,
                   'abstract_diagram': False,
                   'nodes_after_chaining': False,
                   'nodes_table': False,
                   'chaining_diagram': True,
                   'chaining_table': False,
                   'interpretations_table': False,
                   'summary_table': False,
                   'lexicon_table': False,
                   'debug': True,
                   'nodes_after_parse': False,
                   'init_table': False,
                   'new_chain': True})
    run_test_doc(file=file, **kwargs)

class TestNewChainChainingTable(TestCase):
    def test_new_chain_chaining_diagram(self):
        """Test doc with file_type=FileType.TEX, trace=False."""
        run_test_new_chain_chaining_diagram(file="test_new_chain_chaining_diagram.tex",
                                            file_type=FileType.TEX,
                                            trace=False)
    def test_new_chain_chaining_diagram_trace(self):
        """Test doc with file_type=FileType.TEX, trace=False."""
        run_test_new_chain_chaining_diagram(file="test_new_chain_chaining_diagram_trace.tex",
                                            file_type=FileType.TEX,
                                            trace=True)
