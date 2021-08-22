;Sa se construiasca multimea atomilor unei liste
;elimina un elem de pe toate poz dintr-o lista (orice nivel)
(defun elimin (e l)
  (cond
    ((null l) nil)
    ((and (atom (car l)) (equal (car l) e)) (elimin e (cdr l)))
    ((atom (car l)) (cons (car l) (elimin e (cdr l))))
    (t (append (elimin e (car l)) (elimin e (cdr l))))
  )
)
(defun get_multime(l)
  (cond 
    ((null l) nil)
    ((atom (car l)) (append (list (car l)) (get_multime (elimin (car l) l))))
    (t (append (get_multime (car l)) (get_multime (cdr l))))
  )
)
;fct care intoarce T, daca lista are nr par de elem pe primul nivel si nil
;in caz contrar fara sa se numere elem listei
(defun is_par(l)
  (cond
    ((null l) t)
    ((and (car l) (not (car (cdr l)))) nil)
    ((and (car l) (car (cdr l))) (is_par (cdr (cdr l))))
  )
)
