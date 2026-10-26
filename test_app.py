import unittest
from app import *
class DomainTests(unittest.TestCase):
    def test_feature_sum(self):self.assertAlmostEqual(dinucleotides('ACGTAC').sum(),1)
    def test_invalid_base(self):
        with self.assertRaises(ValueError):dinucleotides('ACGN')
    def test_single_base(self):np.testing.assert_array_equal(dinucleotides('A'),np.zeros(16))
