;substituie un elem prin altul la toate nivelurile unei liste
(defun subst(e1 e2 l)
  (cond
     ((and (atom l) (equal l e1)) (list e2))
     ((atom l) (list l))
     (t (list (mapcan '(lambda (l) (subst e1 e2 l)) l)))
  )
)

(defun sub(e1 e2 l)
  (cond
     ((and (atom l) (equal l e1)) (list e2))
     ((atom l) (list l))
     (t (list (mapcan '(subst e1 e2 l) l)))
  )
)



(defun substituie(e1 e2 l)
   (car (subst e1 e2 l))
)
