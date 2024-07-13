#!/usr/bin/env python3

import sys
import os

def main():
    # Check if the number of arguments is less than 2
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Check if the markdown file exists
    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)
    
    # If the markdown file exists, we convert it to HTML
    with open(markdown_file, 'r') as md_file:
        markdown_content = md_file.read()
    
    # This is a very simple conversion for demonstration purposes
    html_content = markdown_content.replace('\n', '<br>')
    
    with open(output_file, 'w') as html_file:
        html_file.write(html_content)
    
    sys.exit(0)

if __name__ == "__main__":
    main()

