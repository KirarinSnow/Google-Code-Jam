#!/usr/bin/python
#
# Problem: Old Magician
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 

import sys


def compute():
    w,b = map(int,file.readline().split())

    if b%2 == 0:
	return "WHITE"
    else:
        return "BLACK"

file = sys.stdin

n = int(file.readline())

for i in range(n):
    s = "Case #" + str(i+1) + ": "
    s+= compute()
    print s
