;inverseaza o lista impreuna cu toate sublistele sale de pe orice nivel
(defun invers(l)
       (print l)
  (cond
    ((null l) nil)
    ((atom l) l)
    (t (reverse (mapcar 'invers l)))
  )
)
