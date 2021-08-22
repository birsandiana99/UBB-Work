;sa se determine permutarile unei liste
;permult coada listei si inserez primul elem pe toate poz in fiecare din 
;permutarile obtinute
;insereaza un elem pe o poz
(defun ins(e n l)
  (cond 
    ((= n 1) (cons e l))
    (t (cons (car l) (ins e (- n 1) (cdr l))))
  )
)
;insereaza un elem pe poz 1,2,...,n
(defun insert (e n l)
  (cond
     ((= n 0) nil) ;insereare pe primele 0 pozitii, nimic
     (t (cons (ins e n l) (insert e (- n 1) l))) 
     ;inserez pe poz n, si pe primele n-1 pozitii
  )
)
;inser un elem pe toate poz posibile dintr-o lista
;concat rezultatele
(defun ins_all(e l)
  (insert e (+ 1 (length l)) l)
)
;insereaza elem e pe toate poz in elem (listele) din l
(defun add(e l)
   (cond
     ((null l) nil) ;nu fac nimic daca lista e vida
     (t (append (ins_all e (car l)) (add e (cdr l))))
    ;inserez pe toate poz in primul element
    ;recursiv, la fel, pt restul listei
    ;concatenez rezultatele
   )
)
(defun permutari(l)
  (cond 
     ;daca lista are un singur elem
    ((null (cdr l)) (list (list (car l))))
    ;altfel adaug primul elem in toate permut restului listei 
    (t (add (car l) (permutari (cdr l))))
  )
)
