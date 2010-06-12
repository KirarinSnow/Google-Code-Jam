#!/usr/bin/python
#
# Problem: Reverse Words
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 



def compute():
    line = raw_input().split()
    return ' '.join(line[::-1])


n = input()

for i in range(n):
    s = "Case #" + str(i+1) + ": "
    s+= compute()
    print s
