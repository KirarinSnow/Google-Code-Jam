#!/usr/bin/env python
#
# Problem: Treasure
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Definitely doesn't work on the large.


for case in range(int(raw_input())):
    k, n = map(int, raw_input().split())
    ks = map(int, raw_input().split())
    ps = [map(int, raw_input().split()) for i in range(n)]

    os = []
    cs = []
    for i in ps:
        os.append(i.pop(0))
        cs.append(i[1:])

    ks = tuple(sorted(ks))
    q = [(ks, 0, None, None)]
    d = {}

    p = False
    while q:
        keys, op, chest, prev = q.pop()

        if (keys, op) not in d:
            d[(keys, op)] = (chest, prev)
            if op+1 == 1<<n:
                p = True
                s = (keys, op)
                break

            for i in range(n)[::-1]:
                if op&(1<<i) == 0 and os[i] in keys:
                    nks = list(keys)+cs[i]
                    nks.remove(os[i])
                    nks = tuple(sorted(nks))
                    nop = op ^ (1<<i)
                    q.append((nks, nop, i, (keys, op)))
    
    if p:
        r = []
        while s in d:
            chest, s = d[s]
            r.append(chest)        
        r.pop()
        ans = ' '.join(map(lambda x: str(x+1), r[::-1]))
    else:
        ans = 'IMPOSSIBLE'
    
    print "Case #%d: %s" % (case+1, ans)
