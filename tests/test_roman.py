import unittest
from roman import convert


class TestRomanCase(unittest.TestCase):
    """Unit tests of the Roman -> Arabic converter"""

    def test_single_digit(self):
        self.assertEqual(1, convert("I"))
        self.assertEqual(5, convert("V"))
        self.assertEqual(10, convert("X"))
        self.assertEqual(50, convert("L"))


if __name__ == '__main__':
    unittest.main()
