;suma atomilor numerici dintr-o lista de la orice nivel
(defun sum(l)
  (cond
    ((null l) 0)
    ((numberp l) l)
    ((atom l) 0)
    (t (apply '+ (mapcar 'sum l)))
  )
)
