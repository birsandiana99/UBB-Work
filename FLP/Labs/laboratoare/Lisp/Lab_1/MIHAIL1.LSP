;sa se detrmine multimea atomilor dintr-o lista, de la orice nivel
(defun atomi(l)
  (cond 
     ((null l) l)
     ((atom (car l)) (cons (car l) (atomi (cdr l))))
     (t (append (atomi(car l)) (atomi (cdr l))))
  )
)
(defun elimdubluri(l)
  (cond
    ((null l) l)
    (t (cons (car l) (elimdubluri (delete (car l) l)))) 
  )
)

(defun getatomi(l)
  (elimdubluri (atomi l))
)
;sa se scrie o fct care testeaza daca o lista liniara este multime
(defun multime(l)
   (cond
      ((null l) t) ;lista vida e multime
      ((member (car l) (cdr l)) nil)
      (t (multime(cdr l)))
   )
)
;sa se elimine elementul de pe pozitia a n-a dintr-o lista
(defun elim(n l)
  (cond 
     ((> n (length l)) 'nu_e_in_lista)
     ((equal n 1) (cdr l))
     (t (cons (car l) (elim (- n 1) (cdr l))))
  )
)
