import unittest
from json_to_html import *

class TestJson2Html(unittest.TestCase):

    def setUp(self):
        self.test_json = []
        self.json2html = Json2Html()
    
    def test_1(self):
        etalon_res_1 = '<h1>Title #1</h1><p>Hello, World 1!</p><h1>Title #2</h1><p>Hello, World 2!</p>'
        data = self.json2html.load_file(json_file='source1.json')
        res = self.json2html.convert(data)
        self.assertEqual(res, etalon_res_1)

if __name__ == '__main__':
    unittest.main()
