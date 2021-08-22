;L1
;1 a) get all atoms from any level in the same order
(defun atoms (l)
  (cond
    ((null l) nil)
    ((atom l) (list l))
    ((atom (car l)) (cons (car l) (atoms (cdr l))))
    (t (append (atoms (car l)) (atoms (cdr l))))
   )
)
(atoms '(((A B) C) (D E)))

;1 b) return max value of numerical atoms in list, at superficial level
(defun getmax (l)
  (cond
    ((null l) 0)
    ((numberp l) l)
    ((atom l) 0)
    ((numberp (car l)) (max (car l) (getmax (cdr l))))
    (t (getmax (cdr l)))
   )
)
(getmax '(1 2 3 A B 17 D F X))



(defun st(l nr nrnod)
;incep cu al 3-lea element si iau elem pana cand suma nr subarb este
;nr nodurilor -1
   (cond
      ((equal (cdr l) nil) nil)
      ((= (+ (cadr l) nr) (+ 1 nrnod)) (list (car l) (cadr l)))
      (t (cons (car l) (cons (cadr l) (st (cdr (cdr l)) (+ nr (cadr l)) (+ 1 nrnod)))))  
   )
)
(defun elim(l1 l)
;elimina sublista l1 din lista l, stiu ca l incepe cu l1
  (cond
    ((null l1) l) 
    (t (elim (cdr l1) (cdr l)))  
  )
)

(defun dr(l)
;subarborele drept cu prec ca stiu subarb stang
;elimin din l arb stang
  (elim (st l 0 0) l)
)
(defun trans (l)
  (cond
    ((equal nil (cdr (cdr l))) (list (car l)))  
    (t (cons (car l) (list (trans (cdr (cdr (st l 0 0)))) (trans (dr  l))))) 
  )
)

(st '(A 2 B 0 C 2 D 0 E 0) 0 0)

