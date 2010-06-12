% Problem: T9 Spelling
% Language: LilyPond
% Author: KirarinSnow
% Usage: lilypond thisfile.ly <input.in >output.out


\version "2.12.2"


out = ""

total = #(read) #(read-char)

break = #(list (make-music 'RestEvent 'duration (ly:make-duration 0)))

rep = #(lambda (ch)
	  (if (eq? ch #\sp)
	      1
	      (list-ref '(1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 4 1 2 3 1 2 3 4)
	                (- (char->integer ch) 97))))

digit = #(lambda (ch)
	  (if (eq? ch #\sp)
	      0
	      (list-ref '(2 2 2 3 3 3 4 4 4 5 5 5 6 6 6 7 7 7 7 8 8 8 9 9 9 9)
	                (- (char->integer ch) 97))))

note = #(lambda (ct cd index)
	  (make-music 
	   'NoteEvent
	   'duration
	   (apply ly:make-duration
	     (case ct
	       ((1) '(0))
	       ((2) '(1))
	       ((3) '(1 0 2 3))
	       ((4) '(2))))
	   'pitch
	   (apply ly:make-pitch (pitch cd index))))

pitch = #(lambda (cd index)
	  (if (= index 0)
	      (case (quotient (+ 2 cd) 3) ; low frequency
	        ((1) (list 1 3  -18113/1000000))
	        ((2) (list 1 4 -155861/1000000))
	        ((3) (list 1 5 -279901/1000000))
	        ((0) (list 1 6 -419883/1000000)))
	      (case (abs (remainder (1- cd) 3)) ; high frequency
	        ((0) (list 2 1  249131/1000000))
	        ((1) (list 2 3 -385852/1000000))
	        ((2) (list 2 4 -517534/1000000)))))

chord = #(lambda (ch)
	  (let ((ct (rep ch))
		(cd (digit ch)))
	   (set! out (format "~a~v@{~a~:*~}x" out ct cd))
	   ((lambda (x)
	     (if (= ct 3)
	         (list (make-music 'TimeScaledMusic
			           'denominator 3
			           'numerator 2
			           'element (make-sequential-music x)))
	         x))
	    (map (lambda (x)
		  (make-music
		   'EventChord
		   'elements
		   (map (lambda (i) (note ct cd i)) (iota 2))))
	     (iota ct)))))

correct = #(lambda (in)
	    (let loop
	     ((digit 0)
	      (out in))
	     (if (> digit 9)
	         out
	         (loop (1+ digit)
	          (ly:string-substitute
		    (format "~sx~s" digit digit)
		    (format "~s ~s" digit digit) out)))))

#(let loop
    ((case 1)
     (events '()))
    (if (> case total)
        (make-sequential-music events)
        (let lineloop
	  ((ch (read-char))
	   (notes '()))
	  (if (eq? ch #\nl)
	      (begin
	        (format #t "Case #~a: ~a~&" case
		 (ly:string-substitute "x" "" (correct (correct out))))
	        (set! out "")
	        (loop (1+ case) (append events notes break)))
	      (lineloop (read-char)
	                (append notes (chord ch)))))))