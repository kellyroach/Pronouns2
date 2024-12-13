################################################################
#
#    test_features_table.py
#
################################################################

from unittest import TestCase
from tests.utils.run_test_doc import *
from pronouns2 import *

def run_test_features_table(file: str, **kwargs) -> None:
    """Shared subroutine for testing demo_write_features_table.

    Args:
        file (str): File name.
    """
    kwargs.update({'info': True,
                   'features_table': True,
                   'abstract_diagram': False,
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

class TestFeaturesTable(TestCase):
    def test_features_table_txt(self):
        """Test doc with file_type=FileType.TXT."""
        run_test_features_table(file="test_features_table.txt", file_type=FileType.TXT)
    def test_features_table_tex(self):
        """Test doc with file_type=FileType.TEX."""
        run_test_features_table(file="test_features_table.tex", file_type=FileType.TEX)
