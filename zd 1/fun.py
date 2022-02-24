# !/usr/bin/env python3
# -*- cosing: utf-8 -*-


def figure(type=0):
    def result(a, b):
        if type:
            return (a * b) / 2
        else:
            return a * b
    return result
