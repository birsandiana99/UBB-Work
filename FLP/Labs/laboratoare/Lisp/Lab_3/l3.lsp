;verifica daca un atom e membru al unei liste nu neaparat liniara
(defun membru(e l)
  (cond
    ((null l) 0)
    ((and (atom l) (equal e l)) 1)
    ((atom l) 0)
    ((apply '+ (mapcar '(lambda (ll) (membru e ll)) l)))
  )
)
(defun member (e l)
  (cond
    ((equal 0 (membru e l)) nil)
    (t t)
  )
)
(defun subl(l)
 (cond
    ((atom l) nil)
    (t (cons l (mapcar 'subl l)))
  ) 
)