import unittest
import requests

class apicall(unittest.TestCase):
    def test_api_output(self):
        url = "http://127.0.0.1:8080"
        response = requests.get(url)
        data = response.json()

        # print(data)

        self.assertEqual("ROOT_BLOCK", data['chain'][0]['data'])


if __name__ == '__main__':
    unittest.main()