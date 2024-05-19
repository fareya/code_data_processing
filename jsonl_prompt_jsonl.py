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
    # prompt_script = "You are an expert Java programmer. Please generate a comment that describes the functionality of the following method.\n"
    prompt_script = "You are an expert Java programmer. Please generate a comment that states the functionality of the following method.\n"
    count = 0
    with open(input_file_two, 'r') as f:
        index_data = json.load(f)
    with open(output_file, 'w') as out:
        for line in open(input_file_one, 'r'):
            data = json.loads(line)
            callee_methods = data['callee_method_names']
            if callee_methods:
                print(len(callee_methods))
                count = count + 1
                print(count)
                prompt = prompt_script + "Method: " + "\n" + data['method_signature']+ data['method_implementation'] + "\n"
                final_data = {}
                final_data['prompt'] = prompt
                final_data['method_name'] = data['method_name']
                final_data['comment'] = data['comment']
                out.write(json.dumps(final_data) + '\n')

if __name__ == '__main__':
    main()