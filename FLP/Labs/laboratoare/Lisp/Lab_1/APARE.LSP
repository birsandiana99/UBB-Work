;o functie care pt o lista de atomi formeaza o lista cu elemente perechi de for;ma (atom n), unde n este nr de aparitii al atomului atom in lista initiala
(defun nr_aparitii(a l) ;determina numarul de aparitii al lui a in l
   (cond
       ((null l) 0)
       ((= (car l) a) (+ 1 (nr_aparitii a (cdr l))))
       (t (nr_aparitii a (cdr l))) 
   )
)
(defun apare(l)
  (cond 
     ((null l) nil)
     (t (cons (cons (car l) (cons (nr_aparitii (car l) l) nil)) (apare (cdr l))     ))
  )
)
