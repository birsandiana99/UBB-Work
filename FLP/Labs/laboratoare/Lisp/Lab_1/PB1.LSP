;functie care obtine dintr-o lista lista tuturor atomilor de pe orice nivel in ;ordinea in care apar
(defun add_last(a l)
  (cond 
     ((null l) (cons a nil))
     (t (cons (car l) (add_last a (cdr l))))
  )
)
(defun lis_atomi(l)
  (cond 
     ((null l) l)                              ;daca e vida, se returneaza lista vida
     ((atom (car l)) (cons (car l) (lis_atomi (cdr l))))
                                                  ;daca primul elem e atom il concatenez cu lista rez din a 2 parte
     (t (append (lis_atomi (car l)) (lis_atomi (cdr l))))
                                                   ;daca primul elem este lista, atunci formez cele 2 liste si le concatenez
  )
)
;plecand de la o lista data inverseaza valorile continue de atomi
