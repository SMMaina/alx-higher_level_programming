#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sumd = sump = multiaxb = 0
        for tuple in my_list:
            sumd += tuple[1]
            multiaxb = tuple[0] * tuple[1]
            sump += multiaxb
        return (sump / sumd)
    return 0
