import unittest
from json_to_html import *

class TestJson2Html(unittest.TestCase):

    def setUp(self):
        self.test_json = []
        self.json2html = Json2Html()
    

    def test_task5(self):
        etalon_res = '<p id="my-id" class="my-class">hello</p><p class="my-class1 my-class2">example&lt;a&gt;asd&lt;/a&gt;</p>'
        data = self.json2html.load_file(json_file='source5.json')
        res = self.json2html.convert(data)
        self.assertEqual(res, etalon_res)


    def test_task5_extended(self):
        etalon_res = '<p id="my-id" class="my-class">hello</p><p class="my-class1 my-class2">example&lt;a&gt;asd&lt;/a&gt;</p>'
        data = json.loads("""{
                "p #my-id .my-class": "hello",
                "p .my-class1 .my-class2":"example<a>asd</a>"
            }""")
        res = self.json2html.convert(data)
        self.assertEqual(res, etalon_res)
    

if __name__ == '__main__':
    unittest.main()
