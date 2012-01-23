; Problem: Year of More Code Jam
; Language: Scheme
; Author: KirarinSnow
; Usage: guile thisfile.scm <input.in >output.out
; Comments: Too slow for large.


(use-modules (srfi srfi-1) (ice-9 format) (ice-9 poe))


(define (compute)
  (let* ((n (read))
	 (t (read))
	 (rd (list->vector
	      (map (lambda (x)
		     (cons 1 (map (lambda (y) (read))
				  (iota (1- (read))))))
		   (iota t))))
	 
	 (d (lambda (i j)
	      (let* ((l (vector-ref rd j))
		     (v (list-index (lambda (x) (> x i)) (vector-ref rd j))))
		(if v v (length l)))))
		   
	 (day (lambda (i)
		(let lt ((j 0)
			 (ts 0))
		  (if (>= j t)
		      ts
		      (lt (1+ j)
			  (+ ts
			     (/ (d i j) n)
			     (* 2
				(let lu ((k (1+ j))
					 (us 0))
				  (if (>= k t)
				      us
				      (lu (1+ k)
					  (+ us
					     (/ (* (d i j) (d i k)) 
						(* n n)))))))))))))

	 (fin (lambda (i x)
		(if (<= i 10000)
		    x
		    (+ x (* (- n 10000) (day 10001))))))
	 (fmt (lambda (x)
		(let* ((a (floor x))
		       (b (- x a)))
		  (format "~a+~a/~a" a (numerator b) (denominator b))))))
    
    (let ld ((i 1)
	     (s 0))
      (if (or (> i n) (> i 10000))
	  (fmt (fin i s))
	  (ld (1+ i)
	      (+ s (day i)))))))

(map
 (lambda (i)
   (format #t "Case #~a: ~a\n" i (compute)))
 (iota (read) 1))
