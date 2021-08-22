;sa se scrie o fct care intoarce suma atomilor numerici de la orice nivel dintr;-o lista.
(defun suma(l)
  (cond 
     ((null l) 0)
     ((numberp l) l)
     (t (apply '+ (mapcar 'suma l)))
  )
)
