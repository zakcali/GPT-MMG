import spacy
import sys
import ast
from spacy.tokens import DocBin

def convert_json(source_file, destination_file):
    nlp = spacy.blank("tr")
    # the DocBin will store the example documents
    db = DocBin()

    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
        training_data = ast.literal_eval(content)  # Safely evaluate the file content as a Python literal

    for text, annotations in training_data:
        doc = nlp(text)
        for token in doc:
            print(token.idx, token.text, token.whitespace_)
        ents = []
        # Access the 'entities' list from the annotations dictionary
        for start, end, label in annotations["entities"]:
            span = doc.char_span(start, end, label=label)
            print(f"start: {start}, end: {end}, span: {span}, label: {label}")
            ents.append(span)
        doc.ents = ents
        db.add(doc)
    db.to_disk(destination_file)


arguments = sys.argv
if len(arguments) > 1:
    print("Converting spacy json file, named:", arguments[1], "into spacy docbin file")
    convert_json(arguments[1] + ".json", arguments[1] + ".spacy")
else:
    print("Converting spacy json file, named input.json into spacy docbin file, named train.spacy")
    convert_json('input.json', 'train.spacy')


