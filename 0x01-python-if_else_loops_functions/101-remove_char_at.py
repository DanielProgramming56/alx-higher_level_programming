#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        # Check if the index is out of range
        return str
    else:
        return str[:n] + str[n+1:]
