;nr de noduri dintr-un arbore n-ar.
(defun nr(a)
  (cond
    ((null (cdr a)) 1)
    (t (+ 1 (apply '+ (mapcar 'nr (cdr a)))))
  )
)
