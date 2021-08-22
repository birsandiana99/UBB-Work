;pornind de la o lista sa se intoarca toate perechile din lista

(defun perechi(l)
  (cond 
    ((equal (car (cdr l)) nil) nil)
    (t (cons (cons (car l) (cons (car (cdr l)) nil)) (perechi (cdr l))))
  )
)
