#!/usr/bin/python3
import string
print(string.ascii_uppercase.translate(
    str.maketrans("", "", string.ascii_lowercase)))
