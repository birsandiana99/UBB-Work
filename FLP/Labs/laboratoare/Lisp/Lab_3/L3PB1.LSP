;sa se det nr de elm dintr-o lista, la orice nivel
(defun nr(l)
  (cond
    ((null l) 0)
    ((atom l) 1)
    (t (apply '+ (mapcar 'nr l))) 
  )
)
