import unittest
import math
from calc import sqrt_func, fact_func, ln_func, power_func
#adding comment to test build
class TestCalculator(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(sqrt_func(16), 4)

    def test_factorial(self):
        self.assertEqual(fact_func(5), 120)

    def test_ln(self):
        self.assertAlmostEqual(ln_func(math.e), 1.0, places=5)

    def test_power(self):
        self.assertEqual(power_func(2, 3), 8)

if __name__ == "__main__":
    unittest.main()
