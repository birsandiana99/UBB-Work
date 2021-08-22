(defun reverseAux (l)
  (cond
    ((listp l) (reverseAll l))
    (t l)
  )
)
(defun reverseAll (l)
  (mapcar 'reverseAux (reverse l))
)

(mapcar 'print '((1 2 (x y z)) (4 5 6)))