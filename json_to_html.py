import json
from collections import OrderedDict
import re
from html import escape

class Json2Html:
    
    converted = ""

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


    def add_tag_attributes(self, elem_name):
        """
            RegExp func for finding id and class of tags
        """
        ids_list = re.findall(r'\#([a-zA-Z0-9-_]+)', elem_name)
        css_classes = re.findall(r'\.([a-zA-Z0-9-_]+)', elem_name)
        tag_name = re.findall(r'^([a-zA-Z0-9-_]+)', elem_name)[0]

        if len(ids_list) > 0:
            tag_attributes = 'id="%s" ' % ids_list[0]
        else: 
            tag_attributes = ''
        if css_classes:
            tag_attributes += 'class="%s"' % ' '.join(css_classes) 

        return tag_name, tag_attributes


    def convert_list(self, json_data):
        """
            Convert json's list input data
        """
        converted_list = ''
        for list_elem in list(map(self.convert_dict, json_data)):
            converted_list += '<li>%s</li>' % list_elem
        converted_list = '<ul>%s</ul>' % converted_list
        return converted_list


    def convert_dict(self, json_data):
        """
            Convert dict input data
        """
        converted_dict = ''
        for elem_name, elem_attr in json_data.items():
            tag_name, tag_attributes = self.add_tag_attributes(elem_name)
            if type(elem_attr) == list:
                converted_list = self.convert_list(elem_attr)
                converted_dict += '<%s %s>%s</%s>' % (tag_name, tag_attributes, escape(converted_list), tag_name)
            else:
                converted_dict += '<%s %s>%s</%s>' % (tag_name, tag_attributes, escape(elem_attr), tag_name)
        return converted_dict
    

    def convert(self, json_input):
        """
            Convert JSON to HTML
        """
        if type(json_input) == list:
            converted = self.convert_list(json_input)
        else:
            converted = self.convert_dict(json_input)

        return converted


json2html = Json2Html()
data = json2html.load_file(json_file='source5.json')
res = json2html.convert(data)
print('=======Result==========')
print(res)
print('=======EndResult========\n\n')
