#!/usr/bin/env python
#
# Problem: Alien Language
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


import re

lth, wds, case = map(int, raw_input().split())

words = [raw_input() for i in range(wds)]

for i in range(case):
    test = raw_input().replace(')', ']').replace('(', '[')
    c = len(filter(lambda j: re.match(test, words[j]), range(wds)))
    print "Case #%d: %d" % (i+1, c)
