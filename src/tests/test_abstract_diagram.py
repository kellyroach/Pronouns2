################################################################
#
#    test_abstract_diagram.py
#
################################################################

from unittest import TestCase
from tests.utils.run_test_doc import *
from pronouns2 import *

def run_test_abstract_diagram(file: str, **kwargs) -> None:
    """Shared subroutine for testing demo_write_abstract_diagram.

    Args:
        file (str): File name.
    """
    kwargs.update({'info': True,
                   'features_table': False,
                   'abstract_diagram': True,
                   'nodes_after_chaining': False,
                   'nodes_table': False,
                   'chaining_diagram': False,
                   'chaining_table': False,
                   'interpretations_table': False,
                   'summary_table': False,
                   'lexicon_table': False,
                   'debug': False,
                   'trace': False})
    run_test_doc(file=file, **kwargs)

class TestAbstractDiagram(TestCase):
    def test_abstract_diagram_tex(self):
        """Test doc with file_type=FileType.TEX."""
        run_test_abstract_diagram(file="test_abstract_diagram.tex", file_type=FileType.TEX)
