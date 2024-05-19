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
    with open('output_file.jsonl', 'a') as out:
        for line in open(input_file_one, 'r'):
            x = x +1 
            if x == 10:
                break

            print('x:', x)
            count = count + 1
            data = json.loads(line)
            prompt = prompt_script + "Method:\n " + data['method_signature'] + data['method_implementation'] + "\n"
            callee_methods = data['callee_method_names']
            print(callee_methods)
            if(x==2):
                print(index_data['AminoAcidCompoundSet.getCompoundForString'])
            if callee_methods:
                print(len(callee_methods))
                for method in callee_methods:
                    any_method_in_keys = any(method in s for s in all_keys)
                    if any_method_in_keys:
                        if method in all_keys:
                            print("method is in keys")
                            callee_method_signature = index_data[method]['method_signature']
                            callee_method_body = index_data[method]['method_implementation']
                            prompt = prompt + "Callee Method:\n " + callee_method_signature + callee_method_body + "\n"
                            final_data['prompt'] = prompt
                            final_data['method_name'] = data['method_name']
                            final_data['comment'] = data['comment']
                            print(final_data)
                    out.write(json.dumps(final_data) + '\n')

if __name__ == '__main__':
    main()

