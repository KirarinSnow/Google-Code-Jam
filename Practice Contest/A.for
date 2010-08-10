\ Problem: Old Magician
\ Language: Forth
\ Author: KirarinSnow
\ Usage: gforth thisfile.for <input.in >output.out 


: GETLINE
    PAD DUP 100 STDIN READ-LINE * + EVALUATE ;

: SOLVE
    1 + 1 DO
      ." Case #" I 0 .R ." : "

      GETLINE SWAP DROP 2 MOD
      0 = IF ." WHITE" ELSE ." BLACK" THEN

      CR
    LOOP ;

GETLINE SOLVE BYE
