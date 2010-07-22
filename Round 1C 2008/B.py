#!/usr/bin/python
#
# Problem: Ugly Numbers
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compute():
    num = raw_input()
    d = [[0]*210]
    d[0][0] = 1
    for i in range(len(num)):
        d.append([0]*210)
        
    for i in range(len(num)):
        # starting position; compute val for all possible ending points after
        val = 0
        for j in range(i, len(num)):
            val = (val*10 + (ord(num[j])-ord('0')))%210
            
            # update table
            for k in range(210):
                for s in [1, -1]: # + or -
                    if i == 0 and s == -1:
                        break  # no negative for first position
                    
                    kk = (k + s*val)%210
                    d[j+1][kk] += d[i][k]
    
    count = 0
    for i in range(210):
        if (i%2)*(i%3)*(i%5)*(i%7) == 0:
            count += d[len(num)][i]
    return count

for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
