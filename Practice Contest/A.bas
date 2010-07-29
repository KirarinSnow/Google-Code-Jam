10 REM  Problem: Old Magician
20 REM  Language: BASIC
30 REM  Author: KirarinSnow
40 REM  Usage: yabasic thisfile.bas <input.in >output.out
50
60
70 INPUT "" N
80 FOR I = 1 TO N
90 INPUT "" W, B
100 S$ = "WHITE"
110 IF MOD(B, 2) = 1 THEN S$ = "BLACK"
120 ENDIF
130 PRINT "Case #", I, ": ", S$
140 NEXT I
150 END
