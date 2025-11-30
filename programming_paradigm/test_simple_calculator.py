import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # ----------------- Addition Tests -----------------
    def test_addition(self):
        """Test the addition method with various inputs."""
        self.assertEqual(self.calc.add(2, 3), 5)          # positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)         # negative and positive
        self.assertEqual(self.calc.add(0, 0), 0)          # zero addition
        self.assertEqual(self.calc.add(-5, -7), -12)      # negative numbers
        self.assertEqual(self.calc.add(2.5, 3.1), 5.6)    # floating point numbers

    # ----------------- Subtraction Tests -----------------
    def test_subtraction(self):
        """Test the subtraction method with various inputs."""
        self.assertEqual(self.calc.subtract(5, 3), 2)      # positive numbers
        self.assertEqual(self.calc.subtract(-1, 1), -2)    # negative and positive
        self.assertEqual(self.calc.subtract(0, 0), 0)      # zero subtraction
        self.assertEqual(self.calc.subtract(-5, -7), 2)    # negative numbers
        self.assertEqual(self.calc.subtract(3.5, 1.2), 2.3) # floating point numbers

    # ----------------- Multiplication Tests -----------------
    def test_multiplication(self):
        """Test the multiplication method with various inputs."""
        self.assertEqual(self.calc.multiply(2, 3), 6)       # positive numbers
        self.assertEqual(self.calc.multiply(-1, 1), -1)     # negative and positive
        self.assertEqual(self.calc.multiply(0, 5), 0)       # multiplication by zero
        self.assertEqual(self.calc.multiply(-5, -7), 35)    # negative numbers
        self.assertAlmostEqual(self.calc.multiply(2.5, 1.2), 3.0) # floating point numbers

    # ----------------- Division Tests -----------------
    def test_division(self):
        """Test the division method with various inputs."""
        self.assertEqual(self.calc.divide(6, 3), 2)         # normal division
        self.assertEqual(self.calc.divide(-4, 2), -2)       # negative numerator
        self.assertEqual(self.calc.divide(0, 5), 0)         # zero numerator
        self.assertEqual(self.calc.divide(-10, -2), 5)      # negative numerator and denominator
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0) # floating point division

    def test_division_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(5, 0))           # division by zero
        self.assertIsNone(self.calc.divide(0, 0))           # zero divided by zero
        self.assertIsNone(self.calc.divide(-5, 0))          # negative numerator divided by zero

if __name__ == "__main__":
    unittest.main()
