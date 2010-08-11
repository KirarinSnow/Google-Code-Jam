[
  Problem: Old Magician
  Language: Brainfuck
  Author: KirarinSnow
  Usage: bf thisfile.bf <input.in >output.out
]


READ CASE NUMBER

 ----------
[
 ++++++++++
 >>>>
 < ++++++++++ ++++++++++ ++++++++++ ++++++++++ ++++++++ >
 ,----------
]


TAPE: 0 0 0 C1 D1 0 0 C2 D2 0 0 CN DN 0 0 0 *0
DIGITS ARE IN ASCII
D1 THROUGH DN HOLD THE REMAINING CASES
C1 THROUGH CN HOLD THE CURRENT CASE NUMBER


  -

  SUM DIGITS TO DETERMINE WHETHER THERE ARE REMAINING CASES
  +[ 
      <<<[-]>>> 
      >[<<<<+>>>>-]<<<<      MOVE SUM
      <[>+>+<<-]>>[<<+>>-]<< ADD DIGIT
      >---------- ---------- ---------- ---------- -------- NORMALIZE
      <
  ]
  >++++++++++ ++++++++++ ++++++++++ ++++++++++ ++++++++

  TAPE: 0 *N 0 C1 D1 0 0 C2 D2 0 0 CN DN 0 0 0 1

  IF REMAINING CASES IS NONZERO THEN EXECUTE THIS BLOCK
  [  
     [-] <
     DECREMENT REMAINING CASES
     >>>> [>>>>]
    
     TAPE: 0 0 0 C1 D1 0 0 C2 D2 0 0 CN DN 0 0 0 1 0 0 0 *0
     
     <<<< [-]

     TAPE: 0 0 0 C1 D1 0 0 C2 D2 0 0 CN DN 0 0 0 *0

     <<<< - [>+>+<<-]>>[<<+>>-]<
     ---------- ---------- ---------- ---------- ------- (ASCII 47)
     [>[-]+<-] + > [<->-] <
     [
       IF SUBTRACTING FROM ZERO THEN CONTINUE
       [-] <
       ++++++++++ REPLACE WITH 9
       <<<< - [>+>+<<-]>>[<<+>>-]<
       ---------- ---------- ---------- ---------- ------- (ASCII 47)
       [>[-]+<-] + > [<->-] <
     ]
     
     < [<<<<] >>>> [>>>>]

     TAPE: 0 0 0 C1 D1 0 0 C2 D2 0 0 CN DN 0 0 0 *0

     
     INCREMENT CASE COUNTER
     <<<< < + [<+<+>>-]<<[>>+<<-]>
     ---------- ---------- ---------- ---------- ---------- -------- (ASCII 58)
     [<[-]+>-] + < [>-<-] >
     [
       IF ADDING TO ZERO THEN CONTINUE
       [-] >
       ---------- REPLACE WITH 0
       
       <<<< + [<+<+>>-]<<[>>+<<-]>
       ---------- ---------- ---------- ---------- ---------- --------
       [<[-]+>-] + < [>-<-] >
     ]
     
     >> [<<<<]

  C ++++++++++ ++++++++++ ++++++++++ ++++++++++ ++++++++++ ++++++++++ +++++++. 
  a ++++++++++ ++++++++++ ++++++++++. 
  s ++++++++++ ++++++++.
  e ---------- ----.
    ---------- ---------- ---------- ---------- ---------- ----------
    ---------.
  # +++.
    [-]


     PRINT DIGITS OF CASE NUMBER

     TAPE: *0 0 0 C1 D1 0 0 C2 D2 0 0 CN DN 0 0 0 0

     SKIP LEADING ZEROES

     >>> [<+<+>>-]<<[>>+<<-]>
     ---------- ---------- ---------- ---------- -------- (ASCII 48)
     [<[-]+>-]+<[>-<-]>
     [
         [-]
         >>>> > [<+<+>>-]<<[>>+<<-]>
         ---------- ---------- ---------- ---------- -------- (ASCII 48)
         [<[-]+>-]+<[>-<-]>
     ]
     
     >> [<.> >>>>]


 : ++++++++++ ++++++++++ ++++++++++ ++++++++++ ++++++++++ ++++++++. 
   ---------- ---------- ------.
   [-]

     >
     MAIN CASE

     TAPE: (OTHER STUFF) *0
     
     ----------
     [
        ++++++++++
        >[-]<
        [>+<-]      COPY CHARACTER TO NEXT CELL; TERMINATE WITH NEWLINE
        ,----------
     ]
  

     > ---------- ---------- ---------- ---------- -------- NORMALIZE
     > + <  INITIALIZE PARITY BIT PAIR: 1 0 = EVEN; 0 1 = ODD
     [>[->+>]>[-<+>>>]<<<<-] FLIP BIT WHILE DECREMENTING LAST DIGIT
     
     >
     [
         -
         PRINT 'WHITE'
         ++++++++++ ++++++++++ ++++++++++ ++++++++++ ++++++++++
                    ++++++++++ ++++++++++ ++++++++++ +++++++.
         ---------- -----.
         +.
         ++++++++++ +.
         ---------- -----.[-]
     ]
     >
     [
         -
         PRINT 'BLACK'
         ++++++++++ ++++++++++ ++++++++++ ++++++++++ ++++++++++
                    ++++++++++ ++++++.
         ++++++++++.
         ---------- -.
         ++.
         ++++++++.[-]
     ]
     <<<
     
     END MAIN     
     <


     +++++ +++++ . [-]  PRINT NEWLINE

     SUM DIGITS TO DETERMINE WHETHER THERE ARE REMAINING CASES
     +[ 
         <<<[-]>>> 
         >[<<<<+>>>>-]<<<<      MOVE SUM
         <[>+>+<<-]>>[<<+>>-]<< ADD DIGIT
         >---------- ---------- ---------- ---------- -------- NORMALIZE
         <
     ]
     >++++++++++ ++++++++++ ++++++++++ ++++++++++ ++++++++
   
     TAPE: 0 *N 0 C1 D1 0 0 C2 D2 0 0 CN DN 0 0 0 1
  ]
