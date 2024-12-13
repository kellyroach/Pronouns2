################################################################
#
#    test_lexicon_table.py
#
################################################################

from unittest import TestCase
from tests.utils.run_test_doc import *
from pronouns2 import *

def run_test_lexicon_table(file: str, **kwargs) -> None:
    """Shared subroutine for testing demo_write_lexicon_table.

    Args:
        file (str): File name.
    """
    kwargs.update({'info': True,
                   'features_table': False,
                   'abstract_diagram': False,
                   'nodes_after_chaining': False,
                   'nodes_table': False,
                   'chaining_diagram': False,
                   'chaining_table': False,
                   'interpretations_table': False,
                   'summary_table': False,
                   'lexicon_table': True,
                   'debug': False,
                   'trace': False})
    run_test_doc(file=file, **kwargs)

class TestLexiconTable(TestCase):
    def test_lexicon_table_txt(self):
        """Test doc with file_type=FileType.TXT."""
        run_test_lexicon_table(file="test_lexicon_table.txt", file_type=FileType.TXT)
    def test_lexicon_table_tex(self):
        """Test doc with file_type=FileType.TEX."""
        run_test_lexicon_table(file="test_lexicon_table.tex", file_type=FileType.TEX)
