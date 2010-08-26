#!/usr/bin/python
#
# Problem: Welcome to Code Jam
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compute():
    wc = 'welcome to code jam'
    counter = map(lambda x: [x, 0], wc)
    s = raw_input()

    for c in s:
        if c == 'w':
            counter[0][1] += 1
        for i in range(1, len(counter)):
            if c == counter[i][0]:
                counter[i][1] += counter[i-1][1]
                counter[i][1] %= 10000
    return counter[-1][1]

for i in range(input()):
    print "Case #%d: %04d" % (i+1, compute())
