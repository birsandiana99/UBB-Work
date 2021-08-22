;det produsul atomilor numerici de la nivelul superficial dintr-o lista

(defun pr_sup(l)
  (cond 
    ((null l) 1)
    ((numberp (car l)) (* (car l) (pr_sup (cdr l))))
    (t (pr_sup(cdr l)))
  )
)
