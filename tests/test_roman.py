import unittest
from roman import convert


class TestHandlerCase(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(1, convert("I"))
        self.assertEqual(5, convert("V"))


if __name__ == '__main__':
    unittest.main()
