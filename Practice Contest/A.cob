000100 * Problem: Old Magician
000110 * Language: COBOL
000120 * Author: KirarinSnow
000130 * Usage: cobc -x thisfile.cob -o exec && ./exec <input.in >output.out
000140 * Comments: Only works when the number of cases has 4 digits. (???)
000150 *           Some bizarre weirdness going on here. No idea.
000160
000170
000200 IDENTIFICATION DIVISION.
000210 PROGRAM-ID. GCJ.
000220 AUTHOR. KirarinSnow.
000400 DATA DIVISION.
000410 WORKING-STORAGE SECTION.
000415 01  total            PIC 9(4).
000420 01  c                PIC 9(9).
000430 01  cstr             PIC X(9).
000440 01  cstart           PIC 9(9).
000450 01  cend             PIC 9(9).  
000500 01  ln               PIC X(99).
000510 01  sep              PIC 9(9).
000530 01  w                PIC 9(9).
000540 01  b                PIC 9(9).
000550 01  quot             PIC 9(9).
000560 01  rem              PIC 9(9).
000590 01  result           PIC X(5).
000600 PROCEDURE DIVISION.
000602     MOVE 0 TO total.
000605     ACCEPT total.
000610     MOVE 0 TO c.
000615     PERFORM total TIMES
000620	       ADD 1 TO c
000625         MOVE c TO cstr
000630	       MOVE 1 TO cstart
000640         INSPECT c TALLYING cstart FOR LEADING ZEROS
000645         SUBTRACT cstart FROM 10 GIVING cend
000650        
000700         ACCEPT ln
000705         MOVE 1 TO sep
000710         INSPECT ln TALLYING sep FOR CHARACTERS
000720             BEFORE INITIAL SPACE
000730         MOVE ln(sep:10) TO b
000740         DIVIDE b BY 2 GIVING quot REMAINDER rem
000750	       IF rem = 1
000760             MOVE "BLACK" TO result
000770         ELSE
000780             MOVE "WHITE" TO result
000790         END-IF
000800
000900         DISPLAY "Case #", cstr(cstart:cend), ": ", result
001000     END-PERFORM.
009999     STOP RUN.
