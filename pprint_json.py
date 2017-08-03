import json
import os
import argparse
from pprint import pprint

def load_data():
    if os.path.isfile("raw_json.json"): 
        with open("raw_json.json", 'r', encoding='utf-8-sig') as raw_json_file:
            raw_json_file_text = json.load(raw_json_file)
            #return raw_json_file_text
            pprint(raw_json_file_text)
    else:
        print("oops")
        return None

load_data()       

# def pretty_print_json(data):
#     pass


# if __name__ == '__main__':
#     pass
