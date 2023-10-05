import string
alphabet = string.ascii_uppercase
print(alphabet.translate(str.maketrans(alphabet, alphabet + '\n')))
