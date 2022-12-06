#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != '':
        first_chr = sentence[0]
    else:
        sentence = None
    return (len(sentence), first_chr)
