! Problem: Picking Up Chicks
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
    n = getNumber.result
    call getNumber
    k = getNumber.result
    call getNumber
    b = getNumber.result
    call getNumber
    t = getNumber.result

    for i from 0 to n - 1
        call getNumber
        x'i' = getNumber.result
    endfor

    for i from 0 to n - 1
        call getNumber
        v'i' = getNumber.result
    endfor

    nr = 0
    nb = 0
    ans = 0
    for j from 1 to n
        i = n - j
        if nr != k
            if x'i' + t * v'i' < b
                nb = nb + 1
            else
                nr = nr + 1
                ans = ans + nb
            endif
        endif
    endfor

    if nr >= k
        .result$ = "'ans'"
    else
        .result$ = "IMPOSSIBLE"
    endif
endproc

call getNumber
cases = getNumber.result

for case from 1 to cases
    call compute
    echo Case #'case': 'compute.result$'
endfor
