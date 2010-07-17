\\ Problem: Numbers
\\ Language: PARI/GP
\\ Author: KirarinSnow
\\ Usage: gp -f -q thisfile.gp <input.in >output.out
\\ Comments: PARI/GP: http://pari.math.u-bordeaux.fr/
\\           Fails on large set.


\\ convert input file to PARI/GP-readable format...

file = extern("sed 's/^/[/g;s/$/],/g;s/ /,/g' /dev/stdin | tr -d '\n' | sed '1 s/^/[/; $ s/,$/]/'"); 

for(c = 1, file[1][1], cc = c + 1; \
     n = file[cc][1]; \
     o = floor(((3 + sqrt(5))^n)%1000); \
     print1("Case #"); \
     print1(c); \
     print1(": "); \
     q = Vec(Str(1000+o)); \
     print1(q[2]); \
     print1(q[3]); \
     print1(q[4]); \
     print1("\n"));

quit();
