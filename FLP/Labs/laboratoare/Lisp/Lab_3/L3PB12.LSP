;lista tuturor atomilor ce apar pe orice nivel
(defun lis_atomi(l)
  (cond
    ((atom l) (list l))
    (t (mapcan 'lis_atomi l))
  )
)
