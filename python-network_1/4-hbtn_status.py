#!/usr/bin/python3
"""
Python script that fetches an URL with requests package
"""
import requests


if __name__ == "__main__":
    r = 'https://intranet.hbtn.io/status'
    if r.startswith('https://'):
        r = "https://alu-intranet.hbtn.io/status"
    t = requests.get(r).text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(t), t))
