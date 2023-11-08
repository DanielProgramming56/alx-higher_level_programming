#!/usr/bin/python3
"""Contain a single function that read files"""


def read_file(filename=""):
    """Reads and prints content of file"""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
