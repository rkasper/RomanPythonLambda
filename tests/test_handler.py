import unittest
import index


class TestHandlerCase(unittest.TestCase):
    """
    Tests the web service, which is implemented as a Lambda request handler.

    These tests are more-or-less acceptance tests. The idea is to to A-TDD - for each story:
    - Add an acceptance test for the story.
    - Do micro-scale TDD to get the story done, committing locally along the way.
    - When the acceptance test goes green, push to master.
    """

    def assert_roman_converts_to_arabic(self, roman, arabic):
        param = {'roman': roman}
        event = {'queryStringParameters': param}
        result = index.handler(event, None)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'text/plain')
        self.assertEqual(arabic, result['body'])

    def test_web_service_with_no_parameter_returns_documentation(self):
        event = {}
        result = index.handler(event, None)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'text/plain')
        self.assertTrue(result['body'] != '')

    def test_single_digit(self):
        self.assert_roman_converts_to_arabic('I', '1')
        self.assert_roman_converts_to_arabic('V', '5')
        self.assert_roman_converts_to_arabic('X', '10')
        self.assert_roman_converts_to_arabic('L', '50')


if __name__ == '__main__':
    unittest.main()
