#!/usr/bin/python
#
# Problem: Store Credit
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 



def compute():
    c = input()
    i = input()
    prices = map(int,raw_input().split())

    results = []

    for j in range(len(prices)):
        if c-prices[j] in prices:
            results.append(j+1)

    if len(results) > 2: # double-counted
        results2 = []
        for k in range(len(results)):
            if prices[results[k]-1] != c/2:
                results2.append(results[k])
        results = results2

    return ' '.join(map(str,results))


n = input()

for i in range(n):
    s = "Case #" + str(i+1) + ": "
    s+= compute()
    print s
