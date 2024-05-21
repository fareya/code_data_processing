import json
import os
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python jsonl_prompt_jsonl.py <input_file_jsonl> <input_file_json> <output_file>")
        sys.exit(1) 
    input_file_one = sys.argv[1]
    input_file_two = sys.argv[2]
    index_data = None 
    with open(input_file_two, 'r') as f:
        index_data = json.load(f)
    count = 0 
    for line in open(input_file_one,'r'):
        data = json.loads(line)
        if not('callee_method_ids' in data.keys()):
            method_names = data['callee_method_names'] 
            if len(method_names) > 0:  
                in_json = False 
                for method in method_names: 
                    if not in_json: # if we havent already found a method that is in our list of methods ... 
                        if method in index_data.keys():
                            in_json = True 
                if in_json:
                    count = count + 1  
    print(count)
if __name__ == '__main__':
    main()