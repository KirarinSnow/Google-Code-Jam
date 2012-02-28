#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# 문제: 계산식 복원 
# 언어: Python
# 저자: KirarinSnow
# 사용: python thisfile.py <input.in >output.out


def test(a, b, c, o):
    aa = ['', None]
    bb = ['', None]
    cc = ['', None]
    if o == '+':
        io = '-'
    else:
        io = '+'

    for i in range(m)[::-1]:
        cs = [[["_" for jjj in range(3)] for jj in range(2)] for j in range(2)]
        pc = [aa[0] != None, aa[1] != None]
        
        fp = ''.join(map(lambda z: ['#', '?'][z == '?'], [a[i], b[i], c[i]]))
        for cr in (0, 1):
            for pcr in (0, 1):
                if pc[pcr]:
                    if fp == '###':
                        x = eval(a[i] + o + b[i] + o + str(pcr))
                        if cr == [1, 0][0 <= x <= 9]:
                            if x%10 == int(c[i]):
                                cs[cr][pcr] = [a[i], b[i], c[i]]
                    elif fp == '?##':
                        x = eval(c[i] + io + b[i] + io + str(pcr))
                        if cr == [1, 0][0 <= x <= 9]:
                            cs[cr][pcr] = [str(x%10), b[i], c[i]]
                    elif fp == '#?#':
                        if o == '+':
                            x = int(c[i]) - int(a[i]) - pcr
                        else:
                            x = int(a[i]) - int(c[i]) - pcr
                        if cr == [1, 0][0 <= x <= 9]:
                            cs[cr][pcr] = [a[i], str(x%10), c[i]]
                    elif fp == '##?':
                        x = eval(a[i] + o + b[i] + o + str(pcr))
                        if cr == [1, 0][0 <= x <= 9]:
                            cs[cr][pcr] = [a[i], b[i], str(x%10)]
                    elif fp == '??#':
                        if cr == 0:
                            if o == '+' and int(c[i]) >= pcr:
                                cs[cr][pcr] = ['0', str(int(c[i])-pcr), c[i]]
                            if o == '-' and int(c[i]) <= 9-pcr:
                                cs[cr][pcr] = [str(int(c[i])+pcr), '0', c[i]]
                        else:
                            if o == '+' and int(c[i]) <= 8+pcr:
                                cs[cr][pcr] = [str(int(c[i])-pcr+1), '9', c[i]]
                            if o == '-' and int(c[i]) >= 1-pcr:
                                cs[cr][pcr] = ['0', str(10-pcr-int(c[i])), c[i]]
                    elif fp == '#??':
                        if cr == 0:
                            if o == '+' and int(a[i]) <= 9-pcr:
                                cs[cr][pcr] = [a[i], '0', str(int(a[i])+pcr)]
                            if o == '-' and int(a[i]) >= pcr:
                                cs[cr][pcr] = [a[i], '0', str(int(a[i])-pcr)]
                        else:
                            if o == '+' and int(a[i]) >= 1-pcr:
                                cs[cr][pcr] = [a[i], str(10-pcr-int(a[i])), '0']
                            if o == '-' and int(a[i]) <= 8+pcr:
                                cs[cr][pcr] = [a[i], str(int(a[i])+1-pcr), '9']
                    elif fp == '?#?':
                        if cr == 0:
                            if o == '+' and int(b[i]) <= 9-pcr:
                                cs[cr][pcr] = ['0', b[i], str(int(b[i])+pcr)]
                            if o == '-' and int(b[i]) <= 9-pcr:
                                cs[cr][pcr] = [str(int(b[i])+pcr), b[i], '0']
                        else:
                            if o == '+' and int(b[i]) >= 1-pcr:
                                cs[cr][pcr] = [str(10-pcr-int(b[i])), b[i], '0']
                            if o == '-' and int(b[i]) >= 1-pcr:
                                cs[cr][pcr] = ['0', b[i], str(10-pcr-int(b[i]))]
                    else:
                        if cr == 0:
                            if o == '+':
                                cs[cr][pcr] = ['0', '0', str(pcr)]
                            if o == '-':
                                cs[cr][pcr] = [str(pcr), '0', '0']
                        else:
                            if o == '+':
                                cs[cr][pcr] = [str(1-pcr), '9', '0']
                            if o == '-':
                                cs[cr][pcr] = ['0', str(1-pcr), '9']
                
        f = [-1]*2
        aaa = list(aa)
        bbb = list(bb)
        ccc = list(cc)

        for cr in (0, 1):
            d = "_"
            dd = ''
            for pcr in (0, 1):
                if aaa[pcr] != None:
                    e = cs[cr][pcr][0] + aaa[pcr] + \
                        cs[cr][pcr][1] + bbb[pcr] + \
                        cs[cr][pcr][2] + ccc[pcr]
                    ee = ''.join(cs[cr][pcr])
                    if e < d:
                        f[cr] = pcr
                        d = e
                        dd = ee

            if f[cr] != -1:
                aa[cr] = dd[0] + aaa[f[cr]]
                bb[cr] = dd[1] + bbb[f[cr]]
                cc[cr] = dd[2] + ccc[f[cr]]

        for cr in (0, 1):
            if f[cr] == -1:
                aa[cr] = bb[cr] = cc[cr] = None
    if aa[0] == None:
        return None
    else:
        a, b, c = map(lambda x: max('0', x.lstrip('0')), [aa[0], bb[0], cc[0]])
        return "%s %s %s = %s" % (a, o, b, c)

for case in range(1, input()+1):
    y = raw_input()
    a, o, b, _, c = y.split(' ')

    q = [[a, b, c]]
    if a[0] == '?':
        x = []
        for i in q:
            ai, bi, ci = i
            for j in range(1, 10):
                x.append([str(j) + ai[1:], bi, ci])
        q.extend(x)
    if b[0] == '?':
        x = []
        for i in q:
            ai, bi, ci = i
            for j in range(1, 10):
                x.append([ai, str(j) + bi[1:], ci])
        q.extend(x)
    if c[0] == '?':
        x = []
        for i in q:
            ai, bi, ci = i
            for j in range(1, 10):
                x.append([ai, bi, str(j) + ci[1:]])
        q.extend(x)

    v = []
    for i in q:
        a, b, c = i
        m = max(map(len, [a, b, c]))
        a, b, c = map(lambda x: '0'*(m-len(x))+x, [a, b, c])
        w = test(a, b, c, o)
        if w != None and len(w) == len(y):
            v.append(w)
    ans = min(v)
    
    print "Case #%d: %s" % (case, ans)
