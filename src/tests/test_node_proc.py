################################################################
#
#    test_node_proc.py
#
################################################################

from unittest import TestCase
from pronouns2 import *

class TestNodeProc(TestCase):
    def test_node_proc(self):
        """Test node_proc.py functions."""
        node_proc_reset()
        node = new_node(NodeId.N_NODE)
        cnode = new_c_node()
        snode = new_s_node()
        nnode = new_n_node()
        enode = new_e_node()
        self.assertEqual(node.id, NodeId.N_NODE)
        self.assertEqual(cnode.id, NodeId.C_NODE)
        self.assertEqual(snode.id, NodeId.S_NODE)
        self.assertEqual(nnode.id, NodeId.N_NODE)
        self.assertEqual(enode.id, NodeId.E_NODE)
        self.assertEqual(node.number, 1)
        self.assertEqual(cnode.number, 2)
        self.assertEqual(snode.number, 3)
        self.assertEqual(nnode.number, 4)
        self.assertEqual(enode.number, 5)

