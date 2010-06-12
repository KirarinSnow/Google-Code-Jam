#!/usr/bin/env python
#
# Problem: Alien Language
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out

import sys
from math import *
from string import *
import re


def next():
    return buffer.pop(0)

def nint():
    return int(next())
    

file = sys.stdin

buffer = file.read().split()

lth, wds, case = nint(), nint(), nint()
words = []
for i in range(wds):
    words.append(next())

test = []
for i in range(case):
    print "Case #" + str(i+1) + ":",
    test.append(next().replace(')',']').replace('(','['))
    c = 0
    for j in range(wds):
        if re.match(test[i],words[j]):
            c+=1
    print c

