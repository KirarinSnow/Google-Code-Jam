% Problem: Store Credit
% Language: Prolog
% Author: KirarinSnow
% Usage: swipl -q -c thisfile.pro <input.in >output.out


compute(Case, Cases) :-
    readln([Credit]),
    readln(_),
    readln(Line),
    member(Item, Line),
    Match is Credit - Item,
    member(Match, Line),
    nth1(Index1, Line, Item),
    nth1(Index2, Line, Match),
    Index1 < Index2,
    format('Case #~d: ~d ~d~n', [Case, Index1, Index2]),
    Case < Cases.

:-
    prompt1(''),
    readln([Cases]),
    between(1, Cases, Case),
    \+compute(Case, Cases).
