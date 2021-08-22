;fct care returneaza produsul atomilor numerici de la orice nivel dintr-o lista
(defun prod_num (l)
  (cond 
   ((null l) 1);daca lista e vida peodusul este 1
   ((and (atom (car l)) (numberp (car l))) (* (car l) (prod_num (cdr l))))
   ;daca e atom si e numeric at prod dintre el si prod din restul listei 
   ((atom (car l)) (prod_num (cdr l))) 
   ;daca primul e atom si nu e numeric atunci produsul din restul listei
   (t (* (prod_num (car l)) (prod_num(cdr l)))) 
   ;daca primul este lista,nu atom atunci produsul este produsul din primul ele   ;ment si prosusul din restul listei
  )
)
;fct care ordoneaza o lista liniara, cu pastrarea dublurilor
(defun inserare (a l)
  (cond
    ;daca l e lista vida, constr l cu elem a
    ((null l) (cons a nil))
    ;daca e mai mic decat primul elem il pun pe prima pozitie
    ((< a (car l)) (cons a l))
    ;altfel inserez in restul listei
    (t (cons (car l) (inserare a (cdr l))))
  )
)

(defun ordon (l)
  (cond 
    ((null l) l) ;daca lista e vida, atunci e ordonata, o returnez
    (t (inserare (car l) (ordon (cdr l))))
    ;altfel inserez primul elem in lista ordon formata din celel elem
  )
)
;fct care intoarce reuniunea a doua multimi
;cele doua multimi le voi da ca doua liste liniare
;va trebui sa fac o fct care determina daca un elem este sau nu intr-o lista
;pt a nu introduce de doua ori un element in reuniune
(defun cauta (a l)
 (cond
    ((null l) nil) ;daca lista e vida, elem nu e in lista ==> false=nil
    (t (or (equal (car l) a) (cauta a (cdr l)))) 
 )
)
;reuniunea 
;caut primul elem din a doua multime in prima, daca il gasesc reunesc prima 
;cu partea a doua din mult a doua, daca nu-l gasesc pun elem in multime si apoi;reunesc cu restul mult 2
(defun reuniune(m1 m2)
  (cond
     ((null m2) m1) ;daca a doua mult e vida, at reuniunea e prima multime
     ((cauta (car m2) m1) (reuniune m1 (cdr m2)))
     (t (cons (car m2) (reuniune m1 (cdr m2))))
  )
)
;functie care inverseaza o lista
;inversez partea a doua a listei si pun primul element la sfarsitul ei
(defun ins_last(a l)
  (cond
    ((null l) (cons a nil))
    (t (cons (car l) (ins_last a (cdr l))))
  )
)
(defun inversare(l)
   (cond
        ((null l) nil)
        ((atom (car l)) (ins_last (car l) (inversare (cdr l))))
        (t  (ins_last (inversare (car l)) (inversare (cdr l))))     
   )
)



