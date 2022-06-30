#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argno = len(sys.argv) - 1
    colon = ':.'
    if argno > 0:
        if argno == 1:
            print("{:d} argument:".format(argno))
        else:
            print("{:d} arguments{:s}".format(argno, colon[0]))
        for i in range(1, argno + 1):
            print("{:d}: {:s}".format(i, sys.argv[i]))
    if argno == 0:
        print("{:d} arguments{:s}".format(argno, colon[1]))
