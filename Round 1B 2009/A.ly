% Problem: Decision Tree
% Language: LilyPond
% Author: KirarinSnow
% Usage: lilypond thisfile.ly <input.in >output.out

\version "2.12.1"

z=#define
y=#format
x=#lambda
w=#read
#(z(v a)(map a(iota(w)1)))
#(z(c f q)(*(car q)(if(any list? q)(c f((if(memq(cadr q)f)caddr cadddr)q))1)))
#(v(x(i)(w)(set! z(w))(y #t"Case #~a:
"i)(v(x(i)(w)(y #t"~y"(c(v(x(i)(w)))z))))))