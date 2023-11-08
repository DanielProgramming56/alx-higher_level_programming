#!/usr/bin/python3
"""Contain a single function """
import json


def to_json_string(my_obj):
    """Returns the Str representation of an object"""
    json_obj = json.loads(my_obj)
    return json_obj
