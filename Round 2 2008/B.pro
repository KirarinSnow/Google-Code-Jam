% Problem: Triangle Areas
% Language: Prolog
% Author: KirarinSnow
% Usage: swipl -s thisfile.pro < input.in > output.out

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
    Line = [N,M,A],
    test(N,M,A).

test(N,M,A) :-
    Max is N*M,
    A > Max,
    write('IMPOSSIBLE'),
    !.

test(N,M,A) :-
    write('0 1 '),
    write(N),
    write(' 0 '),
    X is (A-1) mod N + 1,
    Y is (A-1) // N + 1,
    write(X),
    write(' '),
    write(Y),
    !.

:-
    prompt1(''),
    readln(Line),
    Line = [Cases],
    loop(1,Cases),
    halt.
