;fct care intoarce multimea perechilor dintr-o lista
(defun perechi(e l)
  (cond 
    ((null l) nil)
    ((atom l) (list (list e (car l))))
    (t (append (list (list e (car l))) (perechi e (cdr l))))
  )
)
(defun get_perechi(l)
  (cond 
    ((null l) nil)
    (t (append (perechi (car l) (cdr l)) (get_perechi (cdr l))))
  )
)
;produsul atomilor numerici dintr-o lista de la nivel superficial
(defun produs (l)
  (cond 
    ((null l) 1)
    ((and (atom l) (not (numberp l))) 1)
    ((numberp l) l)
    ((numberp (car l)) (* (car l) (produs (cdr l))))
    (t (produs (cdr l)))
  )
)
;o fct care intoarce o lista de forma perechi de atom, nr aparitii
;numara de cate ori apare un atom intr-o lista
(defun nr(e l)
  (cond 
   ((null l) 0)
   ((equal (car l) e) (+ 1 (nr e (cdr l))))
   (t (nr e (cdr l)))
  )
)
(defun per_nr(l)
  (cond
    ((null l) nil)
    (t (append (list (list (car l) (nr (car l) l))) (per_nr (remove (car l) l))       ))
  )
)
