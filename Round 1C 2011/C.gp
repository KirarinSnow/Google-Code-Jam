\\ Problem: Perfect Harmony
\\ Language: PARI/GP
\\ Author: KirarinSnow
\\ Usage: gp -f -q thisfile.gp <input.in >output.out
\\ Comments: PARI/GP: http://pari.math.u-bordeaux.fr/


extern("tr ' ' '\n' < /dev/stdin > temp")
file = readvec("temp")

for(i = ii = 1, file[1], \
  n = file[ii+1]; l = file[ii+2]; h = file[ii+3]; \
  f = concat([1], vecsort(vecextract(file, vector(n, j, j+ii+3)))); \
  ii = ii+n+3; \
  gcds = vector(n+1, j, 0); \
  for(k = 1, n, gcds[k+1] = gcd(gcds[k], f[n-k+2])); \
  for(x = m = 1, n+1, \
    m = lcm(m, f[x]); g = gcds[n+2-x]; \
    if(x == n+1, \
      c = if(l%m == 0, l, if(floor(l/m) < floor(h/m), m*(1+floor(l/m)), "NO")),\
      if(g%m == 0, \
        d = divisors(g/m); \
        for(dd = 1, #d, c = m*d[dd]; if(l <= c && c <= h, break(2)))))); \
  print1(Str("Case #", i, ": ", c, "\n")))

quit()
