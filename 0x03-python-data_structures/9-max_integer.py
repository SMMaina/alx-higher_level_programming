#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list != []:
        lsort = sorted(my_list)
        return(lsort[-1])
    return (None)
