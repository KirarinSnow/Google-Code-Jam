% Problem: Candy Splitting
% Language: LilyPond
% Author: KirarinSnow
% Usage: lilypond thisfile.ly <input.in >output.out


\version "2.12.1"

#(map-in-order
  (lambda (i)
   (format #t "Case #~a: ~a~%" i
    (let ((x (map-in-order (lambda _ (read)) (iota (read)))))
     (if (zero? (apply logxor x))
      (- (apply + x) (apply min x))
      "NO"))))
  (iota (read) 1))
