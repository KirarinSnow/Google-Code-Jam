% Problem: Music Collection
% Language: LilyPond
% Author: KirarinSnow
% Usage: lilypond thisfile.ly <input.in >output.out


\version "2.12.3"

#(use-modules (ice-9 rdelim))

#(map-in-order
  (lambda (i)
   (format #t "Case #~a:~%~{~a~%~}" i
    (let ((s (cdr (map-in-order
		   (lambda _ (string-upcase (read-line))) (iota (1+ (read)))))))
     (map-in-order
      (lambda (t)
       (let loop ((n 0)
		  (m (string-length t))
		  (f #f)
		  (b '()))
	(if (or f (> n m))
	 (if (> (length b) 0)
	     (format "~s" (reduce (lambda (x y) (if (string< x y) x y)) "" b))
	     ":(")
	 (let ((c (filter
		   (lambda (p)
		    (= (length
			(filter (lambda (q) (string-contains q p)) s)) 1))
		   (map (lambda (x) (substring t x (+ x n)))
		    (iota (1+ (- m n)))))))
	  (loop (1+ n) m (> (length c) 0) c)))))
      s))))
  (iota (read) 1))
