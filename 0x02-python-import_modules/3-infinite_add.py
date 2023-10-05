#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add
    from sys import argv
    count = 0
    lenArgv = len(argv) - 1
    for i in range(1, lenArgv + 1):
        count += int(argv[i])
    print("{}".format(count))
