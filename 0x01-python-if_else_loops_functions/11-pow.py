#!/usr/bin/python3
def pow(a, b):
    result = 1

    # Handle the case when b is negative
    if b < 0:
        a = 1 / a
        b = -b

    for _ in range(b):
        result *= a

    # Round the result to 2 decimal places
    result = round(result, 2)

    return result
