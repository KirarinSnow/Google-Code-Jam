! Problem: Old Magician
! Language: Fortran
! Author: KirarinSnow
! Usage: gfortran thisfile.f95 -o exec && ./exec <input.in >output.out


FUNCTION COMPUTE() RESULT(S)
  INTEGER :: W, B
  CHARACTER(LEN=5) :: S
  READ (*,*) W, B

  IF (MOD(B, 2) == 0) THEN
     S = "WHITE"
  ELSE
     S = "BLACK"
  ENDIF
END FUNCTION COMPUTE

PROGRAM GCJ
  IMPLICIT NONE

  INTEGER :: CASES, CASE
  CHARACTER(LEN=5) :: COMPUTE
  
  READ (*,*) CASES

  DO CASE = 1, CASES
     WRITE (*, '("Case #" I0 ": " A5)') CASE, COMPUTE()
  END DO
END PROGRAM GCJ
