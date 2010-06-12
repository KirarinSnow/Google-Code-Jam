(*
 *  Problem: Old Magician
 *  Language: Standard ML
 *  Author: KirarinSnow
 *  Usage: sml thisfile.sml <input.in 1>/dev/null 2>output.out
 *)


open TextIO;

fun compute() =
    let
	val line = valOf(inputLine(stdIn));
	val wb = String.tokens (fn x => Char.isSpace x) (line);
	val b = valOf(Int.fromString(hd(tl(wb))))
    in
	if b mod 2 = 0 then "WHITE" else "BLACK"
    end;

fun each(i:int, c:int) =
    let
	val k = output(stdErr,
		concat(["Case #", Int.toString(i), ": ", compute(), "\n"]))
    in
	if (i > c-1) then () else (each(i+1, c))
    end;

val cases = valOf(inputLine(stdIn));

each(1, valOf(Int.fromString(cases)));

closeIn(stdIn);
