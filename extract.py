# Entity parser to create y_predict values to be used with scikitlearn, to calculate F1 scores

import csv, os
from bs4 import BeautifulSoup

def mark_plain_text(html_content):
    """
    Finds plain text within the  and wraps it in  tags, excluding specific terms.

    Args:
        html_content (str): The HTML content to process.

    Returns:
        str: The modified HTML content with marked plain text.
    """

    excluded_terms = [", ", ". (", ". )", ").", "(.",".) (", ".(", ".)", ".", " ", "ve", "veya", "ya da", "<br>", "-", "", ";", ",", "\"\"\"", "(", ")", ":", ". ", "?)", ") (", ". \n-"]  # Terms to exclude

    soup = BeautifulSoup(html_content, 'html.parser')
    body = soup.find('body')

    for text_node in body.find_all(string=True):
        text = text_node.string.strip()  # Remove leading/trailing spaces

        # Check if it's plain text and not an excluded term
        if not text_node.parent.name == 'span' and \
           ('class' not in text_node.parent.attrs and 'style' not in text_node.parent.attrs) and \
           text not in excluded_terms:
            new_span = soup.new_tag('span', attrs={'class': 'O'})
            new_span.string = text_node.string
            text_node.replace_with(new_span)

    return str(soup)

def extract_entities(html_content, prefix_filename):
    """
    Extracts entities marked with "<span class=" from an HTML file.

    Args:
        html_content (str): HTML text

    Returns:
        list: A list of entities, where each entity is a dictionary with
              keys "class" and "text".
    """

    soup = BeautifulSoup(html_content, 'html.parser')
    entities = []

    for span in soup.find_all('span'):
        if 'class' in span.attrs:
            entity = {
                'class': span['class'],
                'text': span.text.strip(),
                'filename': prefix_filename
            }
            entities.append(entity)

    return entities

def write_entities_to_csv(entities, csv_file):
    """
    Writes the extracted entities to a CSV file.

    Args:
        entities (list): A list of entities (dictionaries).
        csv_file (str): Path to the CSV file.
    """

    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')  # Use tab delimiter
        writer.writerow(['class', 'text', 'filename'])  # Write header
        for entity in entities:
            # Convert class list to a comma-separated string (if needed)
            entity['class'] = ','.join(entity['class'])
            writer.writerow(entity.values())  # Write entity values as a row

# Example usage:
csv_prefix = 'extracted-'  # Replace with your desired CSV file path
EXTENSION = '.html'

# Read HTML content and mark plain text

for htmlFilename in os.listdir('.'):
    if not htmlFilename.endswith(EXTENSION):
        continue  # skip non-html files

    with open(htmlFilename, 'r', encoding='utf-8') as f:
        html_content = f.read()
    modified_html = mark_plain_text(html_content)
    entities = extract_entities(modified_html, htmlFilename.replace('.html', '').replace('-output', ''))
    write_entities_to_csv(entities, csv_prefix+htmlFilename.replace('html', 'csv'))

    print("Entities extracted and saved to:", csv_prefix+htmlFilename.replace('html', 'csv'))
