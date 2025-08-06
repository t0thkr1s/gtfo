#!/usr/bin/env python3
# coding=utf-8
import argparse
import json
import os
from pathlib import Path
from string import Template

from colorama import Fore, Style, init
from pygments import highlight, formatters, lexers

# Initialize colorama for Windows compatibility
init(autoreset=True)

banner = '''
         __    ___        __    _
  ___ _ / /_  / _/ ___   / /   (_)  ___   ___
 / _ `// __/ / _/ / _ \ / _ \ / /  / _ \ (_-<
 \_, / \__/ /_/   \___//_.__//_/  /_//_//___/
/___/
'''

# Get the absolute path to the data directory
PACKAGE_DIR = Path(__file__).parent
data_dir = PACKAGE_DIR / "data"
json_ext = ".json"

info = Template(Style.BRIGHT + '[ ' + Fore.GREEN + '*' + Fore.RESET + ' ] ' + Style.RESET_ALL + '$text')
fail = Template(Style.BRIGHT + '[ ' + Fore.RED + '-' + Fore.RESET + ' ] ' + Style.RESET_ALL + '$text')
title = Template(
    '\n' + Style.BRIGHT + '---------- [ ' + Fore.CYAN + '$title' + Fore.RESET + ' ] ----------' + Style.RESET_ALL + '\n'
)
description = Template(Style.DIM + '# ' + '$description' + Style.RESET_ALL)
divider = '\n' + Style.BRIGHT + ' - ' * 10 + Style.RESET_ALL + '\n'


def parse_args():
    from . import __version__
    parser = argparse.ArgumentParser(
        prog="gtfo",
        description="Command-line tool for GTFOBins - helps you bypass system security restrictions."
    )
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}')
    parser.add_argument('binary', metavar='binary', help='Unix binary to search for exploitation techniques')
    return parser.parse_args()


def run(binary=None):
    """Main function that can be called programmatically"""
    if binary is None:
        args = parse_args()
        binary = args.binary
    
    file_path = data_dir / f"{binary}{json_ext}"
    if file_path.exists():
        print(info.safe_substitute(text="Supplied binary: " + binary))
        print(info.safe_substitute(text="Please wait, loading data ... "))
        with open(file_path) as source:
            data = source.read()

        json_data = json.loads(data)
        if 'description' in json_data:
            print('\n' + description.safe_substitute(description=json_data['description']))

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


def main():
    """Console script entry point"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    run()


if __name__ == '__main__':
    main()
