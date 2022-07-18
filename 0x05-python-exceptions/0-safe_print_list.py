#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printno = 0
    for item in range(x):
        try:
            print(my_list[item], end='')
            printno += 1
        except:
            break
        print()
        return (printno)
