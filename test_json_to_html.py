import unittest
from json_to_html import *

class TestJson2Html(unittest.TestCase):

    def setUp(self):
        self.test_json = []
        self.json2html = Json2Html()
    

    def test_task4_1(self):
        etalon_res = '<ul><li><span>Title #1</span><content><ul><li><p>Example 1</p><header>header 1</header></li></ul></content></li><li><div>div 1</div></li></ul>'
        data = self.json2html.load_file(json_file='source4_1.json')
        res = self.json2html.convert(data)
        self.assertEqual(res, etalon_res)
    

    def test_task4_2(self):
        etalon_res = '<p>hello1</p>'
        data = self.json2html.load_file(json_file='source4_2.json')
        res = self.json2html.convert(data)
        self.assertEqual(res, etalon_res)


if __name__ == '__main__':
    unittest.main()
