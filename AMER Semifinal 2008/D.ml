(*  
 *  Problem: King
 *  Language: OCaml
 *  Author: KirarinSnow
 *  Usage: ocamlopt str.cmxa -o exec thisfile.ml && ./exec <input.in >output.out
 *  Comments: Adapted from reference solution.
 *)


open Scanf;;

let maxb = 1 lsl 16;;

let index y b = (y * maxb) + b;;

let rec solve a m x y b r c =
    if y = r then
      0
    else
      if x = c then
	solve a m 0 (y + 1) b r c
      else
	if m.(x).(index y b) <> (-1) then
	  m.(x).(index y b)
	else
	  let b2 = (b lsl 1) land ((1 lsl (c + 1)) - 1) in	     
	    if a.(y).[x] <> '.' then
	      m.(x).(index y b) <- solve a m (x + 1) y b2 r c
	    else
	      begin
		m.(x).(index y b) <-
		  solve a m (x + 1) y (b2 + 1) r c;
		
		if x != 0 && (b land 1) <> 0 then
		  m.(x).(index y b) <- max m.(x).(index y b)
		    (1 + (solve a m (x + 1) y (b2 - 2) r c));
	
		if x != 0 && (b land (1 lsl c)) <> 0 then
		  m.(x).(index y b) <- max m.(x).(index y b)
		    (1 + (solve a m (x + 1) y b2 r c));
		
		if (b land (1 lsl (c - 1))) <> 0 then
	            m.(x).(index y b) <- max m.(x).(index y b)
		      (1 + (solve a m (x + 1) y (b2 - (1 lsl c)) r c));
		
		if x < (c - 1) && (b land (1 lsl (c - 2))) <> 0 then
		    m.(x).(index y b) <- max m.(x).(index y b)
		      (1 + (solve a m (x + 1) y (b2 - (1 lsl (c - 1))) r c));
	      end;
	    m.(x).(index y b);;

let compute () =
  scanf "%d %d\n"
    (fun r c -> 
       let a = Array.create r "" in
	 for i = 0 to (r - 1) do
	   scanf "%s\n" (fun x -> a.(i) <- x)
	 done;
	 
	 let m = Array.make_matrix c (r * maxb) (-1) in
	 let m1 = solve a m 0 0 0 r c in
	   
         let a = Array.map
	   (fun l -> Str.global_replace (Str.regexp "K") "." l) a in
	   
	 let m = Array.make_matrix c (r * maxb)  (-1) in
	 let m2 = solve a m 0 0 0 r c in
	   
	   if m2 > m1 then "A" else "B"
    );;       


for i = 1 to read_int () do
  Printf.printf "Case #%d: %s\n" i (compute ());
done;;
