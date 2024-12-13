################################################################
#
#    test_secondary_uty.py
#
################################################################

import unittest
from pronouns2 import *

class TestSecondaryUtyFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up reusable inputs for tests."""
        demo("10.1")
        cls.nodes = tree_nodes(Node.tree())
        cls.C1 = cls.nodes[0]
        cls.S2 = cls.nodes[1]
        cls.John = cls.nodes[2]
        cls.JohnA = cls.nodes[3]
        cls.JohnB = cls.nodes[4]
        cls.JohnC = cls.nodes[5]
        cls.JohnD = cls.nodes[6]
        cls.S4 = cls.nodes[7]
        cls.PHI = cls.nodes[8]
        cls.PHIA = cls.nodes[9]
        cls.PHIB = cls.nodes[10]
        cls.PHIC = cls.nodes[11]
        cls.PHID = cls.nodes[12]
        cls.June = cls.nodes[13]
        cls.JuneA = cls.nodes[14]
        cls.JuneB = cls.nodes[15]
        cls.present = cls.nodes[16]
        cls.presentA = cls.nodes[17]
        cls.presentB = cls.nodes[18]
        cls.S8 = cls.nodes[19]
        cls.he = cls.nodes[20]
        cls.heA = cls.nodes[21]
        cls.S10 = cls.nodes[22]
        cls.she = cls.nodes[23]
        cls.sheA = cls.nodes[24]
        cls.it = cls.nodes[25]
        cls.itA = cls.nodes[26]

    def test_secondary_uty_sc(self):
        """Test sc function."""
        self.assertEqual(sc(self.it, self.she), True)
        self.assertEqual(sc(self.it, self.he), True)
        self.assertEqual(sc(self.it, self.present), True)
        self.assertEqual(sc(self.it, self.June), True)
        self.assertEqual(sc(self.it, self.PHI), True)
        self.assertEqual(sc(self.it, self.John), True)
        self.assertEqual(sc(self.she, self.it), False)
        self.assertEqual(sc(self.she, self.he), True)
        self.assertEqual(sc(self.she, self.present), True)
        self.assertEqual(sc(self.she, self.June), True)
        self.assertEqual(sc(self.she, self.PHI), True)
        self.assertEqual(sc(self.she, self.John), True)
        self.assertEqual(sc(self.he, self.it), False)
        self.assertEqual(sc(self.he, self.she), False)
        self.assertEqual(sc(self.he, self.present), True)
        self.assertEqual(sc(self.he, self.June), True)
        self.assertEqual(sc(self.he, self.PHI), True)
        self.assertEqual(sc(self.he, self.John), True)
        self.assertEqual(sc(self.PHI, self.it), False)
        self.assertEqual(sc(self.PHI, self.she), False)
        self.assertEqual(sc(self.PHI, self.he), False)
        self.assertEqual(sc(self.PHI, self.present), False)
        self.assertEqual(sc(self.PHI, self.June), False)
        self.assertEqual(sc(self.PHI, self.John), True)

    def test_secondary_uty_agr(self):
        """Test agr function."""
        self.assertEqual(agr(self.it, self.she), False)
        self.assertEqual(agr(self.it, self.he), False)
        self.assertEqual(agr(self.it, self.present), True)
        self.assertEqual(agr(self.itA, self.present), True)
        self.assertEqual(agr(self.it, self.June), False)
        self.assertEqual(agr(self.it, self.PHI), True)
        self.assertEqual(agr(self.itA, self.PHI), True)
        self.assertEqual(agr(self.it, self.John), False)
        self.assertEqual(agr(self.she, self.he), False)
        self.assertEqual(agr(self.she, self.present), False)
        self.assertEqual(agr(self.she, self.June), True)
        self.assertEqual(agr(self.sheA, self.June), True)
        self.assertEqual(agr(self.she, self.PHI), True)
        self.assertEqual(agr(self.sheA, self.PHI), True)
        self.assertEqual(agr(self.she, self.John), False)
        self.assertEqual(agr(self.he, self.present), False)
        self.assertEqual(agr(self.he, self.June), False)
        self.assertEqual(agr(self.he, self.PHI), True)
        self.assertEqual(agr(self.heA, self.PHI), True)
        self.assertEqual(agr(self.he, self.John), True)
        self.assertEqual(agr(self.heA, self.John), True)
        self.assertEqual(agr(self.PHI, self.John), True)
        self.assertEqual(agr(self.PHIA, self.John), True)
        self.assertEqual(agr(self.PHIB, self.John), False)
        self.assertEqual(agr(self.PHIC, self.John), False)
        self.assertEqual(agr(self.PHID, self.John), True)

    def test_secondary_uty_eq_feat(self):
        """Test eq_feat function."""
        self.assertEqual(eq_feat(Feature.PLUS, Feature.PLUS), True)
        self.assertEqual(eq_feat(Feature.PLUS, Feature.QUESTION), True)
        self.assertEqual(eq_feat(Feature.PLUS, Feature.MINUS), False)
        self.assertEqual(eq_feat(Feature.QUESTION, Feature.PLUS), True)
        self.assertEqual(eq_feat(Feature.QUESTION, Feature.QUESTION), True)
        self.assertEqual(eq_feat(Feature.QUESTION, Feature.MINUS), True)
        self.assertEqual(eq_feat(Feature.MINUS, Feature.PLUS), False)
        self.assertEqual(eq_feat(Feature.MINUS, Feature.QUESTION), True)
        self.assertEqual(eq_feat(Feature.MINUS, Feature.MINUS), True)

    def test_secondary_uty_rnr(self):
        """Test rnr function."""
        self.assertEqual(rnr(self.it, self.present), True)
        self.assertEqual(rnr(self.it, self.PHI), True)
        self.assertEqual(rnr(self.she, self.June), True)
        self.assertEqual(rnr(self.she, self.PHI), True)
        self.assertEqual(rnr(self.he, self.PHI), True)
        self.assertEqual(rnr(self.he, self.John), True)
        self.assertEqual(rnr(self.PHI, self.John), True)
        self.assertEqual(rnr(self.PHI, self.June), False)
        self.assertEqual(rnr(self.PHI, self.present), False)
        self.assertEqual(rnr(self.June, self.PHI), False)
        self.assertEqual(rnr(self.June, self.present), False)
        self.assertEqual(rnr(self.present, self.PHI), False)
        self.assertEqual(rnr(self.present, self.June), False)
        self.assertEqual(rnr(self.she, self.it), False)
        self.assertEqual(rnr(self.it, self.she), False)

if __name__ == "__main__":
    unittest.main()
