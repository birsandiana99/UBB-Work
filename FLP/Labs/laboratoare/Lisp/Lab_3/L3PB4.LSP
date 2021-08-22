;maximul atomilor numerici dintr-o lista de la orice nivel
(defun maxim(l)
  (cond
     ((null l) -666)
     ((numberp l) l)
     ((atom l) -666)
     (t (apply 'max (mapcar 'maxim l)))
  )
)
