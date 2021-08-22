;sortarea unei liste
(defun ins(e l)
  (cond
     ((null l) (list e))
     ((< e (car l)) (cons e l))
     (t (cons (car l) (ins e (cdr l))))
  )
)
(defun sort(l)
   (cond
     ((null (cdr l)) (list (car l)))
     (t (ins (car l) (sort (cdr l))))
   )
)
