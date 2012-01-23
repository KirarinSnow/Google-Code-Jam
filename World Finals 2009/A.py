#!/usr/bin/python
#
# Problem: Year of More Code Jam
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


from fractions import Fraction

def compute():
    n, t = map(int, raw_input().split())
    rd = [map(int, raw_input().split()) for i in range(t)]
    rd = map(lambda x: [1] + x[1:], rd)
    ds = [0] * t

    inc = {}
    inct = {}
    
    for ii, i in enumerate(rd):
        for j in i:
            if j not in inc:
                inc[j] = 0
                inct[j] = []
            inc[j] += 1
            inct[j].append(ii)

    s = Fraction(0)
    s1 = Fraction(0)
    s2 = Fraction(0)

    for i in xrange(1, min(10001, n+1)):
        if i in inc:
            s2 = 0
            s1 += inc[i]
            for j in inct[i]:
                ds[j] += 1
            for m in range(t):
                for mm in range(m+1, t):
                    s2 += ds[m]*ds[mm]
        incr = s1/Fraction(n) + 2*s2/Fraction(n*n)
        s += incr

    if n > 10000:
        s += (n - 10000) * incr

    a = int(s)
    b = s - a
    return "%d+%d/%d" % (a, b.numerator, b.denominator)

for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
