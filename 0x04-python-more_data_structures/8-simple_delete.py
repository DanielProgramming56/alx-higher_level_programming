def simple_delete(a_dictionary, key=""):
    # Check if the key exists in the dictionary
    if key in a_dictionary:
        # If the key exists, delete it
        del a_dictionary[key]