;sterge aparitiile unui atom de pe toate nivelele unei liste
(defun sterge(e l)
  (cond
    ((and (atom l) (equal e l)) nil)
    ((atom l) (list l))
    (t (list (mapcan '(lambda (l) (sterge e l)) l)))
  )
)
(defun sterg(e l)
  (car (sterge e l))
)
