! Problem: Old Magician
! Language: Praat
! Author: KirarinSnow
! Usage: praat thisfile.praat <input.in >output.out 
! Comments: Praat is a phonetics analysis program with scripting capabilities,
!           available here: http://www.fon.hum.uva.nl/praat/


system cp /dev/stdin temp
name$ = "temp"
in$ < 'name$'

procedure getNumber
    .result = extractNumber (in$, "")
    in$ = replace_regex$ (in$, "^\S+[\n ]", "", 1)
endproc

procedure compute
    call getNumber
    call getNumber
    b = getNumber.result mod 2
    if b = 1
        .result$ = "BLACK"
    else
        .result$ = "WHITE"
    endif
endproc

call getNumber
cases = getNumber.result

for i from 1 to cases
    call compute
    echo Case #'i': 'compute.result$'
endfor
