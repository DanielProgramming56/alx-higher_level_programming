#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    lenArgv = len(argv)
    if (lenArgv > 1):
        a = int(argv[1])
        operator = argv[2]
        b = int(argv[3])
        if (operator == '+'):
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))
        elif (operator == '-'):
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
        elif (operator == '*'):
            print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
        elif (operator == '/'):
            print("{} {} {} = {}".format(a, operator, b, div(a, b)))
        else:
            print("{}".format('Unknown operator. Available operators: +, -, * and /'))
            exit(1)
    else:
        print("{}".format('Usage: ./100-my_calculator.py <a> <operator> <b>'))
        exit(1)
