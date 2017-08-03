import json
import os
import argparse

def load_data(filepath):
    if os.path.isfile(filepath): 
        with open(filepath, 'r', encoding='utf-8') as raw_json_file:
            raw_json_file_text = json.load(raw_json_file)
            return raw_json_file_text
    else:
        return None

def pretty_print_json(file_to_serialize):
    print(json.dumps(file_to_serialize, indent=4, ensure_ascii=False))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Getting pretty json')
    parser.add_argument('-p', '--path', required = True,        
                        help = 'Enter path to json file after flag -p or --path')
    namespace = parser.parse_args()

    if namespace.path:
        pretty_print_json(load_data(namespace.path))
