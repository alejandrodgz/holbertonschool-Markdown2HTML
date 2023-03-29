#!/usr/bin/python3
"""
The main function of the script. It checks if the input Markdown file exists.
"""

from sys import argv, stderr, exit
from os import path


def main():
    # Check if the correct number of arguments have been passed
    if len(argv) < 3:
        stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    if not (path.exists(argv[1])):
        print("Missing " + argv[1] + "\n")
        exit(1)


if __name__ == '__main__':
    main()
