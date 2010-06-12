\\ Problem: Old Magician
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
       w = line[1]; \
       b = line[2]; \
       if (b%2 == 1, \
       	  print1("BLACK")); \
       if (b%2 == 0, \
       	  print1("WHITE")); \
       print1("\n");)

quit();
