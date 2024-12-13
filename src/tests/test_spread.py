################################################################
#
#    test_spread.py
#
################################################################

from unittest import TestCase
from tests.utils.assertions import FloatAssertionMixin
from pronouns2 import *

class TestSpread(FloatAssertionMixin, TestCase):
    def test_spread_example(self):
        old_angles = [0.9272952180016123, 2.214297435588181]
        rho = 0.24145300700522387
        new_angles = spread(old_angles, rho)
        self.assertListAlmostEqual(new_angles,
                                   [0.7033969992335587, 2.4381956543562353], places=4)

    def test_spread_ordinary(self):
        old_angles = [0.7684266671440736, 1.4363945355906882, 1.8019442776018897, 2.082750104745662, 2.548319641144211]
        rho = 0.4431372758558222
        new_angles = spread(old_angles, rho)
        self.assertListAlmostEqual(new_angles,
                                   [0.1805606070973793, 1.1093897381055182, 1.8698134873962555, 2.5830465093992734, -2.884017753318698], places=4)

    def test_spread_coincident_even(self):
        old_angles = [0.0, 0.0, 0.0, 0.7853981633974483]
        rho = 0.38898452964834274
        new_angles = spread(old_angles, rho)
        self.assertListAlmostEqual(new_angles,
                                   [-1.2953378052714672, -0.6843223349198091, -0.07330686456815272, 1.0175990340051246], places=4)

    def test_spread_coincident_odd(self):
        old_angles = [0.0, 0.0, 0.0, 0.7853981633974483, -3.141592653589793]
        rho = 0.4431372758558222
        new_angles = spread(old_angles, rho)
        self.assertListAlmostEqual(new_angles,
                                   [-1.181649908905186, -0.6247871847610078, -0.06792446061682966, 0.9262972243346841, 2.7952368309008744], places=4)

    def test_spread_early_average(self):
        old_angles = [0.0, 0.5236114777699692, 1.0471848490249274, -0.5236114777699683]
        rho = 0.38898452964834274
        new_angles = spread(old_angles, rho)
        self.assertListAlmostEqual(new_angles,
                                   [-0.2036617644723009, 0.7272884192505007, 1.6582153193031086, -1.1346119481951025], places=4)

    def test_spread_late_average(self):
        old_angles = [2.0944078045648666, 2.617981175819824, -3.141592653589793, -2.617981175819824]
        rho = 0.38898452964834274
        new_angles = spread(old_angles, rho)
        self.assertListAlmostEqual(new_angles,
                                   [1.4833773342866845, 2.4143042343392924, -2.9379308891174922, -2.0069807053946915], places=4)

    def test_spread_delta_0p0(self):
        old_angles = [1.0973100370555384, 1.1724678487334534, 1.2651683082846423, 1.4786882146833893, 1.8545904360032246, 1.9368217258610443]
        rho = 0.0
        new_angles = spread(old_angles, rho)
        self.assertListAlmostEqual(new_angles,
                                   [1.0973100370555384, 1.1724678487334534, 1.2651683082846423, 1.4786882146833893, 1.8545904360032246, 1.9368217258610443], places=4)

    def test_spread_delta_0p25(self):
        old_angles = [1.0973100370555384, 1.1724678487334534, 1.2651683082846423, 1.4786882146833893, 1.8545904360032246, 1.9368217258610443]
        rho = 0.19272315135762313
        new_angles = spread(old_angles, rho)
        self.assertListAlmostEqual(new_angles,
                                   [0.5754388837562914, 0.8379312572790898, 1.1145854042938677, 1.4887742936144575, 1.994050666399798, 2.2622532950966114], places=4)

    def test_spread_delta_0p5(self):
        old_angles = [1.0973100370555384, 1.1724678487334534, 1.2651683082846423, 1.4786882146833893, 1.8545904360032246, 1.9368217258610443]
        rho = 0.3231649375435616
        new_angles = spread(old_angles, rho)
        self.assertListAlmostEqual(new_angles,
                                   [0.22221818911878177, 0.6115051625081116, 1.0126656150663997, 1.4956009054777084, 2.088442240150452, 2.4825167915854625], places=4)

    def test_spread_delta_1p0(self):
        old_angles = [1.0973100370555384, 1.1724678487334534, 1.2651683082846423, 1.4786882146833893, 1.8545904360032246, 1.9368217258610443]
        rho = 0.48847264369552157
        new_angles = spread(old_angles, rho)
        self.assertListAlmostEqual(new_angles,
                                   [-0.22541523037990885, 0.32455740263780397, 0.883503579944712, 1.5042522094877215, 2.2080638352929167, 2.761654745903873], places=4)

    def test_spread_delta_2p0(self):
        old_angles = [1.0973100370555384, 1.1724678487334534, 1.2651683082846423, 1.4786882146833893, 1.8545904360032246, 1.9368217258610443]
        rho = 0.6563407742352064
        new_angles = spread(old_angles, rho)
        self.assertListAlmostEqual(new_angles,
                                   [-0.6799819716863027, 0.0331651552146921, 0.7523409749016814, 1.5130375121496336, 2.329538230021261, 3.0451162229570263], places=4)

    def test_spread_delta_4p0(self):
        old_angles = [1.0973100370555384, 1.1724678487334534, 1.2651683082846423, 1.4786882146833893, 1.8545904360032246, 1.9368217258610443]
        rho = 0.7925190087024974
        new_angles = spread(old_angles, rho)
        self.assertListAlmostEqual(new_angles,
                                   [-1.0487362794851904, -0.2032184970244959, 0.6459390514069296, 1.5201643384383026, 2.428080869138686, -3.008119043315518], places=4)

    def test_spread_delta_8p0(self):
        old_angles = [1.0973100370555384, 1.1724678487334534, 1.2651683082846423, 1.4786882146833893, 1.8545904360032246, 1.9368217258610443]
        rho = 0.8842517204614269
        new_angles = spread(old_angles, rho)
        self.assertListAlmostEqual(new_angles,
                                   [-1.2971374484348726, -0.3624518247306838, 0.574264330283385, 1.5249651284048618, 2.494461400105946, -2.8532195404397758], places=4)

    def test_spread_delta_16p0(self):
        old_angles = [1.0973100370555384, 1.1724678487334534, 1.2651683082846423, 1.4786882146833893, 1.8545904360032246, 1.9368217258610443]
        rho = 0.9385706918658256
        new_angles = spread(old_angles, rho)
        self.assertListAlmostEqual(new_angles,
                                   [-1.4442267008321608, -0.45674087831311994, 0.531822576927619, 1.5278078871973566, 2.533768230725922, -2.7614967350639272], places=4)

    def test_spread_delta_32p0(self):
        old_angles = [1.0973100370555384, 1.1724678487334534, 1.2651683082846423, 1.4786882146833893, 1.8545904360032246, 1.9368217258610443]
        rho = 0.9683120618753138
        new_angles = spread(old_angles, rho)
        self.assertListAlmostEqual(new_angles,
                                   [-1.5247627597239628, -0.5083671436479698, 0.5085843627683757, 1.529364388340685, 2.5552899746607576, -2.7112755725039444], places=4)

    def test_spread_delta_64p0(self):
        old_angles = [1.0973100370555384, 1.1724678487334534, 1.2651683082846423, 1.4786882146833893, 1.8545904360032246, 1.9368217258610443]
        rho = 0.9839009582177253
        new_angles = spread(old_angles, rho)
        self.assertListAlmostEqual(new_angles,
                                   [-1.5669756192354827, -0.5354269764194282, 0.4964040862177108, 1.5301802261777588, 2.5665705658104248, -2.684952222332342], places=4)

    def test_spread_1(self):
        old_angles = [0.5235987755982988, 1.5707963267948966]
        rho = 0.333333333333333
        new_angles = spread(old_angles, rho)
        self.assertListAlmostEqual(new_angles,
                                   [0.1745329251994333, 1.9198621771937623], places=4)

    def test_spread_2(self):
        old_angles = [0.5235987755982988, 1.5707963267948966, 2.0943951023931953]
        rho = 0.333333333333333
        new_angles = spread(old_angles, rho)
        self.assertListAlmostEqual(new_angles,
                                   [0.22569420887355884, 1.6219576104690223, 2.6691551616656195], places=4)

    def test_spread_3(self):
        old_angles = [0.5235987755982988, 1.0471975511965976, 1.5707963267948966, 2.0943951023931953]
        rho = 0.333333333333333
        new_angles = spread(old_angles, rho)
        self.assertListAlmostEqual(new_angles,
                                   [3.3306690738754696e-16, 0.8726646259971649, 1.7453292519943293, 2.6179938779914935], places=4)

