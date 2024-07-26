#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ Checks if the data set is a valid utf-8 encoding """
    for n in data:
        if n >= 256:
            return False
    return True
