import json
import sys


def convert_jsonl(source_file, destination_file):
    output_data = []
    with open(source_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            data = json.loads(line)
            # Remove the "Comments" key if it exists
            if "Comments" in data:
                del data["Comments"]
            # Remove the "id" key if it exists
            if "id" in data:
                del data["id"]
            # Rename "label" to "entities"
            if "label" in data:
                data["entities"] = [(entity[0], entity[1], entity[2]) for entity in data["label"]]
                del data["label"]
            # Extract the "text" value and "entities"
            text = data["text"]
            entities = data["entities"]
            output_data.append((text, {"entities": entities}))

    with open(destination_file, 'w', encoding='utf-8') as outfile:
        outfile.write('[')
        for i, item in enumerate(output_data):
            if i > 0:
                outfile.write(',\n')
            # Write the item to the file with tuples formatted as (a, b, c)
            outfile.write(json.dumps(item, ensure_ascii=False).replace('"entities": [', '"entities": [').replace('[',
                                                                                                                 '(').replace(
                ']', ')').replace('((', '[(').replace('))', ')]'))
        outfile.write(']')


arguments = sys.argv
if len(arguments) > 1:
    print("Converting doccano jsonl file, named:", arguments[1], "into spacy json file")
    convert_jsonl(arguments[1] + ".jsonl", arguments[1] + ".json")
else:
    print("Converting doccano jsonl file, named input.jsonl into spacy json file, named output.json")
    convert_jsonl('input.jsonl', 'output.json')
