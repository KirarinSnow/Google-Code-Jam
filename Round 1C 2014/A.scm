;; Problem: Part Elf
;; Language: Scheme
;; Author: KirarinSnow
;; Usage: guile thisfile.scm <input.in >output.out


(use-modules (srfi srfi-1) (ice-9 format))

(let* ((a (iota 41))
       (b (map (lambda (j) (expt 2 j)) a)))
  (map
   (lambda (i) 
     (format #t "Case #~a: ~a~%" i
	     (let ((r (read)))
	       (if (member (denominator r) b)
		   (car (filter (lambda (k) (<= (/ 1 (expt 2 k)) r)) a))
		   "impossible"))))
   (iota (read) 1)))
