;multimea tuturor sublistelor unei liste liniare date
(defun subliste(l)
  (cond
     ((atom l) nil) ;daca e atom nu are subliste
     ((atom (car l)) (subliste (cdr l)))
     (t (append (cons (car l) (subliste (car l))) (subliste (cdr l))))
  )
) 
