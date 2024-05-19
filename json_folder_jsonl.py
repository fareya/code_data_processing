# simple code to convert a list of json files into a single jsonl file
import json
import os
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python json_to_jsonl.py <input_dir> <output_file>")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_file = sys.argv[2]
    print(f"input_dir: {input_dir}")
    print(f"output_file: {output_file}")
    with open(output_file, 'w') as out:
        for filename in os.listdir(input_dir):
            if filename.endswith('.json'):
                with open(os.path.join(input_dir, filename), 'r') as f:
                    data = json.load(f)
                    data['filename'] = filename
                    out.write(json.dumps(data) + '\n')


if __name__ == '__main__':
    main()