% Problem: Watersheds
% Language: LilyPond
% Author: KirarinSnow
% Usage: lilypond thisfile.ly <input.in >output.out
% Comments: I was going to add a short piece that the interpreter would
%           turn into some pretty sheet music and a MIDI file as a side
%           effect (some would say that's LilyPond's main purpose), but I
%           unfortunately ran out of time.


\version "2.12.1"


#(define (make-row w func)
  (if (zero? w)
   '()
   (cons (func) (make-row (1- w) func))))

#(define (make-table h w func)
  (if (zero? h)
   '()
   (cons (make-row w func) (make-table (1- h) w func))))

#(define (setc! l c x)
  (if (zero? c)
   (set-car! l x)
   (setc! (cdr l) (1- c) x)))

#(define (setrc! table r c x)
  (if (zero? r)
   (setc! (car table) c x)
   (setrc! (cdr table) (1- r) c x)))

#(define (getc l c)
  (if (zero? c)
   (car l)
   (getc (cdr l) (1- c))))

#(define (getrc table r c)
  (if (zero? r)
   (getc (car table) c)
   (getrc (cdr table) (1- r) c)))

#(define (find-sink table h w r c)
  (let ((min (getrc table r c))
	(dest (list r c)))
   (if (and (positive? r) (< (getrc table (1- r) c) min))
    (begin
     (set! min (getrc table (1- r) c))
     (set! dest (list (1- r) c))))
   (if (and (positive? c) (< (getrc table r (1- c)) min))
    (begin
     (set! min (getrc table r (1- c)))
     (set! dest (list r (1- c)))))
   (if (and (< c (1- w)) (< (getrc table r (1+ c)) min))
    (begin
     (set! min (getrc table r (1+ c)))
     (set! dest (list r (1+ c)))))
   (if (and (< r (1- h)) (< (getrc table (1+ r) c) min))
    (begin
     (set! min (getrc table (1+ r) c))
     (set! dest (list (1+ r) c))))
   (if (and (= (first dest) r) (= (second dest) c))
    dest
    (find-sink table h w (first dest) (second dest)))))

#(define (nxt table h w r c)
  (let ((min (getrc table r c))
	(dest (list r c)))
   (if (and (positive? r) (< (getrc table (1- r) c) min))
    (begin
     (set! min (getrc table (1- r) c))
     (set! dest (list (1- r) c))))
   (if (and (positive? c) (< (getrc table r (1- c)) min))
    (begin
     (set! min (getrc table r (1- c)))
     (set! dest (list r (1- c)))))
   (if (and (< c (1- w)) (< (getrc table r (1+ c)) min))
    (begin
     (set! min (getrc table r (1+ c)))
     (set! dest (list r (1+ c)))))
   (if (and (< r (1- h)) (< (getrc table (1+ r) c) min))
    (begin
     (set! min (getrc table (1+ r) c))
     (set! dest (list (1+ r) c))))
   dest))
			      
#(define (adj table h w r c)
  (let ((ad '()))
   (if (and (positive? r) (equal? (nxt table h w (1- r) c) (list r c)))
    (set! ad (append ad (list (list (1- r) c)))))
   (if (and (positive? c) (equal? (nxt table h w r (1- c)) (list r c)))
    (set! ad (append ad (list (list r (1- c))))))
   (if (and (< c (1- w)) (equal? (nxt table h w r (1+ c)) (list r c)))
    (set! ad (append ad (list (list r (1+ c))))))
   (if (and (< r (1- h)) (equal? (nxt table h w (1+ r) c) (list r c)))
    (set! ad (append ad (list (list (1+ r) c)))))
   ad))

#(define (label table out h w q letter)
  (if (null? q)
   'done
   (let* ((rc (car q))
	  (r (car rc))
	  (c (cadr rc)))
    (if (zero? (getrc out r c))
     (begin
      (setrc! out r c letter)
      (label table out h w
       (append (cdr q) (adj table h w r c))
       letter))))))
	       
	       
#(define (compute)
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
	  (if (zero? (getrc out i j))
	   (set! letter (1+ letter)))
	  (let ((sink (find-sink mp h w i j)))
	   (label mp out h w (list sink) letter))
	  (loopc (cdr c) (1+ j)))))
       (loopr (cdr r) (1+ i)))))
    
    (map (lambda (lst)
	  (map (lambda (c)
		(format "~vc" (min c 122)))
	   lst))
     out))))
	       
#(map
  (lambda (i) (format #t "Case #~a:~%~{~{~a ~}~%~}" i (compute)))
  (iota (read) 1))
