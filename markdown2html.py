#!/usr/bin/python3
""" 
Script to convert Markdown file to HTML

Arguments:
    input_file: name of the Markdown file
    output_file: output HTML file name

Example:
    ./markdown2html.py README.md README.html
"""

import sys
import os
import markdown


"""Number of command-line args"""
if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
    sys.exit(1)

"""Extracting the args"""
markdown_file = sys.argv[1]
html_file = sys.argv[2]

if not path.exists(sys.argv[1]) or not str(sys.argv[1]).endswith(".md"):
    sys.stderr.write("Missing " + sys.argv[1] + '\n')
    sys.exit(1)

with open(markdown_file, 'r') as markdown_input:
    markdown_content = markdown_input.read()

html_content = markdown.markdown(markdown_content)
with open(html_file, 'w') as html_output:
    html_output.write(html_content)

sys.exit(0)
