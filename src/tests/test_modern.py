################################################################
#
#    test_modern.py
#
################################################################

from unittest import TestCase
from pronouns2 import *

class TestModern(TestCase):
    def test_modern_token_width(self):
        self.assertAlmostEqual(modern_token_width("PHI"),
                               0.19525606322)
        self.assertAlmostEqual(modern_token_width("interest"),
                               1.1549379779)
        self.assertAlmostEqual(modern_token_width("PHI1A"),
                               0.56136140142)
        self.assertAlmostEqual(modern_token_width("interestA"),
                               1.3746010636666666)

    def test_modern_base_subscript(self):
        self.assertEqual(modern_base_subscript("PHI"),
                         ["PHI", ""])
        self.assertEqual(modern_base_subscript("interest"),
                         ["interest", ""])
        self.assertEqual(modern_base_subscript("PHI1A"),
                         ["PHI", "1A"])
        self.assertEqual(modern_base_subscript("interestA"),
                         ["interest", "A"])
        self.assertEqual(modern_base_subscript("gamblersD"),
                         ["gamblers", "D"])
        self.assertEqual(modern_base_subscript("12B"),
                         ["12", "B"])
        self.assertEqual(modern_base_subscript("x2"),
                         ["x", "2"])
        self.assertEqual(modern_base_subscript("test2A"),
                         ["test", "2A"])

    def test_modern_token(self):
        self.assertEqual(modern_token("gamblers"),
                         'gamblers')
        self.assertEqual(modern_token("gamblersD"),
                         '${\\textrm{gamblers}_{\\textrm{d}}}$')
        self.assertEqual(modern_token("gamblersD", code=True),
                         '${\\texttt{gamblers}_{\\texttt{d}}}$')
        self.assertEqual(modern_token("interest", bold=True),
                         '\\textbf{interest}')
        self.assertEqual(modern_token("interestA", bold=True),
                         '${\\textbf{\\textrm{interest}}_{\\textbf{\\textrm{a}}}}$')
        self.assertEqual(modern_token("PHI"),
                         '$\\phi$')
        self.assertEqual(modern_token("PHI1A"),
                         '${\\phi_{\\textrm{1a}}}$')
        self.assertEqual(modern_token("PHI1A", bold=True, code=True),
                         '${\\bm{\\phi}_{\\textbf{\\texttt{1a}}}}$')

    def test_modern_chain(self):
        self.assertEqual(modern_chain("PHI1A\\symbol{94}interestB"),
                         '${\\phi_{\\textrm{1a}}}$\\symbol{94}${\\textrm{interest}_{\\textrm{b}}}$')
        self.assertEqual(modern_chain("PHI1A\\symbol{94}interestB", bold=True, code=True),
                         '${\\bm{\\phi}_{\\textbf{\\texttt{1a}}}}$\\textbf{\\texttt{\\symbol{94}}}${\\textbf{\\texttt{interest}}_{\\textbf{\\texttt{b}}}}$')
        self.assertEqual(modern_chain("12B\\symbol{94}PHI2"),
                         '${\\textrm{12}_{\\textrm{b}}}$\\symbol{94}${\\phi_{\\textrm{2}}}$')

    def test_modern_interp(self):
        self.assertEqual(modern_interp("PHI1A\\symbol{94}interestB\\qquad 12B\\symbol{94}PHI2"),
                         '${\\phi_{\\textrm{1a}}}$\\symbol{94}${\\textrm{interestB\\qquad }_{\\textrm{12b}}}$\\symbol{94}${\\phi_{\\textrm{2}}}$')
        self.assertEqual(modern_interp("gamblersA\\qquad PHI1"),
                         '${\\textrm{gamblersA\\qquad }_{\\textrm{phi1}}}$')

    def test_modern_nodes_str(self):
        self.assertEqual(modern_nodes_str("lt:3, rt:5, th:5, np:4, ch:0, co:4A, ec:4B,"),
                         '\\texttt{lt:3, rt:5, th:5, np:4, ch:0, co:${\\textrm{4}_{\\textrm{a}}}$, ec:${\\textrm{4}_{\\textrm{b}}}$,}')
        self.assertEqual(modern_nodes_str("x:12A, y:15, z:12B"),
                         '\\texttt{x:${\\textrm{12}_{\\textrm{a}}}$, y:15, z:${\\textrm{12}_{\\textrm{b}}}$}')
        self.assertEqual(modern_nodes_str("(N, lit:PHI1 , ftr:[+??????--], up:3, dn:0,"),
                         '\\texttt{(N, lit:${\\phi_{\\textrm{1}}}$, ftr:[+??????--], up:3, dn:0,}')

