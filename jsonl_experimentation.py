import json
import os
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python jsonl_prompt_jsonl.py <input_file_jsonl> <input_file_json> <output_file>")
        sys.exit(1) 
    input_file_one = sys.argv[1] # read in the jsonl file
    input_file_two = sys.argv[2] # read in the json file
    print('main')
    index_data = None 
    with open(input_file_two, 'r') as f:
        index_data = json.load(f)
        print(len(index_data.keys()))
    idx_list = list(index_data.keys())

    count = 0 
    for line in open(input_file_one,'r'):
        data = json.loads(line)
        idx_list = list(index_data.keys())
        if 'callee_method_ids' in data.keys():
            callee_method_ids = data['callee_method_ids']
            for callee_method_id in callee_method_ids:
                if str(callee_method_id) in idx_list:
                    count += 1
                    print(index_data[str(callee_method_id)])

    print(count)
if __name__ == '__main__':
    main()