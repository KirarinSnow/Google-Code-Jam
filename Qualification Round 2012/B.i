PLEASE NOTE  Problem: Dancing With the Googlers
PLEASE NOTE  Language: INTERCAL
PLEASE NOTE  Author: KirarinSnow
PLEASE NOTE  Usage: ick -b thisfile.i && ./thisfile <input.in >output.out 
PLEASE NOTE  Comments: Using C-INTERCAL.


DO NOTE  initialize input (.4) and output (.5) heads
DO .4 <- #0
DO .5 <- #0

DO NOTE  case no. (.8), total cases (.9)
PLEASE DO .8 <- #0
DO (20) NEXT
DO .9 <- :3

DO NOTE  restart main loop
PLEASE DO COME FROM (10)

DO NOTE  increment case counter
DO .1 <- .8
DO (1020) NEXT
PLEASE DO .8 <- .1

DO NOTE  print "Case #X: "
DO .1 <- #67
DO (30) NEXT
PLEASE DO .1 <- #97
DO (30) NEXT
DO .1 <- #115
DO (30) NEXT
PLEASE DO .1 <- #101
DO (30) NEXT
DO .1 <- #32
DO (30) NEXT
PLEASE DO .1 <- #35
DO (30) NEXT
DO :4 <- .8
DO (40) NEXT
PLEASE DO .1 <- #58
DO (30) NEXT
DO .1 <- #32
DO (30) NEXT

DO NOTE  handle test case
DO (100) NEXT

DO NOTE  print newline
DO .1 <- #10
PLEASE DO (30) NEXT

DO NOTE  check test case limit
(10) DO (11) NEXT
(11) DO (12) NEXT
PLEASE DO GIVE UP
(12) DO .3 <- "?'.8$.9'"~'#0$#65535'
DO .1 <- '.3~.3'~#1
DO (1020) NEXT
PLEASE DO RESUME .1

DO NOTE  FUNCTION read int into :3
(20) DO ,1 <- #1
DO :3 <- #0
PLEASE DO COME FROM (23)
DO WRITE IN ,1
DO .2 <- ,1 SUB #1
DO .1 <- .4
PLEASE DO (1000) NEXT
DO .4 <- .3~#255
DO (21) NEXT
DO :1 <- :3
PLEASE DO :2 <- #10
DO (1540) NEXT
DO :1 <- :3
DO :2 <- .4
PLEASE DO (1500) NEXT
DO :1 <- :3
DO :2 <- #48
(23) DO (1510) NEXT
(21) PLEASE DO (22) NEXT
DO FORGET #1
DO RESUME #1
(22) DO .1 <- .4~#16
PLEASE DO (1020) NEXT
DO RESUME .1

DO NOTE  FUNCTION write char from .1
(30) DO ,1 <- #1
PLEASE DO .1 <- '.1~#15'$'.1~#240'
DO .1 <- '.1~#15'$'.1~#240'
DO .2 <- '.1~#15'$'.1~#240'
DO .1 <- '#128$.5'~#54613
PLEASE DO (1010) NEXT
DO .5 <- .2
DO .2 <- .3~#255
DO ,1 SUB #1 <- .2
PLEASE DO READ OUT ,1
DO RESUME #1

DO NOTE  FUNCTION write integer from :4
(40) DO .6 <- #0
PLEASE DO COME FROM (43)
DO :1 <- :4
DO :2 <- #10
DO (1550) NEXT
PLEASE DO :1 <- :3
DO (1540) NEXT
DO :2 <- :3
DO :3 <- :1
PLEASE DO :1 <- :4
DO :4 <- :3
DO (1510) NEXT
DO STASH :3
PLEASE DO .1 <- .6
DO (1020) NEXT
DO .6 <- .1
(43) DO (41) NEXT
(41) PLEASE DO (42) NEXT
DO FORGET #1
DO COME FROM (46)
DO RETRIEVE :3
PLEASE DO .1 <- :3
DO .2 <- #48
DO (1000) NEXT
DO .1 <- .3
PLEASE DO (30) NEXT
DO .1 <- .6
DO .2 <- #1
DO (1010) NEXT
PLEASE DO .6 <- .3
(46) DO (44) NEXT
(44) DO (45) NEXT
DO FORGET #1
PLEASE DO RESUME #1
(45) DO :1 <- '.6~.6'~#1
DO :2 <- #1
DO (1500) NEXT
PLEASE DO RESUME :3
(42) DO :1 <- ':4~:4'~#1
DO :2 <- #1
DO (1500) NEXT
PLEASE DO RESUME :3

DO NOTE  FUNCTION compute solution for test case
(100) DO (20) NEXT
DO :10 <- :3
PLEASE DO (20) NEXT
DO :11 <- :3
DO (20) NEXT
DO :12 <- :3
PLEASE DO .18 <- #0
DO .19 <- :10

DO NOTE  count
DO .20 <- #0

DO NOTE  loop i=0 to N
DO COME FROM (110)

DO NOTE  increment i
DO .1 <- .18
PLEASE DO (1020) NEXT
DO .18 <- .1

DO NOTE  read integer into :13
DO (20) NEXT
PLEASE DO :13 <- :3
DO (200) NEXT

DO NOTE  check test case limit
(110) DO (111) NEXT
(111) PLEASE DO (112) NEXT
DO :4 <- .20
DO (40) NEXT
DO RESUME #2
(112) PLEASE DO .3 <- "?'.18$.19'"~'#0$#65535'
DO .1 <- '.3~.3'~#1
DO (1020) NEXT
DO RESUME .1

DO NOTE  COUNT EXISTING MATCHES
(200) DO :1 <- :13
DO :2 <- #2
DO (1500) NEXT
PLEASE DO :1 <- :3
DO :2 <- #3
DO (1550) NEXT
DO .1 <- :3
PLEASE DO .2 <- :12
DO (1010) NEXT
DO .22 <- .3
DO (201) NEXT
PLEASE DO (300) NEXT
DO RESUME #1
(201) DO (202) NEXT
DO FORGET #1
PLEASE DO .1 <- .20
DO (1020) NEXT
DO .20 <- .1
DO RESUME #1
(202) PLEASE DO .3 <- "&'.22$#32768'"~'#0$#65535'
DO .1 <- '.3~.3'~#1
DO (1020) NEXT
DO RESUME .1

DO NOTE  COUNT ADJUSTABLES
(300) DO :1 <- :13
DO :2 <- #2
DO (1500) NEXT
PLEASE DO :1 <- :3
DO :2 <- #3
DO (1550) NEXT
DO .1 <- :3
PLEASE DO .2 <- :12
DO (1010) NEXT
DO .1 <- .3
DO (1020) NEXT
PLEASE DO .23 <- .1
DO .24 <- :13
DO :1 <- .24
DO :2 <- #3
PLEASE DO (1550) NEXT
DO .1 <- :3
DO .2 <- #3
DO (1030) NEXT
PLEASE DO .25 <- .3
DO .1 <- .24
DO .2 <- .25
DO (1010) NEXT
PLEASE DO .26 <- .3
DO (301) NEXT
DO .1 <- .20
DO (1020) NEXT
PLEASE DO .20 <- .1
DO :1 <- :11
DO :2 <- #1
DO (1510) NEXT
PLEASE DO :11 <- :3
DO RESUME #1
(301) DO (302) NEXT
DO FORGET #1
PLEASE DO RESUME #1
(302) DO .3 <- "?'.26$#1'"~'#0$#65535'
DO .27 <- '.3~.3'~#1
DO .3 <- "?'.24$#0'"~'#0$#65535'
PLEASE DO .28 <- '.3~.3'~#1
DO .29 <- :11
DO .3 <- "?'.29$#0'"~'#0$#65535'
DO .29 <- '.3~.3'~#1
PLEASE DO .1 <- .22
DO (1020) NEXT
DO .30 <- .1
DO .3 <- "?'.30$#0'"~'#0$#65535'
PLEASE DO .2 <- '.3~.3'~#1
DO .1 <- #1
DO (1010) NEXT
DO .30 <- .3
PLEASE DO .3 <- "&'.27$.28'"~'#0$#65535'
DO .1 <- '.3~.3'~#1
DO .3 <- "&'.1$.29'"~'#0$#65535'
DO .1 <- '.3~.3'~#1
PLEASE DO .3 <- "&'.1$.30'"~'#0$#65535'
DO .1 <- '.3~.3'~#1
DO (1020) NEXT
DO RESUME .1
