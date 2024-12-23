import glob
import sys
import os
import re

new_header = """<!DOCTYPE html>
<html lang="tr">
<head>
<style>
.ANAT {
	background-color:Fuchsia
}
.OBS-P {
	background-color:DeepSkyBlue
}
.OBS-A {
	background-color:Yellow
}
.OBS-U {
	background-color:DarkGray 
}
.IMP {
	background-color:#ED2939
}
</style>
</head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<body>"""

new_footer = """
<br><br><span style="background-color:Fuchsia;">ANATOMY, ANAT </span><br>
<span style="background-color:DeepSkyBlue;">OBSERVATION_PRESENT, OBS-P </span><br>
<span style="background-color:Yellow;">OBSERVATION_ABSENT, OBS-A </span><br>
<span style="background-color:Gray;">OBSERVATION_UNCERTAIN, OBS-U </span><br>
<span style="background-color:#ED2939;">IMPRESSION, IMP </span>
</body>
</html>
"""

anat_span = '<span style="background-color:Fuchsia;">ANATOMY, ANAT </span><br>'+'\n'
op_span = '<span style="background-color:DeepSkyBlue;">OBSERVATION_PRESENT, OBS-P </span><br>'+'\n'
oa_span = '<span style="background-color:Yellow;">OBSERVATION_ABSENT, OBS-A </span><br>'+'\n'
ou_span = '<span style="background-color:Gray;">OBSERVATION_UNCERTAIN, OBS-U </span><br>'+'\n'
imp_span = '<span style="background-color:#ED2939;">IMPRESSION, IMP </span>'+'\n'

def extract_and_wrap_text(text):
  """
  Extracts text content between <body> and </body> tags and wraps it in <p> tags.

  Args:
    text: The HTML content as a string.

  Returns:
    The modified HTML content with text wrapped in <p> tags.
  """

  # Extract text between <body> and </body> tags
  body_content = re.search(r'<p>(.*?)</p>', text, re.DOTALL).group(1)

  # Wrap the entire body content in <p> tags
  wrapped_content = f"<p>{body_content}</p>"
  return wrapped_content

def convert_html_files(input_pattern, output_file):
    html_output = new_header

    # Find all .jsonl files matching the input pattern
    files = glob.glob(input_pattern)

    for file in files:
        with open(file, 'r', encoding='utf-8') as infile:
            html_content = infile.read()
            html_content = extract_and_wrap_text(html_content)
            html_content = html_content.replace(anat_span, '')
            html_content = html_content.replace(op_span, '')
            html_content = html_content.replace(oa_span, '')
            html_content = html_content.replace(ou_span, '')
            html_content = html_content.replace(imp_span, '')

            html_content = html_content.replace('<br>\n<br>', '<br>')
            html_content = html_content.replace('<br>\n<br>', '<br>')
            html_content = html_content.replace('<br>\n<br>', '<br>')
            html_content = html_content.replace('<br><br>', '<br>')
            html_content = html_content.replace('<p>\n', '<p>')
            html_content = html_content.replace('<p>\n', '<p>')
            html_content = html_content.replace('<br></p>', '</p>')
            
            html_content = html_content.replace('-<span', '- <span')
            html_content = html_content.replace('"> ', '">')
            html_content = html_content.replace('"> ', '">')
            html_content = html_content.replace(' </span>', '</span>')
            html_content = html_content.replace(' </span>', '</span>')

            # html_content = html_content.replace('class="IMP"', 'class="IMPRESSION"')
            # html_content = html_content.replace('class="OBS-U"', 'class="OBS-UNCERTAIN"')
            # html_content = html_content.replace('class="OBS-A"', 'class="OBS-ABSENT"')
            # html_content = html_content.replace('class="OBS-P"', 'class="OBS-PRESENT"')
            html_output += html_content
    html_output += new_footer
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(html_output)

# Define input file pattern and output file path
extension_pattern = '*.html'
file_name = 'combined.html'

arguments = sys.argv
if len(arguments) > 1:
    file_name = arguments[1] + ".html"
print("Combining into file:", file_name)
PATH = 'combined'
if not os.path.exists(PATH):
    os.makedirs(PATH)

# Perform the conversion
convert_html_files(extension_pattern, PATH + '\\' + file_name)
