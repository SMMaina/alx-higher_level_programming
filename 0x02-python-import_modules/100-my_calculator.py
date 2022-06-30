#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    sign = '+-*/'
    argno = len(sys.argv) - 1
    error = ["Usage: ./100-my_calculator.py <a> <operator> <b>",
             "Unknown operator. Available operators: +, -, * and /"]
    if argno == 3:
        if sys.argv[2] in sign:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            if sys.argv[2] == sign[0]:
                print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
            if sys.argv[2] == sign[1]:
                print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
            if sys.argv[2] == sign[2]:
                print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
            if sys.argv[2] == sign[3]:
                print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        else:
            print("{}".format{error[1]))
            exit(1)
    else:
        print("{}".format(arror[0]))
        exit(1)

