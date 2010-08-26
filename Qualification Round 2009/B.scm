; Problem: Watersheds
; Language: Scheme
; Author: KirarinSnow
; Usage: guile thisfile.scm <input.in >output.out
; Comments: Actually this is basically the same as my LilyPond submission
;           for the small input set for this problem. I just took the
;           LilyPond out of it. :)
;           I was originally going to code this in Piet, but it got
;           unwieldy and bug-ridden. I did the same in PostScript, but
;           it was producing errors whose causes I couldn't pinpoint.
;           So apologies for not having a more substantial submission
;           in a different programming language, as with my solutions
;           to Problems A and C.


(use-modules (srfi srfi-1) (ice-9 format))


(define (make-row w func)
  (if (= w 0)
      '()
      (cons (func) (make-row (- w 1) func))))

(define (make-table h w func)
  (if (= h 0)
      '()
      (cons (make-row w func) (make-table (- h 1) w func))))

(define (setc! l c x)
  (if (= c 0)
      (set-car! l x)
      (setc! (cdr l) (- c 1) x)))

(define (setrc! table r c x)
  (if (= r 0)
      (setc! (car table) c x)
      (setrc! (cdr table) (- r 1) c x)))

(define (getc l c)
  (if (= c 0)
      (car l)
      (getc (cdr l) (- c 1))))

(define (getrc table r c)
  (if (= r 0)
      (getc (car table) c)
      (getrc (cdr table) (- r 1) c)))

(define (find-sink table h w r c)
  (let ((min (getrc table r c))
	(dest (list r c)))
    (if (and (> r 0) (< (getrc table (- r 1) c) min))
	(begin
	  (set! min (getrc table (- r 1) c))
	  (set! dest (list (- r 1) c))))
    (if (and (> c 0) (< (getrc table r (- c 1)) min))
	(begin
	  (set! min (getrc table r (- c 1)))
	  (set! dest (list r (- c 1)))))
    (if (and (< c (- w 1)) (< (getrc table r (+ c 1)) min))
	(begin
	  (set! min (getrc table r (+ c 1)))
	  (set! dest (list r (+ c 1)))))
    (if (and (< r (- h 1)) (< (getrc table (+ r 1) c) min))
	(begin
	  (set! min (getrc table (+ r 1) c))
	  (set! dest (list (+ r 1) c))))
    (if (and (= (car dest) r) (= (cadr dest) c))
	dest
	(find-sink table h w (car dest) (cadr dest)))))

(define (nxt table h w r c)
  (let ((min (getrc table r c))
	(dest (list r c)))
    (if (and (> r 0) (< (getrc table (- r 1) c) min))
	(begin
	  (set! min (getrc table (- r 1) c))
	  (set! dest (list (- r 1) c))))
    (if (and (> c 0) (< (getrc table r (- c 1)) min))
	(begin
	  (set! min (getrc table r (- c 1)))
	  (set! dest (list r (- c 1)))))
    (if (and (< c (- w 1)) (< (getrc table r (+ c 1)) min))
	(begin
	  (set! min (getrc table r (+ c 1)))
	  (set! dest (list r (+ c 1)))))
    (if (and (< r (- h 1)) (< (getrc table (+ r 1) c) min))
	(begin
	  (set! min (getrc table (+ r 1) c))
	  (set! dest (list (+ r 1) c))))
    dest))

(define (adj table h w r c)
  (let ((ad '()))
    (if (and (> r 0) (equal? (nxt table h w (- r 1) c) (list r c)))
	(set! ad (append ad (list (list (- r 1) c)))))
    (if (and (> c 0) (equal? (nxt table h w r (- c 1)) (list r c)))
	(set! ad (append ad (list (list r (- c 1))))))
    (if (and (< c (- w 1)) (equal? (nxt table h w r (+ c 1)) (list r c)))
	(set! ad (append ad (list (list r (+ c 1))))))
    (if (and (< r (- h 1)) (equal? (nxt table h w (+ r 1) c) (list r c)))
	(set! ad (append ad (list (list (+ r 1) c)))))
    ad))

(define (label table out h w q letter)
  (if (null? q)
      'done
      (let* ((rc (car q))
	     (r (car rc))
	     (c (cadr rc)))
	(if (= 0 (getrc out r c))
	    (begin
	      (setrc! out r c letter)
	      (label table out h w
		     (append (cdr q) (adj table h w r c))
		     letter))))))


(define (compute)
  (let ((h (read))
	(w (read))
	(letter 96))
    (let ((mp (make-table h w (lambda () (read))))
	  (out (make-table h w (lambda () 0))))
      
      (let loopr ((r mp)
		  (i 0))
	(if (null? r)
	    'done
	    (begin 
	      (let loopc ((c (car r))
			  (j 0))
		(if (null? c)
		    'done
		    (begin
		      (if (= 0 (getrc out i j))
			  (set! letter (+ letter 1)))
		      (let ((sink (find-sink mp h w i j)))
			(label mp out h w (list sink) letter))
		      (loopc (cdr c) (+ j 1)))))
	      (loopr (cdr r) (+ i 1)))))
      
      (map (lambda (lst)
	     (map (lambda (c)
		    (format "~vc" (min c 122)))
		  lst))
	   out))))

(map
 (lambda (i)
   (format #t "Case #~a:~%~{~{~a ~}~%~}" i (compute)))
 (iota (read) 1))
