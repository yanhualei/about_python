import requests
import unittest

class V2exAPITestCase(unittest.TestCase):

    def test_node_api(self):
        url = "https://www.v2ex.com/api/nodes/show.json"
        querystring = {"name":"python"}
        response = requests.request("GET", url, params=querystring).json()
        self.assertEqual(response["name"],'python')
        self.assertEqual(response['id'], 90)

if __name__ == '__main__':
    unittest.main()