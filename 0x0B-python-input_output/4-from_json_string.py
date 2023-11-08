#!/usr/bin/python3
"""Contain a single function """
import json


def from_json_string(my_str):
    """Returns the Str representation of an object"""
    str_json = json.loads(my_str)
    return str_json
