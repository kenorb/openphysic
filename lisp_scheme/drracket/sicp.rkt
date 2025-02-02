#lang planet neil/sicp
; http://racket-lang.org/
; http://www.neilvandyke.org/racket-sicp/

; Structure and Interpretation of Computer Programs
; second edition
; http://mitpress.mit.edu/sicp/

(display "1.1 The Elements of Programming\n")

(display "1.1.1 Expressions\n")
486
(+ 137 349)
(- 1000 334)
(* 5 99)
(/ 10 5)
(/ 10 3)
(+ 2.7 10)
(+ 21 35 12 7)
(* 25 4 12)
(+ (* 3 5) (- 10 6))

(display "1.1.2 Naming and the Environment\n")
(define size 2)
(* 5 size)
(define pi 3.14159)
(* 2 pi)
(define radius 10)
(* pi (* radius radius))
(define circumference (* 2 pi radius))
circumference

(display "1.1.3 Evaluating Combinations\n")
(* (+ 2 (* 4 6))
   (+ 3 5 7))

(display "1.1.4 Compound Procedures\n")
(define (square x) (* x x))
(square 21)
(square (+ 2 5))
(square (square 3))
(define(sum-of-squares x y)
  (+ (square x) (square y)))
(sum-of-squares 3 4)

(display "1.1.5 Conditional Expressions and Predicates\n")

(display "define absolute-value procedure\n")
(define (abs x)
  (cond ((> x 0) x)
        ((= x 0) 0)
        ((< x 0) (- x))))

(abs 2)
(abs (- 2))
(abs 0)

(display "another way to write the absolute-value procedure\n")
(define (abs2 x)
  (cond ((< x 0) (- x))
        (else x)))

(abs2 2)
(abs2 (- 2))
(abs2 0)

(display "yet another way to write the absolute-value procedure\n")
(define (abs3 x)
  (if (< x 0)
      (- x)
      x))

(abs3 2)
(abs3 (- 2))
(abs3 0)

; and or not
;(and (> x 5) (< x 10))

(display "define greater-than or equal to (ge) procedure\n")
(define (>= x y)
  (or (> x y) (= x y)))

(display "another way to define greater-than or equal to (ge) procedure\n")
(define (>=2 x y)
  (not (< x y)))

(display "Exercises\n")
(display "ToDo\n")

(display "1.1.7 Example: Square Roots by Newton's Method\n")
(display "sqrt(x) = y : y such that y>=0 and y^2=x\n")

; pseudo-Lisp
;(define (sqrt x)
;  (the y (and (>= y 0)
;              (= (square y x)))))

; wa want to compute sqrt(2)
; we guess that sqrt(2) is 1 => y=1 x=2
1
; we calculate x/y
(/ 2 1)
; quotient=2
; we calculate average (of guess and x/y)
(/ (+ 1 2) 2.0)
; average=1.5

; next step
; x=previous average=1.5
(/ 2 1.5)
; quotient=1.333
(/ (+ 1.3333333333333333 1.5) 2)

; ...

; cf sqrt.rkt
;(load "sqrt.rkt")

(display "1.2 Procedures and the Processes They Generate\n")

(display "1.2.1 Linear Recursion an Iteration\n")

(display "Linear recursive process\n")

(define (factorial n)
  (if (= n 1)
      1
      (* n (factorial (- n 1)))))

(factorial 6)


(display "Linear iterative process\n")

(define (factorial-it n)
  (fact-iter 1 1 n))

(define (fact-iter product counter max-count)
  (if (> counter max-count)
      product
      (fact-iter (* counter product)
                 (+ counter 1)
                 max-count)))

(factorial-it 6)