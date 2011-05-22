\\ Problem: Perfect Harmony
\\ Language: PARI/GP
\\ Author: KirarinSnow
\\ Usage: gp -f -q thisfile.gp <input.in >output.out
\\ Comments: PARI/GP: http://pari.math.u-bordeaux.fr/



\\ convert input file to PARI/GP-readable format...

file = extern("sed -e 's/^/[/g;s/$/],/g;s/ /,/g;' /dev/stdin | tr -d '\n' | sed -e '1 s/^/[/; $ s/,$/]/'"); 

cases = file[1][1];

for (i = 1, cases, \
  print1("Case #"); print1(i); print1(": "); \
  ii = 2*i; line = file[ii]; \
  n = line[1]; l = line[2]; h = line[3]; \
  ii = 2*i+1; f = vecsort(file[ii]); \
  ga = listcreate(n+1); \
  gb = listcreate(n+1); \
  p = listcreate(n+1); \
  listput(p, 1); \
  listput(gb, 0); \
  for(k = 1, n, \
    listput(gb, gcd(gb[#gb], f[n-k+1])); \
    listput(p, lcm(p[#p], f[k]))); \
  b = 0; \
  for(x = 1, n, \
    m = p[x]; g = gb[n+2-x]; \
    if(g%m==0, \
      k = g / m; \
      d = divisors(k); \
      for(dd = 1, #d, \
        c = m*d[dd]; \
        if(l <= c && c <= h, \
          print1(c); b = 1; break)); \
      if (b==1, break))); \
  if(b != 1, \
    x = n+1; \
    m = p[x]; \
    if(l%m==0, print1(l), \
      if(floor(l/m) < floor(h/m), \
        print1(m*(floor(l/m)+1)), \
        print1("NO")))); \
  print1("\n"));

quit();
