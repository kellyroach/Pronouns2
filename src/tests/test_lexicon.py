################################################################
#
#    test_lexicon.py
#
################################################################

from unittest import TestCase
from pronouns2 import *

class TestLexicon(TestCase):
    def test_lexicon(self):
        """Test lexicon.py functions."""
        self.assertEqual(lexicon_select("++---?++-"),
                         ['myself'])
        self.assertEqual(lexicon_select("++---?+-+"),
                         ['mine', 'my'])
        self.assertEqual(lexicon_select("++--+?+--"),
                         ['PHI', 'us', 'we'])
        self.assertTrue(isinstance(lexicon_lookup("June's"),Node))
        self.assertTrue(isinstance(lexicon_lookup("boys"),Node))
        self.assertTrue(isinstance(lexicon_lookup("boys'"),Node))
        self.assertTrue(isinstance(lexicon_lookup("mosquitoes'"),Node))
        self.assertEqual(lexicon_select('+--+??+--'),
                         ['PHI', 'all', 'another', 'any',
                         'each', 'he', 'her', 'him', 'none',
                         'one', 'oneself', 'other', 'she',
                         'some', 'somebody', 'that', 'them',
                         'these', 'they', 'this', 'those',
                         'what', 'which', 'who', 'whom'])
        self.assertEqual(lexicon_select('mom'),
                         ['Anna', 'Janet', 'Jill', 'June',
                         'Linda', 'Mary', 'Penelope', 'Sandy',
                         'Sue', 'asshole', 'aunt', 'blame',
                         'camel', 'cat', 'daughter',
                         'embezzler', 'fish', 'gambler', 'girl',
                         'grandmother', 'mosquito', 'mom',
                         'mother', 'neighbor', 'pig', 'pilot',
                         'sheep', 'sister', 'student', 'toy'])




