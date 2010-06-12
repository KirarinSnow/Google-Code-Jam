% Problem: Fair Warning
% Language: Prolog
% Author: KirarinSnow
% Usage: swipl -q -c thisfile.pro <input.in >output.out


gcd(X, 0, X).
gcd(0, X, X).
gcd(X, Y, D) :-	A is min(X, Y),	B is max(X, Y),	Z is B mod A, gcd(A, Z, D).

fold_gcd([], 0).
fold_gcd([H|T], X) :- fold_gcd(T, Y), gcd(H, Y, X).

fold_min([], 10**50).
fold_min([H|T], X) :- fold_min(T, Y), X is min(H, Y).

fold_diff([], _, []).
fold_diff([H|T], M, X) :- fold_diff(T, M, Y), Z is H-M, X = [Z|Y].

compute(Case, Total) :-
    readln([_|Events]),
    fold_min(Events, Min),
    fold_diff(Events, Min, Diffs),
    fold_gcd(Diffs, Gcd),
    Result is -Min mod Gcd,
    format('Case #~d: ~d~n', [Case, Result]),
    !,
    Case >= Total.

:-
    prompt1(''),
    readln([Total]),
    between(1, Total, Case),
    compute(Case, Total).
