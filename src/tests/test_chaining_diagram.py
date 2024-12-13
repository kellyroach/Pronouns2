################################################################
#
#    test_chaining_diagram.py
#
################################################################

from unittest import TestCase
from tests.utils.run_test_doc import *
from pronouns2 import *

def run_test_chaining_diagram(file: str, **kwargs) -> None:
    """Shared subroutine for testing chaining_diagram.

    Args:
        file (str): File name.
    """
    kwargs.update({'file_type': FileType.TEX,
                   'info': True,
                   'features_table': False,
                   'abstract_diagram': False,
                   'nodes_after_chaining': False,
                   'nodes_table': False,
                   'chaining_diagram': True,
                   'chaining_table': False,
                   'interpretations_table': False,
                   'summary_table': False,
                   'lexicon_table': False,
                   'trace': False})
    run_test_doc(file=file, **kwargs)

class TestChainingDiagram(TestCase):
    def test_chaining_diagram(self):
        """Test chaining_diagram for info=True, debug=False."""
        run_test_chaining_diagram(file="test_chaining_diagram.tex", debug=False)
    def test_chaining_diagram_debug(self):
        """Test chaining_diagram for info=True, debug=True."""
        run_test_chaining_diagram(file="test_chaining_diagram_debug.tex", debug=True)
