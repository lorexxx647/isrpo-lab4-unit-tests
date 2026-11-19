# test_calculator.py
import unittest
from calculator import add, subtract, multiply, divide, power, sqrt


class CalculatorTestCase(unittest.TestCase):

    # ---------- add ----------
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

    def test_add_float(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)

    # ---------- subtract ----------
    def test_subtract_positive(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_subtract_to_negative(self):
        self.assertEqual(subtract(4, 10), -6)

    def test_subtract_zero(self):
        self.assertEqual(subtract(7, 0), 7)

    # ---------- multiply ----------
    def test_multiply_positive(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(10, 0), 0)

    def test_multiply_negative(self):
        self.assertEqual(multiply(-3, 4), -12)

    # ---------- divide ----------
    def test_divide_positive(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_float(self):
        self.assertAlmostEqual(divide(7, 3), 2.3333333, places=5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    # ---------- power ----------
    def test_power_positive(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_zero_exponent(self):
        self.assertEqual(power(5, 0), 1)

    def test_power_negative_exponent(self):
        self.assertAlmostEqual(power(2, -1), 0.5, places=7)

    # ---------- sqrt ----------
    def test_sqrt_positive(self):
        self.assertEqual(sqrt(9), 3)

    def test_sqrt_zero(self):
        self.assertEqual(sqrt(0), 0)

    def test_sqrt_negative_raises(self):
        with self.assertRaises(ValueError):
            sqrt(-1)


if __name__ == "__main__":
    unittest.main()
