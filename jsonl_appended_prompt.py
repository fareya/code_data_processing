# we maintain the data id here so that we can use it later, all this script does is store prompts and original code id
import json
import os
import sys
def main():
    if len(sys.argv) != 4:
        print("Usage: python jsonl_prompt_jsonl.py <input_file_jsonl> <input_file_json> <output_file>")
        sys.exit(1)

    input_file_one = sys.argv[1]
    input_file_two = sys.argv[2]
    output_file = sys.argv[3]
    print(f"input_file (jsonl): {input_file_one}")
    print(f"input_file (json): {input_file_two}")
    print(f"output_file: {output_file}")

    #prompt_script = "You are an expert Java programmer. Please generate a comment that describes the functionality of the following method given, provided callee method information.\n"
    prompt_script = "You are an expert Java programmer. Please generate a comment that states the functionality of the following method.\n"
    #prompt_script = "You are an expert Java programmer. Please generate a comment that states the functionality of the following method, provided callee method information.\n"
    final_data = {}
    count = 0 
    with open(input_file_two, 'r') as f:
        index_data = json.load(f)
    all_keys = index_data.keys() 
    x= 0   
    with open(output_file, 'a') as out:
        for line in open(input_file_one, 'r'):
            # you can change the count to see the number of prompts you want to see
            if count == 15:
                break
            data = json.loads(line)
            prompt = prompt_script + "Method:\n " + data['method_signature'] + data['method_implementation'] + "\n"
            if 'callee_method_ids' in data.keys():
                method_ids = list(set(data['callee_method_ids']))
                # we can change the method_ids to 1 if we want to see the prompt for only one callee method
                if len(method_ids) == 2:
                    count = count + 1
                    for method_id in method_ids:
                        prompt = prompt + "Callee Method:\n" + index_data[str(method_id)]['method_signature'] + index_data[str(method_id)]['method_implementation'] + "\n"
                    final_data['method_name'] = data['method_name']
                    final_data['comment'] = data['comment']
                    final_data['prompt'] = prompt
                    out.write(json.dumps(final_data) + '\n')

if __name__ == '__main__':
    main()

