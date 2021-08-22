;sa se verifice daca o lista este liniara
(defun liniara (l)
  (cond
    ((null l) t)
    ((listp (car l)) nil)
    (t (liniara (cdr l)))
  )
)
;interclaseaza fara pastrarea dublurilor doua liste liniare ordonate
;e -ultimul element adaugat in lista interclasata
(defun interclaseaza (e l1 l2)
  (cond
    ((null l1) (interclaseaza e '(666) l2))  ;daca una dintre liste este vida, va ;rezulta cealalta
    ((null l2) (interclaseaza e l1 '(666)))
                                                                    ;altfel, nici una nu este vida, se compara primul element
    ((and (< (car l1) (car l2)) (not (equal (car l1) e))) 
           (cons (car l1) (interclaseaza (car l1) (cdr l1) l2)))
    (( < (car l1) (car l2)) (interclaseaza e (cdr l1) l2))
                                                                     ;am ajuns aici, inseamna ca primul elem din a doua lista e mai mic
                                                                     ;vad daca nu e dublura
    ((not (equal (car l2) e)) (cons (car l2) (interclaseaza (car l2) l1 (cdr l2))))
    (t (interclaseaza e l1 (cdr l2))) 
  )
)
(defun inter(l1 l2)
  (interclaseaza -666 l1 l2)
)
