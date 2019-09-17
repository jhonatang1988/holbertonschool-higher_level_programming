#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0:
        ch = sentence[0]
    else:
        ch = None
    new_tuple = len(sentence), ch
    return new_tuple
