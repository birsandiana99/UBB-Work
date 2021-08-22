;sa se construiasac o fct care intoarce nr atomilor dintr-o lista de la orice n;ivel
(defun nr_atomi(l)
  (cond 
    ((null l) 0)
    ((atom l) 1)
    (t (apply '+ (mapcar 'nr_atomi l)))
  )
)
