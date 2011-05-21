! Problem: FreeCell Statistics
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
    pd = getNumber.result
    call getNumber
    pg = getNumber.result

    if (pg = 100 and pd < 100) or (pg = 0 and pd > 0)
        .result$ = "Broken"
    elsif pd = 0
        .result$ = "Possible"
    else
        r = 100
        while pd mod 5 = 0 or pd mod 2 = 0
          if pd mod 5 = 0
            pd = pd div 5
            if r mod 5 = 0
              r = r div 5
            endif
          endif
          if pd mod 2 = 0
            pd = pd div 2
            if r mod 2 = 0
              r = r div 2
            endif
          endif
        endwhile
        if r > n
          .result$ = "Broken"
        else
          .result$ = "Possible"
        endif
    endif
endproc

call getNumber
cases = getNumber.result

for i from 1 to cases
    call compute
    echo Case #'i': 'compute.result$'
endfor
