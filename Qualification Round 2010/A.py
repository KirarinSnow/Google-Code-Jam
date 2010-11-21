#!/usr/bin/python
#
# Problem: Snapper Chain
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compute():
    n, k = map(int, raw_input().split())
    return ("ON", "OFF")[not not (k+1)%(1<<n)]

for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
