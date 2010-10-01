dnl  Problem: Decision Tree
dnl  Language: m4
dnl  Author: KirarinSnow
dnl  Usage: m4 thisfile.m4 <input.in >output.out
dnl  Comments: Uses bc. Fails on sample input.
dnl
dnl
define(T, `translit($@)')dnl
define(Q, `patsubst($@)')dnl
define(I, 0)dnl
Q(T(T(T(Q(Q(Q(Q(Q(Q(T(include(/dev/stdin), (), <>),
                    >\s*>, >>),
                  >\s*<, >;),
                \([a-z]+\)\s*<, `*ifElsE<rEgExp<P;``````` \1 ''''''';0>;0;<'),
              ^<, `defiNe<````I';iNcr<I>>\\"Case `#'I:\\"defiNe<`A'''';'),
            ^[0-9]*),
          .+ [0-9]+.*, `dEfiNE<```P';`\& '''>A'),
        <>;N, `(),n'),
      E, e),
    ()),
  .*, `syscmd(`echo "\&" | bc -l')')dnl
