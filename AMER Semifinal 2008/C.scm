; Problem: Test Passing Probability
; Language: Scheme
; Author: KirarinSnow
; Usage: guile thisfile.scm <input.in >output.out


(use-modules (srfi srfi-1) (ice-9 format))


(define (trunc lst len)
  (take lst (min (length lst) len)))

(define (compute)
  (let ((m (read)))
    (let loop
	((q (read))
	 (top (list 1)))
      (if (zero? q)
	  (reduce + 0 top)
	  (loop (1- q)
		(trunc
		 (sort 
		  (concatenate
			 (map (lambda (x) (map (lambda (y) (* x y)) top))
			      (map-in-order (lambda (x) (read)) (iota 4))))
		  >) m))))))

(for-each
 (lambda (i)
   (format #t "Case #~a: ~a\n" i (compute)))
 (iota (read) 1))
