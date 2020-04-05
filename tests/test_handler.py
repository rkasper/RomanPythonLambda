import unittest
import index


class TestHandlerCase(unittest.TestCase):
    """Tests the Lambda request handler. These tests are more-or-less BDD-style tests."""

    def assert_roman_converts_to_arabic(self, roman, arabic):
        param = {'roman': roman}
        event = {'queryStringParameters': param}
        result = index.handler(event, None)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertEqual(arabic, result['body'])

    def test_single_digit_i(self):
        self.assert_roman_converts_to_arabic('I', '1')

    def test_single_digit_v(self):
        self.assert_roman_converts_to_arabic('V', '5')

    def test_single_digit_x(self):
        self.assert_roman_converts_to_arabic('X', '10')


if __name__ == '__main__':
    unittest.main()
