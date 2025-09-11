#!/usr/bin/python3
"""This documents gather stats from stdin"""
import sys


def print_pretty(size, code_dict):
    """parse important data"""
    print("File size: {}".format(size))
    for key, value in sorted(code_dict.items()):
        if value != 0:
            print("{}: {}".format(key, value))


if __name__ == '__main__':
    """init code to print the parsed data"""
    size = 0
    code_dict = {"200": 0, "301": 0, "400": 0, "401": 0,
                 "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        line_counter = 0
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 9:
                continue
            line_counter += 1
            code = parts[7]
            try:
                size += int(parts[8])
            except ValueError:
                continue
            if code in code_dict:
                code_dict[code] += 1
            if line_counter % 10 == 0:
                print_pretty(size, code_dict)
        print_pretty(size, code_dict)
    except KeyboardInterrupt:
        print_pretty(size, code_dict)
        raise
