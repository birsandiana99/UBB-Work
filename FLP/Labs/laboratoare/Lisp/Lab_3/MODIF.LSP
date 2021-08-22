(defun modif (l)
  (cond
    ((numberp l) (* 2 l))
    ((atom l) l)
    (t (mapcar 'modif l))
  )
)
