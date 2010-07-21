\\ Problem: Number Sets
\\ Language: PARI/GP
\\ Author: KirarinSnow
\\ Usage: gp -f -q thisfile.gp <input.in >output.out
\\ Comments: PARI/GP: http://pari.math.u-bordeaux.fr/
\\           Fails on large set.


\\ convert input file to PARI/GP-readable format...

a = extern("sed -e 's/^/[/g;s/$/],/g;s/ /,/g;' /dev/stdin | tr -d '\n' | sed -e '1 s/^/[/; $ s/,$/]/'");


for(c=1, a[1][1],\
    cc = c+1; \
    o = 0; \
    s = 0; \
    p = a[cc][3]; \
    aa = a[cc][1]; \
    bb = a[cc][2]; \
    b = listcreate(bb-aa+1); \
    ff = listcreate(bb-aa+1); \
    for(n = aa, bb, \
	q = 1; \
	fordiv(n,x, \
   	    if(isprime(x) && x>=p, \
	        q*=x)); \
	listput(b,q)); \
    j = 0; \
    x = 1; \
    for(k = 1, bb-aa+1, \
        cp = b[k]; \
	for(ii = 1, length(ff), \
	    if(ff[ii]!= 0 && gcd(ff[ii],cp) > 1, \
	        cp=lcm(cp,ff[ii]); \
	        ff[ii]=0)); \
	listput(ff,cp)); \
    s = 0; \
    for(d = 1, length(ff), \
        if(ff[d]!=0, \
	    s+=1)); \
    print1("Case #"); \
    print1(c); \
    print1(": "); \
    print1(s); \
    print1("\n"));

quit();
