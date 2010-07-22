\\ Problem: Triangle Areas
\\ Language: PARI/GP
\\ Author: KirarinSnow
\\ Usage: gp -f -q thisfile.gp <input.in >output.out
\\ Comments: PARI/GP: http://pari.math.u-bordeaux.fr/




\\ convert input file to PARI/GP-readable format...

file = extern("sed -e 's/^/[/g;s/$/],/g;s/ /,/g;' /dev/stdin | tr -d '\n' | sed -e '1 s/^/[/; $ s/,$/]/'"); 



cases = file[1][1];

for (i = 1, cases, \
       print1("Case #"); \
       print1(i); \
       print1(": "); \
       ii = i + 1; \
       line = file[ii]; \
       n = line[1]; \
       m = line[2]; \
       a = line[3]; \
       if (a > n*m, \
       	  print1("IMPOSSIBLE")); \
       if (a <= n*m, \
          print1("0 1 "); \
	  print1(n); \
	  print1(" 0 "); \
	  print1((a-1)%n+1); \
	  print1(" "); \
	  print1(floor((a-1)/n)+1)); \
       print1("\n");)

quit();
