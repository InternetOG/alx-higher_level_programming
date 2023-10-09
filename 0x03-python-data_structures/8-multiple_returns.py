#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        pass
    else:
        my_tuple = (len(sentence), sentence[0])
        return my_tuple
