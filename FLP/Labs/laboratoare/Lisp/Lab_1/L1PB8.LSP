;Sa se verifice daca un elem e membru al unei liste, nu neaparat liniara
(defun member(e l)
 (cond 
  ((null l) nil)
  ((atom (car l)) (or (equal e (car l)) (member e (cdr l))))
  (t (or (equal (car l) e) (member e (car l)) (member e (cdr l))))
 )
)
