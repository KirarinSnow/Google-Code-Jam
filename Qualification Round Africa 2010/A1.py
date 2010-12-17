#!/usr/bin/python
#
# Problem: Store Credit
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 


def compute():
    credit = input()
    items = input()
    prices = map(int, raw_input().split())

    s1 = set(prices)
    s2 = set(map(lambda x: credit-x, prices))
    s3 = s1.intersection(s2)

    results = [ j+1 for j in range(items) if prices[j] in s3 ]

    if len(results) > 2: # remove double-counted matches
        results = filter(lambda x: prices[x-1] != credit/2, results)
    
    return ' '.join(map(str, results))


for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
