################################################################
#
#    test_primary_uty.py
#
################################################################

import unittest
from pronouns2 import *

class TestPrimaryUtyFunctions(unittest.TestCase):
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

    def test_primary_uty_precede(self):
        """Test precede function."""
        self.assertEqual(precede(self.S10, self.JohnA), True)
        self.assertEqual(precede(self.PHIB, self.S4), False)
        self.assertEqual(precede(self.sheA, self.JuneA), False)
        self.assertEqual(precede(self.June, self.PHIA), True)
        self.assertEqual(precede(self.itA, self.PHI), False)
        self.assertEqual(precede(self.John, self.JohnC), True)
        self.assertEqual(precede(self.itA, self.JohnA), False)
        self.assertEqual(precede(self.S4, self.presentB), True)
        self.assertEqual(precede(self.JohnA, self.PHIB), True)
        self.assertEqual(precede(self.PHIA, self.John), False)
        self.assertEqual(precede(self.PHIB, self.he), False)
        self.assertEqual(precede(self.PHIB, self.John), False)
        self.assertEqual(precede(self.itA, self.PHIA), False)
        self.assertEqual(precede(self.PHIA, self.heA), True)
        self.assertEqual(precede(self.it, self.S8), False)
        self.assertEqual(precede(self.PHIC, self.JohnA), False)
        self.assertEqual(precede(self.JuneA, self.JohnB), True)
        self.assertEqual(precede(self.JohnB, self.PHIA), False)
        self.assertEqual(precede(self.S4, self.S4), False)
        self.assertEqual(precede(self.PHIA, self.S4), False)

    def test_primary_uty_dominate(self):
        """Test dominate function."""
        self.assertEqual(dominate(self.JohnA, self.June), False)
        self.assertEqual(dominate(self.C1, self.S10), True)
        self.assertEqual(dominate(self.S2, self.PHID), False)
        self.assertEqual(dominate(self.it, self.John), False)
        self.assertEqual(dominate(self.sheA, self.he), False)
        self.assertEqual(dominate(self.S10, self.it), True)
        self.assertEqual(dominate(self.S4, self.S4), True)
        self.assertEqual(dominate(self.S8, self.S10), True)
        self.assertEqual(dominate(self.JohnC, self.JohnC), True)
        self.assertEqual(dominate(self.PHIB, self.he), False)
        self.assertEqual(dominate(self.she, self.PHIA), False)
        self.assertEqual(dominate(self.he, self.S10), False)
        self.assertEqual(dominate(self.S4, self.June), True)
        self.assertEqual(dominate(self.S2, self.PHI), True)
        self.assertEqual(dominate(self.S10, self.she), True)
        self.assertEqual(dominate(self.S2, self.itA), False)
        self.assertEqual(dominate(self.JohnD, self.JohnD), True)
        self.assertEqual(dominate(self.C1, self.he), True)
        self.assertEqual(dominate(self.S2, self.present), True)
        self.assertEqual(dominate(self.S2, self.S4), True)

    def test_primary_uty_command(self):
        """Test command function."""
        self.assertEqual(command(self.it, self.S10), True)
        self.assertEqual(command(self.it, self.June), False)
        self.assertEqual(command(self.it, self.S2), False)
        self.assertEqual(command(self.S8, self.S4), True)
        self.assertEqual(command(self.PHI, self.John), False)
        self.assertEqual(command(self.she, self.S8), False)
        self.assertEqual(command(self.John, self.present), True)
        self.assertEqual(command(self.John, self.S10), False)
        self.assertEqual(command(self.she, self.present), False)
        self.assertEqual(command(self.June, self.June), True)
        self.assertEqual(command(self.it, self.it), True)
        self.assertEqual(command(self.S10, self.present), False)
        self.assertEqual(command(self.S10, self.he), True)
        self.assertEqual(command(self.S2, self.she), True)
        self.assertEqual(command(self.PHI, self.it), False)
        self.assertEqual(command(self.S4, self.he), False)
        self.assertEqual(command(self.S4, self.it), False)
        self.assertEqual(command(self.he, self.it), True)
        self.assertEqual(command(self.she, self.she), True)
        self.assertEqual(command(self.S10, self.S2), False)

    def test_primary_uty_separate(self):
        """Test separate function."""
        self.assertEqual(separate(self.John, self.S10), True)
        self.assertEqual(separate(self.PHI, self.he), True)
        self.assertEqual(separate(self.John, self.S8), True)
        self.assertEqual(separate(self.it, self.June), True)
        self.assertEqual(separate(self.June, self.John), False)
        self.assertEqual(separate(self.it, self.he), False)
        self.assertEqual(separate(self.S2, self.S8), True)
        self.assertEqual(separate(self.present, self.she), True)
        self.assertEqual(separate(self.present, self.S4), False)
        self.assertEqual(separate(self.S8, self.S10), True)
        self.assertEqual(separate(self.she, self.John), True)
        self.assertEqual(separate(self.it, self.PHI), True)
        self.assertEqual(separate(self.S2, self.S4), True)
        self.assertEqual(separate(self.PHI, self.S10), True)
        self.assertEqual(separate(self.June, self.she), True)
        self.assertEqual(separate(self.PHI, self.S4), False)
        self.assertEqual(separate(self.S2, self.present), True)
        self.assertEqual(separate(self.S4, self.PHI), False)
        self.assertEqual(separate(self.S10, self.S8), False)
        self.assertEqual(separate(self.S2, self.S10), True)

if __name__ == "__main__":
    unittest.main()
