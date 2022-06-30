#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argno = len(sys.argv)
    add = 0
    if argno > 1:
        for i in range(1,argno):
            add+=int(sys.argv[i])
    print(add)
