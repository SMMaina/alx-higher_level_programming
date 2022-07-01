#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "at school, i leanrt c!"
length, first = multiple_returns(sentence)
print("length: {:d} - first character: {}".format(length, first))
