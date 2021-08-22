;sa se substituie un elem prin elem unei liste la toate nivelurile unei 
;liste date
(defun subst(e l1 l)
  (cond
    ((and (atom l) (equal e l)) l1)
    ((atom l) (list l))
    (t (list (mapcan '(lambda (l) (subst e l1 l)) l)))
  )
)
(defun subst_list(e l1 l)
  (car (subst e l1 l))
)
