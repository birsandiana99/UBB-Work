
;sa se scrie o fct care primind o lista intoarce multimea tuturor perechilor
;din lista
;returneaza lista perechilor formate cu e si toate elem din lista
(defun per_el(e l)
   (cond
    ((null l) nil)
    (t (cons (list e (car l)) (per_el e (cdr l))))
   )
)
(defun perechi(l)
   (cond
     ((equal nil (cdr l)) nil) ;mai am un sigur elem in lista, deci nu mai am
      ;perechi de format
     ;altfel trebuie sa formez perechi dintre primul elem si toate celelalte
      (t (append (per_el (car l) (cdr l)) (perechi (cdr l))))
   )
)
;sa se scrie o fct care determina produsul atomilor numerici de la nivelul
;superficial dintr-o lista
(defun prod(l)
  (cond 
    ((null l) 1) 
    ((numberp (car l)) (* (car l) (prod (cdr l))))
    (t (prod (cdr l)))
  )
)
;se da o lista de atomi. Sa se obtina o lista de perechi, de tip (atom, nr)
;unde nr e nr de aparitii al atomului respectiv in lista
(defun nr(e l) ;nr de aparitii al elem e in lista l
  (cond 
    ((null l) 0)
    ((equal e (car l)) (+ 1 (nr e (cdr l))))
    (t (nr e (cdr l))) 
 )
)
(defun add_last(e l)
   (cond 
     ((null l) (cons e nil))
     (t (cons (car l) (add_last e (cdr l))))
   )
)
(defun lis_apar(l)
  (cond
     ((null l) l)
     (t (cons (list (car l) (nr (car l) l)) (lis_apar (delete (car l) l))))  
  )
)

