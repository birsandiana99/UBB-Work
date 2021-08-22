;verifica daca o lista e sau nu liniara
(defun liniara(l)
   (cond
     ((null l) t)
     (t (and (atom (car l)) (liniara (cdr l))))
    )
)
;sa se substituie prima aparitie a unui element intr-o lista data
;(defun substituie(e1 e2 l)
;pe e1 il inloc cu e2 in lista l
;sa se sorteze cu eliminarea dublurilor
(defun elim(l)
   (cond 
      ((null l) l)
      (t (cons (car l) (elim (delete (car l) (cdr l)))))
   )
)

(defun ins(e l)
  (cond 
     ((null l) (cons e nil))
     ((< e (car l)) (cons e l))
     (t (cons (car l) (ins e (cdr l)))) 
  )
)
(defun sortare(l)
     (cond
         ((null l) nil)
         (t (ins (car l) (sortare (cdr l))))
      )
)
(defun ordon(l)
   (sortare (elim l))  
)
;interclarea a doua liste liniare sortate
(defun interc(l1 l2)
 (cond  
  ((null l1) l2)
   ((null l2) l1)
   ((< (car l1) (car l2)) (cons (car l1) (interc (cdr l1) l2)))
   (t (cons (car l2) (interc l1 (cdr l2))))
   )
)
(defun interclasare(l1 l2)
   (elim (interc l1 l2))
)
