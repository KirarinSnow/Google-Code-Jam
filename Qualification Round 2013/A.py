#!/usr/bin/env python
#
# Problem: Tic-Tac-Toe-Tomek
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


for case in range(int(raw_input())):
    b = [raw_input() for i in range(5)][:-1]

    u = '.' in ''.join(b)
    
    t = map(lambda x: ''.join(x), zip(*b))
    d1 = ''.join(map(lambda x, y: x[y], b, range(4)))
    d2 = ''.join(map(lambda x, y: x[3-y], b, range(4)))

    s = set(b+t+[d1, d2])

    ow = map(lambda x: 'OOOOTOOO'[x:x+4], range(5))
    xw = map(lambda x: 'XXXXTXXX'[x:x+4], range(5))

    if s.intersection(ow):
        ans = 'O won'
    elif s.intersection(xw):
        ans = 'X won'
    elif '.' in ''.join(b):
        ans = 'Game has not completed'
    else:
        ans = 'Draw'

    print "Case #%d: %s" % (case+1, ans)
