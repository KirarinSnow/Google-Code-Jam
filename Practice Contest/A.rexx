/*
 * Problem: Old Magician
 * Language: REXX
 * Author: KirarinSnow
 * Usage: regina thisfile.rexx <input.in >output.out
 */


do i=1 to linein()
    call compute i
end
exit

compute:
    out = 'Case #' || i || ': ' 
    c = linein()
    if subword(c, 2, 1) // 2 then
        out = 'BLACK'
    else
        out = 'WHITE'
    say 'Case #' || arg(1) || ':' out
    return
