#!/usr/bin/env python3
# coding=utf-8
import argparse
import json
import os
from string import Template
from colorama import Fore, Style
from pygments import highlight, formatters, lexers

banner = '''
         __    ___        __    _            
  ___ _ / /_  / _/ ___   / /   (_)  ___   ___
 / _ `// __/ / _/ / _ \ / _ \ / /  / _ \ (_-<
 \_, / \__/ /_/   \___//_.__//_/  /_//_//___/
/___/                                        
'''

data_dir = "data/"
json_ext = ".json"

info = Template(Style.BRIGHT + '[ ' + Fore.GREEN + '*' + Fore.RESET + ' ] ' + Style.RESET_ALL + '$text')
fail = Template(Style.BRIGHT + '[ ' + Fore.RED + '-' + Fore.RESET + ' ] ' + Style.RESET_ALL + '$text')
title = Template('\n' + Style.BRIGHT + '---------- [ ' + Fore.CYAN + '$title' +
                 Fore.RESET + ' ] ----------' + Style.RESET_ALL + '\n')
description = Template(Style.DIM + '# ' + '$description' + Style.RESET_ALL)
divider = '\n' + Style.BRIGHT + ' - ' * 10 + Style.RESET_ALL + '\n'


def parse_args():
    parser = argparse.ArgumentParser(usage="python3 gtfo.py [binary]",
                                     description="Command-line program for GTFOBins. "
                                                 "It helps you to bypass system security restrictions. Version 1.0")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('binary', metavar='[binary]', action='store', help='specifies the binary file')
    return parser.parse_args()


def main(binary):
    file_path = data_dir + binary + json_ext
    if os.path.isfile(file_path):
        print(info.safe_substitute(text="Supplied binary: " + binary))
        print(info.safe_substitute(text="Please wait, loading data ... \n"))
        with open(file_path) as source:
            data = source.read()

        json_data = json.loads(data)
        if 'description' in json_data:
            print(description.safe_substitute(description=json_data['description']))

        for vector in json_data['functions']:
            print(title.safe_substitute(title=str(vector).upper()))
            index = 0
            for code in json_data['functions'][vector]:
                index = index + 1
                if 'description' in code:
                    print(description.safe_substitute(description=code['description']) + '\n')
                print(highlight(code['code'], lexers.BashLexer(),
                                formatters.TerminalTrueColorFormatter(style='igor')).strip())
                if index != len(json_data['functions'][vector]):
                    print(divider)

        print('\n' + info.safe_substitute(text="Goodbye, friend."))
    else:
        print(fail.safe_substitute(text="Sorry, couldn't find anything for " + binary))


if __name__ == '__main__':
    print(banner)
    args = parse_args()
    main(binary=args.binary)
