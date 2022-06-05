#!/usr/bin/python3
def multiple_returns(sentence):
    count = len(sentence)
    if count == 0:
        first = "None"
    else:
        first = sentence[0]
    new = (count, first)
    return new
