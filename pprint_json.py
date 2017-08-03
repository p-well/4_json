import json
import os
import argparse
from pprint import pprint

def load_data():
    if os.path.isfile("raw_json.json"): 
        with open("raw_json.json", 'r', encoding='utf-8') as raw_json_file:
            raw_json_file_text = json.loads(raw_json_file)
            #return raw_json_file_text
            pprint(raw_json_file_text)
    else:
        print("oops")
        return None

load_data()       

def pretty_print_json(data):
    print(json.dumps(data, indent=4, ensure_ascii=False))

if __name__ == '__main__':
    parser = argparse.ArgumentParse('description' = 'Getting pretty json')
    parser.add_argument('-p', '--path', required = True,        
                        'help' = 'Enter path to json file after flag -p or --path')
    namespace = parser.parse_args(sys.argv[1:])
    

