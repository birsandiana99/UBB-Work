;produsul atomilor numerici dintr-o lista de la orice nivel
(defun prod(l)
  (cond
    ((null l) 1)
    ((numberp l) l)
    ((atom l) 1)
    (t (apply '* (mapcar 'prod l)))
  )
)
