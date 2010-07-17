; Problem: Minimum Scalar Product
; Language: Scheme
; Author: KirarinSnow
; Usage: guile thisfile.scm <input.in >output.out


(debug-set! stack 200000)
(use-modules (srfi srfi-1))


;; Read list of k items
(define (read-list k)
  (let loop
      ((lst '())
       (kk k))
    (if (= kk 0)
	(reverse lst)
	(loop (cons (read) lst) (- kk 1)))))


;; Compute solution for each case.
(define (compute)
  (let* ((k (read))
	 (a (read-list k))
	 (b (read-list k)))
    (fold-right + 0 (map * (sort a <) (sort b >)))))


;; Main loop; iterates over all cases.
(let ((n (read)))
  (let loop ((i 1))
    (if (<= i n)
	(begin	
	  ;; Display case number.
	  (display "Case #")
	  (display i)
	  (display ": ")
	  
	  ;; Compute output and return
	  (display (compute))
	  (newline)
	  
	  ;; Advance to next case.
	  (loop (+ i 1)))
	'done)))
