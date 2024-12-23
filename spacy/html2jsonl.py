import re
import json
import sys


def convert_html(html_file, output_file):
    """Converts HTML file with tagged entities to a custom text format.

    Args:
      html_file: Path to the input HTML file.
      output_file: Path to the output text file.
    """

    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
        # ensure correct calculations for offsets
        html_content = html_content.replace('\n', '')
        html_content = html_content.replace('<br>', '\n')

    # Split into paragraphs based on <p> tags
    paragraphs = html_content.split('<p>')[1:]  # Skip the first element
    results = []
    for paragraph_id, paragraph in enumerate(paragraphs, 1):
        paragraph = paragraph.split('</p>')[0]  # Remove closing </p> and anything after

        # --- Replace <br> and clean whitespace ---

        paragraph = ' '.join(paragraph.split(' '))

        text = ''
        labels = []
        current_index = 0

        # Find all spans with class attributes
        for match in re.finditer(r'<span class="(.*?)">(.*?)</span>', paragraph):
            label = match.group(1).strip()
            word = match.group(2).strip()

            # Add the text before the span (without extra space if unnecessary)
            text += paragraph[current_index:match.start()]
            current_index = match.end()

            start = len(text)  # Start index of the label
            text += word
            end = len(text)    # End index of the label
            labels.append([start, end, label])

        # Add any remaining text after the last span
        text += paragraph[current_index:]

        results.append({
            "id": paragraph_id,
            "text": text,
            "label": labels,
            "Comments": []
        })

    with open(output_file, 'w', encoding='utf-8') as f:
        for result in results:
            f.write(json.dumps(result, ensure_ascii=False, separators=(',', ':')) + '\n')


arguments = sys.argv
if len(arguments) > 1:
    print("Converting html file, named:", arguments[1], "into doccano jsonl format")
    convert_html(arguments[1] + ".html", arguments[1] + ".jsonl")
else:
    print("Converting html file, named input.html into doccano jsonl file named output.jsonl")
    convert_html('input.html', 'output.jsonl')
