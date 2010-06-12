#!/usr/bin/python
#
# Problem: Snapper Chain
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compute():
    n, k = map(int, raw_input().split())
    return ("ON", "OFF")[int('0' in ('0'*n + bin(k)[2:])[-n:])]

for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
