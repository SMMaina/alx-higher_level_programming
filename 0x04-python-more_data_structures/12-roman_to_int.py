#!/usr/bin/python3
def roman_to_int(roman):
    addd = 0
    if roman and type(roman) is str:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for idx, value in enumerate(roman):
            if idx < len(roman) - 1 and dic[roman[idx]] < dic[roman[idx+1]]:
                addd -= dic[roman[idx]]
            else:
                addd += dic[roman[idx]]
    return addd
