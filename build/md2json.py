#!/usr/bin/env python3

import sys
import json


def markdown_to_json(filename, anchor):
    """Convert a Markdown file into a JSON string"""
    category = ""
    entries = []
    with open(filename) as fp:
        lines = (line.rstrip() for line in fp)
        lines = list(line for line in lines if line \
                    and line.startswith(anchor) or line.startswith('| '))
    for line in lines:
        if line.startswith(anchor):
            category = line.split()[1]
            continue
        chunks = [x.strip() for x in line.split('|')[1:-1]]
        entry = {
            'API': chunks[0],
            'Description': chunks[1],
            'Auth': None if chunks[2].upper() == 'NO' else chunks[2].strip('`'),
            'HTTPS': True if chunks[3].upper() == 'YES' else False,
            'Link': chunks[4].replace('[Go!]', '')[1:-1],
            'Category': category,
        }
        entries.append(entry)
    return json.dumps(entries)


def main():
    num_args = len(sys.argv)
    if num_args < 2:
        print("No .md file passed")
        sys.exit(1)
    if num_args < 3:
        anchor = '###'
    else:
        anchor = sys.argv[2]
    print(markdown_to_json(sys.argv[1], anchor))

if __name__ == "__main__":
    main()
