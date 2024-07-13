#!/usr/bin/python3
"""
A script that converts Markdown to HTML.
"""

import sys
import os
import re

def convert_markdown_to_html(input_file, output_file):
    """
    Converts a Markdown file to HTML and writes the output to a file.
    """
    # Check that the Markdown file exists and is a file
    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown file and convert it to HTML
    with open(input_file, encoding="utf-8") as f:
        html_lines = []
        in_unordered_list = False
        in_ordered_list = False
        in_paragraph = False
        for line in f:
            line = line.rstrip()
            # Check for Markdown headings
            match = re.match(r"^(#+) (.*)$", line)
            if match:
                if in_unordered_list:
                    html_lines.append("</ul>")
                    in_unordered_list = False
                if in_ordered_list:
                    html_lines.append("</ol>")
                    in_ordered_list = False
                if in_paragraph:
                    html_lines.append("</p>")
                    in_paragraph = False
                heading_level = len(match.group(1))
                heading_text = match.group(2)
                html_lines.append(f"<h{heading_level}>{heading_text}</h{heading_level}>")
            # Check for unordered list items
            elif line.startswith('- '):
                if in_ordered_list:
                    html_lines.append("</ol>")
                    in_ordered_list = False
                if in_paragraph:
                    html_lines.append("</p>")
                    in_paragraph = False
                if not in_unordered_list:
                    in_unordered_list = True
                    html_lines.append("<ul>")
                item_text = line[2:].strip()
                html_lines.append(f"<li>{item_text}</li>")
            # Check for ordered list items
            elif line.startswith('* '):
                if in_unordered_list:
                    html_lines.append("</ul>")
                    in_unordered_list = False
                if in_paragraph:
                    html_lines.append("</p>")
                    in_paragraph = False
                if not in_ordered_list:
                    in_ordered_list = True
                    html_lines.append("<ol>")
                item_text = line[2:].strip()
                html_lines.append(f"<li>{item_text}</li>")
            # Check for paragraph text
            else:
                if in_unordered_list:
                    html_lines.append("</ul>")
                    in_unordered_list = False
                if in_ordered_list:
                    html_lines.append("</ol>")
                    in_ordered_list = False
                if line.strip() == "":
                    if in_paragraph:
                        html_lines.append("</p>")
                        in_paragraph = False
                else:
                    if not in_paragraph:
                        in_paragraph = True
                        html_lines.append("<p>")
                    else:
                        html_lines.append("<br/>")
                    html_lines.append(line)

        if in_unordered_list:
            html_lines.append("</ul>")
        if in_ordered_list:
            html_lines.append("</ol>")
        if in_paragraph:
            html_lines.append("</p>")

    # Write the HTML output to a file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(html_lines))

if __name__ == "__main__":
    # Check that the correct number of arguments were provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Get the input and output file names from the command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert the Markdown file to HTML and write the output to a file
    convert_markdown_to_html(input_file, output_file)

    # Exit with a successful status code
    sys.exit(0)

