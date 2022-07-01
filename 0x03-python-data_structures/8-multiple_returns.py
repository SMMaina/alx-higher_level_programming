#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        a = None
    else:
        a = sentence[0]
    newtuple = (len(sentence), a)
    return (newtuple)
