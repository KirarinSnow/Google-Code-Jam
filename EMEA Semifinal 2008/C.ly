% Problem: Rainbow Trees
% Language: LilyPond
% Author: KirarinSnow
% Usage: lilypond thisfile.ly <input.in >output.out


\version "2.12.3"

compute =
#(lambda ()
  (let* ((n (read))
	 (k (read))
	 (e (map (lambda (y) (list (read) (read))) (iota (1- n))))
	 (c (list->vector
	     (map (lambda (x)
		   (map (lambda (z) (if (= x (car z)) (cadr z) (car z)))
		    (filter (lambda (y) (or (= x (cadr y)) (= x (car y)))) e)))
	      (iota n 1)))))
   (let sub ((d 0)
	     (ii 1)
	     (rt 0)
	     (sn '()))
    (let* ((ch (remove (lambda (z) (member z sn)) (vector-ref c (1- ii))))
	   (nc (length ch)))
     (modulo
      (apply * (append (iota nc (- k d) -1)
		(map (lambda (ci)
		      (sub (+ nc rt) ci (min 1 (1+ rt)) (cons ii sn))) ch)))
      1000000009)))))

#(map-in-order
  (lambda (i) (format #t "Case #~a: ~y" i (compute)))
  (iota (read) 1))
