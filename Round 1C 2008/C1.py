#!/usr/bin/python
#
# Problem: Increasing Speed Limits
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


MAX = 1<<20
MOD = 1000000007

def compute():
    n, m, x, y, z = map(int, raw_input().split())
    a = []
    for i in range(m):
        a.append(input())
    
    # generate points
    s = []
    for i in range(n):
        s.append(a[i%m])
        a[i%m] = (x*a[i%m] + y*(i+1))%z
    
    # sort into binary-indexed tree keys
    ss = list(set(s))
    ss.sort()
    m = {}
    for i in range(len(ss)):
        m[ss[i]] = (MAX>>1)+i  # index of corresponding leaf
     
    # initialize tree; update for each position right to left
    tree = [0]*MAX
    total = 0
    for i in range(n)[::-1]:
        val = m[s[i]]

        # count greater sequences
        v = val
        count = 1 # singleton sequence
        while v > 0:
            if v%2 == 0: # left branch, add to count right branch of parent
                count += tree[v+1]
                count %= MOD
            v /= 2

        # update count for current val
        v = val
        while v > 0:
            tree[v] += count
            tree[v] %= MOD
            v /= 2
        
        # add to total
        total += count
        total %= MOD

    return total

for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
