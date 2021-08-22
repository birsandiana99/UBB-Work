;maximul atomilor numerici de la nivelul superficial al unei liste
(defun maxim(l)
  (cond 
     ((null l) 0) ;daca lista e vida, returnez 0
     ((not (numberp (car l))) (maxim (cdr l)))
     ((and (numberp (car l)) (> (car l) (maxim (cdr l)))) (car l))
     (t (maxim (cdr l)))
  )
)
