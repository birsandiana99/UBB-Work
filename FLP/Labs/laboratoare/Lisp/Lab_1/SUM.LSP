(defun sum(l i n)
 (cond 
   ((> i n) 0)
   (t (+ (car l) (sum (cdr l) (+ i 1) n)))
  )
)
(defun suma(l)
  (sum l 1 (length l))
)
