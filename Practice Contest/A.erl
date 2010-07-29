% Problem: Old Magician
% Language: Erlang
% Author: KirarinSnow
% Usage: escript thisfile.erl <input.in >output.out


main(_) ->
    {ok, [N]} = io:fread("", "~d"),
    compute(1, N).

compute(_, 0) -> true;
compute(Case, Total) ->
    {ok, [_, B]} = io:fread("", "~d ~d"),
    if B rem 2 =:= 1 -> S = "BLACK";
       true -> S = "WHITE"
    end,
    io:fwrite("Case #~p: ~s~n", [Case, S]),
    compute(Case + 1, Total - 1).
