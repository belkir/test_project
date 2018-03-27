import unittest
from json_to_html import *

class TestJson2Html(unittest.TestCase):

    def setUp(self):
        self.test_json = []
        self.json2html = Json2Html()
    
    def test_task(self):
        etalon_res = '<h3>Title #1</h3><div>Hello, World 1!</div>'
        data = self.json2html.load_file(json_file='source2.json')
        res = self.json2html.convert(data)
        self.assertEqual(res, etalon_res)

if __name__ == '__main__':
    unittest.main()
