import unittest
import index


class TestHandlerCase(unittest.TestCase):

    def test_response(self):
        print("testing response.")
        event = {}
        param = {}
        param['roman'] = 'V'
        event['queryStringParameters'] = param
        result = index.handler(event, None)
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertIn('Hello Richard', result['body'])


if __name__ == '__main__':
    unittest.main()
