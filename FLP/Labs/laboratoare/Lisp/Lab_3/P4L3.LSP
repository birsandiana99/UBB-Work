;sa se scrie o fct care intoarce maximul atomilor numerici dintr-o lista
;de la orice nivel
(defun maxim(l)
  (cond
     ((null l) -30000)
     ((numberp l) l)
     (t (apply 'max (mapcan 'maxim l)))
  )
)
