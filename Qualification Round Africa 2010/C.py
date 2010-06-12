#!/usr/bin/python
#
# Problem: T9 Spelling
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 



def compute():
    line = raw_input()
    out = []
    for i in line:
        if i == ' ':
            c = '0'
            d = 1
        else:
            c =         '22233344455566677778889999'[ord(i)-ord('a')]
            d = map(int,'12312312312312312341231234')[ord(i)-ord('a')]

        out.append(c*d)
        
    for j in range(1,len(out)):
        if out[j][0]==out[j-1][0]:
            out[j-1]+=' '
            
    return ''.join(out)


n = input()

for i in range(n):
    s = "Case #" + str(i+1) + ": "
    s+= compute()
    print s
