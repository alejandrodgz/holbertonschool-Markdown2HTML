#!/usr/bin/python3
"""
The main function of the script. It checks if the input Markdown file exists.
"""

from sys import argv, stderr, exit
from os import path


def main():
    def bold(string):
        i = 0
        counter = 0
        new_string = string
        for i in range(len(string) - 1):
            if string[i] == '*' and string[i + 1] == '*':
                counter += 1
                if counter == 1:
                    new_string = new_string.replace('**',"<b>", 1)
                if counter == 2:
                    counter = 0
                    new_string = new_string.replace('**',"</b>", 1)
        return(new_string)
    
    def dunndies(string):
        i = 0
        counter = 0
        new_string = string
        for i in range(len(string) - 1):
            if string[i] == '_' and string[i + 1] == '_':
                counter += 1
                if counter == 1:
                    new_string = new_string.replace('__',"<em>", 1)
                if counter == 2:
                    counter = 0
                    new_string = new_string.replace('__',"</em>", 1)
        return(new_string)
    # Check if the correct number of arguments have been passed
    if len(argv) < 3:
        stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    if not path.exists(argv[1]):
        stderr.write("Missing {}\n".format(argv[1]))
        exit(1)

    with open(argv[1], 'r') as f:
        lines = f.readlines()
        for i, line_raw in enumerate(lines):
            line = bold(dunndies(line_raw))
            if line[0] == '#':
                hash_number = line.count('#')
                heading_text = line[hash_number+1:].strip()
                with open(argv[2], 'a') as out:
                    out.write(f'<h{hash_number}>{heading_text}</h{hash_number}>\n')
            elif line[0] == '-':
                    text_list = line[2:].strip()
                    if lines[i - 1][0] != '-':
                        with open(argv[2], 'a') as out:
                            out.write(f'<ul>\n')
                    with open(argv[2], 'a')as out:
                            out.write(f'<li>{text_list}</li>\n')
                    if i >= len(lines) - 1 or lines[i + 1][0] != '-':
                        with open(argv[2], 'a') as out:
                            out.write(f'</ul>\n')
            elif line[0] == '*':
                    text_list = line[2:].strip()
                    if i == 0 or lines[i - 1][0] != '*':
                        with open(argv[2], 'a') as out:
                            out.write(f'<ol>\n')
                    with open(argv[2], 'a')as out:
                            out.write(f'<li>{text_list}</li>\n')
                    if i >= len(lines) - 1 or lines[i + 1][0] != '*':
                        with open(argv[2], 'a') as out:
                            out.write(f'</ol>\n')
            elif line[0].isalpha():
                if i == 0 or lines[i - 1] == '\n':
                    with open(argv[2], 'a') as out:
                            out.write(f'<p>\n')
                with open(argv[2], 'a')as out:
                    out.write(f'{line}')
                if i == len(lines) - 1 or lines[i + 1] == '\n':
                        with open(argv[2], 'a') as out:
                            out.write(f'</p>\n')
                else:
                    with open(argv[2], 'a') as out:
                            out.write(f'<br/>\n')
                    
 
        
                    


if __name__ == '__main__':
    main()
