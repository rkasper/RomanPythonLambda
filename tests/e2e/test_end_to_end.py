import unittest

import requests


class TestEndToEnd(unittest.TestCase):
    """
    A simple smoke test that proves that the service is up and running end-to-end
    """
    def test_end_to_end_smoke_test(self):
        r = requests.get('https://9zbdaspg2k.execute-api.us-east-2.amazonaws.com/Prod?roman=I')
        self.assertEqual(200, r.status_code)
        self.assertEqual('text/plain', r.headers['content-type'])
        print(r.text)
        self.assertEqual('1', r.text)


if __name__ == '__main__':
    unittest.main()
