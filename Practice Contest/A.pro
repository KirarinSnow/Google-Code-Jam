% Problem: Old Magician
% Language: Prolog
% Author: KirarinSnow
% Usage: swipl -c thisfile.pro <input.in >output.out

loop(I, Cases) :-
    I>Cases.

loop(I, Cases) :-
    write('Case #'),
    write(I),
    write(': '),
    compute,
    nl,
    Next is I+1,
    loop(Next, Cases).

compute :-
    readln(Line),
    Line = [_,B],
    Par is B mod 2,
    test(Par).

test(Par) :-
    Par = 1,
    write('BLACK'),
    !.

test(Par) :-
    Par = 0,
    write('WHITE'),
    !.

:-
    prompt1(''),
    readln(Line),
    Line = [Cases],
    loop(1,Cases),
    halt.
