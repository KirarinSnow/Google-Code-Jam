#!/usr/bin/python
#
# Problem: Your Rank is Pure
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


MAX = 502

def choose(n, k):
    result = 1
    for i in range(1, k+1):
        result = result * (n-i+1) / i
    return result

C = []
for i in range(MAX):
    C.append([])
    for j in range(MAX):
        C[i].append(choose(i, j))

def rchoose(n, k):
    if 0 <= n < MAX and 0 <= k < MAX:
        return C[n][k]
    else:
        return choose(n, k)

A = []
for i in range(MAX):
    A.append([])
    for j in range(MAX):
        A[i].append(0)

for x in range(2,MAX):
    for y in range(x-1):
        if y == 0:
            A[x][y] = 1
        else:
            z = 0
            for i in range(y):
                d = A[y+1][i] * rchoose(x-y-2, y-i-1)
                z = (z+d)%100003
            A[x][y] = z


def compute():
    return sum(A[input()])%100003

for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
