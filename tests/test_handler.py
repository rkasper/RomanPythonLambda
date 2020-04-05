import unittest
import index


class TestHandlerCase(unittest.TestCase):

    def test_single_digit_i(self):
        event = {}
        param = {'roman': 'I'}
        event['queryStringParameters'] = param
        result = index.handler(event, None)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertEqual('1', result['body'])

    def test_single_digit_v(self):
        event = {}
        param = {'roman': 'V'}
        event['queryStringParameters'] = param
        result = index.handler(event, None)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertEqual('5', result['body'])


if __name__ == '__main__':
    unittest.main()
