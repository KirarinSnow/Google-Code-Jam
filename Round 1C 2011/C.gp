\\ Problem: Perfect Harmony
\\ Language: PARI/GP
\\ Author: KirarinSnow
\\ Usage: gp -f -q thisfile.gp <input.in >output.out
\\ Comments: PARI/GP: http://pari.math.u-bordeaux.fr/


\\ convert input file to PARI/GP-readable format...
file = extern("sed -e 's/^/[/g;s/$/],/g;s/ /,/g;' /dev/stdin | tr -d '\n' | sed -e '1 s/^/[/; $ s/,$/]/'")

for(i = 1, file[1][1], \
  line = file[2*i]; n = line[1]; l = line[2]; h = line[3]; \
  f = concat([1], vecsort(file[2*i+1])); \
  gcds = listcreate(n+1); listput(gcds, 0); \
  for(k = 1, n, listput(gcds, gcd(gcds[#gcds], f[n-k+2]))); \
  for(x = m = 1, n+1, \
    m = lcm(m, f[x]); g = gcds[n+2-x]; \
    if(x == n+1, \
      c = if(l%m == 0, l, if(floor(l/m) < floor(h/m), m*(1+floor(l/m)), "NO")),\
      if(g%m == 0, \
        d = divisors(g/m); \
        for(dd = 1, #d, c = m*d[dd]; if(l <= c && c <= h, break(2)))))); \
  print1(Str("Case #", i, ": ", c, "\n")))

quit()
