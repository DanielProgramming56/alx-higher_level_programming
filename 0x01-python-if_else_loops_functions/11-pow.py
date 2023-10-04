def pow(a, b):
    result = 1

    # Handle the case when b is negative
    if b < 0:
        a = 1 / a
        b = -b

    for _ in range(b):
        result *= a

    return result

# Test the function
result = pow(2, 3)
print(result)  # Output: 8

result = pow(5, -2)
print(result)  # Output: 0.04
