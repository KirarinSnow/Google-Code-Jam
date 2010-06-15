% Problem: Fair Warning
% Language: LilyPond
% Author: KirarinSnow
% Usage: lilypond thisfile.ly <input.in >output.out

\version "2.12.2"

#(map
  (lambda (i)
   (let ((l (map (lambda (x) (read)) (iota (read)))))
    (format #t "Case #~a: ~y" i
     (modulo (- (car l))
      (apply gcd (map (lambda (y) (- y (car l))) l))))))
  (iota(read)1))
