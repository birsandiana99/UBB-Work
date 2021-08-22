;sa se scrie o fct care intoarce produsul atomilor numerici de la orice nivel
;dintr-o lista
(defun produs(l)
  (cond
    ((null l) 1)
    ((numberp l) l)
    (t (apply '* (mapcar 'produs l)))
  )
)
