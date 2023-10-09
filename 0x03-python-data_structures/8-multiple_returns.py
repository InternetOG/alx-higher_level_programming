#!/usr/bin/python3
def multiple_returns(sentence):
    if not str(sentence):
        return (0, None)
    elif sentence:
        my_tuple = (len(sentence), sentence[0])
        return my_tuple
