import json
import sys
import re
from IPython.display import HTML


def visualize_medical_reports(filename="all.jsonl", output_filename="all.html"):
    """
  Visualizes multiple medical reports from a .jsonl file sequentially,
  with line breaks and custom background colors, and saves to an HTML file.
  """

    # Define the HTML template
    html_output = """<!DOCTYPE html>
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
<body>
"""

    with open(filename, "r", encoding='utf-8') as f:
        for line in f:
            report_data = json.loads(line)
            text = report_data.get("text", "")
            entities = report_data.get("label", [])

            # Sort entities in reverse order
            entities = sorted(entities, key=lambda x: x[0], reverse=True)

            for start, end, label in entities:
                # Use CSS class names based on the label
                css_class = label.replace(" ", "-").replace(":", "")
                entity_html = f'<span class="{css_class}">{text[start:end]}</span>'
                text = text[:start] + entity_html + text[end:]

            # To preserve single newlines but remove consecutive ones
            text = text.replace("\n \n \n", "\n")
            text = text.replace("\n \n", "\n")
            text = re.sub(r'(\n)+', '\n', text)
            # Replace \n with \n<br> for line breaks to see in html browser
            text = text.replace("\n", "\n" + "<br>")
            # Add the formatted report to the output with two line breaks
            html_output += f"<p>{text}</p>"

    # Close the HTML body and document
    html_output += """<br><br><span style="background-color:Fuchsia;">ANAT </span><br>
<span style="background-color:DeepSkyBlue;">OBS-PRESENT </span><br>
<span style="background-color:Yellow;">OBS-ABSENT </span><br>
<span style="background-color:Gray;">OBS-UNCERTAIN </span><br>
<span style="background-color:#ED2939;">IMPRESSION </span>
"""
    html_output += "</body>\n</html>"

    # Write the HTML output to the file
    with open(output_filename, "w", encoding='utf-8') as outfile:
        outfile.write(html_output)

    return HTML(html_output)  # Also return HTML for display


arguments = sys.argv
if len(arguments) > 1:
    print("Converting doccano jsonl file, named:",arguments[1], "into html file")
    html_visualization = visualize_medical_reports(arguments[1] + ".jsonl", arguments[1] + ".html")
else:
    print("Converting doccano jsonl file, named: all.jsonl into all.html file")
    html_visualization = visualize_medical_reports()
html_visualization
