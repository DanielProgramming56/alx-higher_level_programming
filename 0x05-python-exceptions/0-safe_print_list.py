#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for value in my_list:
        try:
            print(value, end='')
            count += 1

            if count == x:
                break

        except:
            continue
    print()

    return count
