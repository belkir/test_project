import json
from collections import OrderedDict

class Json2Html:
    def load_file(self, json_file=""):
        """
            Loads JSON file
        """
        try:
            with open(json_file, 'r',  encoding='utf8') as json_data:
                data = json.load(json_data, object_pairs_hook=OrderedDict)
                print('\n=======SourceFile==========')
                print(data)
                print('=======EndFile==========\n\n')
                return data
        except Exception as e:
            print('File is empty or not found or wrong format')
            raise SystemExit


    def convert(self, json_input):
        """
            Convert JSON to HTML
        """
        converted = ""
        
        for list_elem in json_input:
            for elem_name, elem_attr in list_elem.items():
                if elem_name == 'title':
                    converted += '<h1>'+elem_attr+'</h1>'
                if elem_name == 'body':
                    converted += '<p>'+elem_attr+'</p>'
        
        return converted


json2html = Json2Html()
data = json2html.load_file(json_file='source1.json')
res = json2html.convert(data)
print('=======Result==========')
print(res)
print('=======EndResult========\n\n')
