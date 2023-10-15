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
import argparse
import pathlib
import re


if __name__ == '__main__':

    # Check the number of command-line arguments
    if len(sys.argv[1:]) != 2:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        sys.exit(1)

    # Extract arguments and store in variables
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the Markdown file exists
    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
        print(f'Missing {input_file}', file=sys.stderr)
        sys.exit(1)

    # Read the Markdown content from the file
    with open(input_file, encoding='utf-8') as f:
        html_content = []
        md_content = [line[:-1] for line in f.readlines()]
        for line in md_content:
            heading = re.split(r'#{1,6} ', line)
            if len(heading) > 1:
                # Get the level of the heading
                h_level = len(line[:line.find(heading[1])-1])
                # Append the html equivalent of the heading
                html_content.append(
                    f'<h{h_level}>{heading[1]}</h{h_level}>\n'
                )
            else:
                html_content.append(line)

    # Write the HTML content to the output file
    with open(output_file, 'w', encoding='utf-8') as f_2:
        f_2.writelines(html_content)
