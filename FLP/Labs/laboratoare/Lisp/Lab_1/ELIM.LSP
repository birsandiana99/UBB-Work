;eliminarea elem negative dintr-o lista
(defun elim(l)
  (cond
   ((and (numberp l) (minusp l)) nil)
   ((atom l) (list l))
   (t (list (mapcan 'elim l)))
  )
)
