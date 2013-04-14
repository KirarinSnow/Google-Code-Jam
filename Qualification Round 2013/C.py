#!/usr/bin/env python
#
# Problem: Fair and Square
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


from itertools import *

# generate list of all fair and square numbers in range
s = [1, 2, 3]

s.extend([int('2'+'0'*i+'2') for i in range(49)])
s.extend([int('2'+'0'*i+'1'+'0'*i+'2') for i in range(24)])

for i in range(24):
    for j in range(2):
        for k in combinations(range(i), j):
            t = [0]*i
            for v in k:
                t[v] = 1
            l = '1'+''.join(map(str, t))
            r = l[::-1]
            s.append(int(l+'2'+r))

for i in range(25):
    for j in range(4):
        for k in combinations(range(i), j):
            t = [0]*i
            for v in k:
                t[v] = 1
            l = '1'+''.join(map(str, t))
            r = l[::-1]
            s.append(int(l+r))
            if i < 24:
                s.append(int(l+'1'+r))
                s.append(int(l+'0'+r))

s.sort()

s = map(lambda x: x*x, s)

# binary search for index in list
def search(x):
    l = 0
    u = len(s)    
    
    while u > l+1:
        m = (u+l)/2
        if x < s[m]:
            u = m
        else:
            l = m
    return l


for case in range(int(raw_input())):
    a, b = map(int, raw_input().split())

    x, y = map(search, [a, b])

    ans = y-x
    if a == s[x]:
        ans += 1
    
    print "Case #%d: %d" % (case+1, ans)
