#!/usr/bin/python3
"""Script that fetches https://alu-intranet.hbtn.io/status using urllib"""
import urllib.request


if __name__ == "__main__":
    request = "https://intranet.hbtn.io/status"
    if request.startswith('https://'):
        request = 'https://alu-intranet.hbtn.io/status'
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
