;; Problem: Lawnmower
;; Language: Scheme
;; Author: KirarinSnow
;; Usage: guile thisfile.scm <input.in >output.out


(use-modules (srfi srfi-1) (ice-9 format))

(map
 (lambda (i) 
   (format #t "Case #~a: ~:[YES~;NO~]~%" i
	   (let ((n (read))
		 (m (read)))
	     (let ((b (map
		       (lambda (x)
			 (map
			  (lambda (y) (read))
			  (iota m)))
		       (iota n))))
	       (let ((t (apply map list b)))
		 (> (length
		     (filter
		      (lambda (x)
			(let ((r (quotient x m))
			      (c (remainder x m)))
			  (let ((p (list-ref (list-ref b r) c)))
			    (and (not (= p (apply max (list-ref b r))))
				 (not (= p (apply max (list-ref t c))))))))
		      (iota (* n m))))
		    0))))))
 (iota (read) 1))
