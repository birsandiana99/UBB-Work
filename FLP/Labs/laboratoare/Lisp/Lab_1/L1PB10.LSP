;Sa se determine adancimea unei liste
(defun adancime(l)
 (cond
   ((null l) 0)
   ((atom (car l)) (adancime (cdr l)))
   (t (max (+ 1 (adancime (car l))) (adancime (cdr l))))
 )
)
(defun adanc(l)
  (+ 1 (adancime l))  
)
;sa se inlocuiasaca fiecare sublista a unei liste cu ultimul ei element
(defun ultim(l) ;intoarce ultimul elem al unei liste
  (cond
     ((atom (car (reverse l))) (car (reverse l)))
     (t (ultim (car (reverse l))))
  )
)
(defun inlocuire(l)
  (cond 
    ((null l) nil)
    ((atom (car l)) (cons (car l) (inlocuire (cdr l))))
    (t (cons (ultim (car l)) (inlocuire (cdr l))))
  )
)
