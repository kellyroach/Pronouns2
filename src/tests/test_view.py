################################################################
#
#    test_view.py
#
################################################################

import unittest
from pronouns2 import *

class TestViewFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up reusable inputs for tests."""
        demo("10.1")
        cls.nodes = tree_nodes(Node.tree())
        cls.nnodes = tree_n_nodes(Node.tree())
        cls.node = cls.nnodes[0]
        cls.ftr = cls.node.ftr
        cls.interps = interpret(cls.nnodes)
        cls.interp = cls.interps[0]
        cls.chains = cls.interp
        cls.chain = cls.chains[0]
        cls.dict = {nnode.number: [] for nnode in cls.nnodes
                                  if nnode.ftr[FeatureIndex.PNF] == Feature.PLUS}

    def test_view_nodes(self):
        """Test view_nodes function."""
        expected_output = [['1 ', '(C, up:0, dn:2, lt:0, rt:0, th:2, nu:1)'],
                           ['2 ', '(S, up:1, dn:3, lt:0, rt:8, th:3, nu:2)'],
                           ['3 ', '(N, lit:John, ftr:[---+--+--], up:2, dn:0,']]
        self.assertEqual(view_nodes(self.nodes)[:3], expected_output)

    def test_view_nodes_row(self):
        """Test view_nodes_row function."""
        expected_output = [['3 ', '(N, lit:John, ftr:[---+--+--], up:2, dn:0,'],
                           ['', ' lt:0, rt:4, th:4, np:3, ch:0, co:3A, ec:3D,'],
                           ['', ' pr:0, su:5, nu:3)']]
        self.assertEqual(view_nodes_row(self.node), expected_output)

    def test_view_node_str(self):
        """Test view_node_str function."""
        expected_output = "(N, lit:John, ftr:[---+--+--], up:2, dn:0,\n     lt:0, rt:4, th:4, np:3, ch:0, co:3A, ec:3D,\n     pr:0, su:5, nu:3)"
        self.assertEqual(view_node_str(self.node), expected_output)

    def test_view_features(self):
        """Test view_features function."""
        expected_output = [['', 'PNF', 'FPF', 'SPF', 'TPF', 'PLF', 'GNF', 'ANF', 'RPF', 'GEN'],
                           ['John', '-', '-', '-', '+', '-', '-', '+', '-', '-'],
                           ['PHI', '+', '?', '?', '?', '?', '?', '?', '-', '-'],
                           ['June', '-', '-', '-', '+', '-', '+', '+', '-', '-']]
        self.assertEqual(view_features(self.nnodes)[:4], expected_output)

    def test_view_features_row(self):
        """Test view_features_row function."""
        expected_output = ['John', '-', '-', '-', '+', '-', '-', '+', '-', '-']
        self.assertEqual(view_features_row(self.node), expected_output)

    def test_view_chaining(self):
        """Test view_chaining function."""
        expected_output = [['John', 'PHI', 'June', 'present', 'he', 'she', 'it'],
                           ['JohnA', 'PHIA', 'JuneA', 'presentA', 'heA', 'sheA', 'itA']]
        self.assertEqual(view_chaining(self.nnodes)[:2], expected_output)

    def test_view_transpose(self):
        """Test view_transpose function."""
        input_data = [["0", "1", "2"], ["3", "4", "5"], ["6", "7", "8"]]
        expected_output = [['0', '3', '6'], ['1', '4', '7'], ['2', '5', '8']]
        self.assertEqual(view_transpose(input_data), expected_output)

    def test_view_transpose_any(self):
        """Test view_transpose_any function."""
        input_data = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        expected_output = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
        self.assertEqual(view_transpose_any(input_data), expected_output)

    def test_view_chaining_columns(self):
        """Test view_chaining_columns function."""
        expected_output = [['John', 'JohnA', 'JohnB^heA', 'JohnC^PHIA', 'JohnD^PHID']]
        self.assertEqual(view_chaining_columns(self.nnodes)[:1], expected_output)

    def test_view_chaining_column(self):
        """Test view_chaining_column function."""
        expected_output = ['John', 'JohnA', 'JohnB^heA', 'JohnC^PHIA', 'JohnD^PHID']
        self.assertEqual(view_chaining_column(self.node), expected_output)

    def test_view_chaining_label(self):
        """Test view_chaining_label function."""
        expected_output = "John "
        self.assertEqual(view_chaining_label(self.node), expected_output)

    def test_view_interpretations(self):
        """Test view_interpretations function."""
        expected_output = [['JohnD^PHID^heA    JuneB^sheA    presentB^itA']]
        self.assertEqual(view_interpretations(self.interps), expected_output)

    def test_view_interpretations_row(self):
        """Test view_interpretations_row function."""
        expected_output = ['JohnD^PHID^heA    JuneB^sheA    presentB^itA']
        viewed_interps = view_interps(self.interps)
        viewed_interp = viewed_interps[0]
        self.assertEqual(view_interpretations_row(viewed_interp), expected_output)

    def test_view_interps(self):
        """Test view_interps function."""
        expected_output = [['JohnD^PHID^heA', 'JuneB^sheA', 'presentB^itA']]
        self.assertEqual(view_interps(self.interps), expected_output)

    def test_view_dict(self):
        """Test view_dict function."""
        expected_output = {5: [], 9: [], 11: [], 12: []}
        self.assertEqual(view_dict(self.dict), expected_output)

    def test_view_chains(self):
        """Test view_chains function."""
        expected_output = ['JohnD^PHID^heA', 'JuneB^sheA', 'presentB^itA']
        self.assertEqual(view_chains(self.chains), expected_output)

    def test_view_chain(self):
        """Test view_chain function."""
        expected_output = 'JohnD^PHID^heA'
        self.assertEqual(view_chain(self.chain), expected_output)

    def test_view_label(self):
        """Test view_label function."""
        expected_output = 'John'
        self.assertEqual(view_label(self.node), expected_output)

    def test_view_short_label(self):
        """Test view_short_label function."""
        expected_output = '3'
        self.assertEqual(view_short_label(self.node), expected_output)

    def test_view_label_2(self):
        """Test view_label function #2."""
        expected_output = ['John', 'PHI', 'June', 'present', 'he', 'she', 'it']
        labels = [view_label(node) for node in self.nnodes]
        self.assertEqual(labels, expected_output)

    def test_view_short_label_2(self):
        """Test view_short_label function #2."""
        expected_output = ['3', '5', '6', '7', '9', '11', '12']
        short_labels = [view_short_label(node) for node in self.nnodes]
        self.assertEqual(short_labels, expected_output)

    def test_view_label_3(self):
        """Test view_label function #3."""
        expected_output = ['C1', 'S2', 'John', 'JohnA', 'JohnB', 'JohnC', 'JohnD', 'S4',
                           'PHI', 'PHIA', 'PHIB', 'PHIC', 'PHID', 'June', 'JuneA', 'JuneB',
                           'present', 'presentA', 'presentB', 'S8', 'he', 'heA', 'S10', 'she',
                           'sheA', 'it', 'itA']
        labels = [view_label(node) for node in self.nodes]
        self.assertEqual(labels, expected_output)

    def test_view_short_label_3(self):
        """Test view_short_label function #3."""
        expected_output = ['1', '2', '3', '3A', '3B', '3C', '3D', '4',
                           '5', '5A', '5B', '5C', '5D', '6', '6A', '6B',
                           '7', '7A', '7B', '8', '9', '9A', '10', '11',
                           '11A', '12', '12A']
        short_labels = [view_short_label(node) for node in self.nodes]
        self.assertEqual(short_labels, expected_output)

if __name__ == "__main__":
    unittest.main()
