;d. Write a function to produce the list of pairs (atom n), where atom appears for
 ;    n times in the parameter list. Example:
  ;   (A B A B A C A) --> ((A 4) (B 2) (C 1)).

(defun apare (e l)                ; daca e apartine listei l
	(cond
		((null l) nil)
		((equal e (car l)) t)
		(t (apare e (cdr l)))
	)
)

(defun nraparitii (e l)
	(cond 
		((null l) 0)
		((equal e (car l)) (+ 1 (nraparitii e (cdr l))))
		(t (nraparitii e (cdr l)))
	)
)

(defun famultime (l)
	(cond
		((null l) nil)
		((not (apare (car l) (cdr l))) (cons (car l) (famultime (cdr l))))
		(t (famultime (cdr l)))
	)
)

(defun aux (l m)
	(cond 
		((null m) nil)
		(t (cons (cons (car m) (nraparitii (car m) l)) (aux l (cdr m))))
	)
)

(defun numaratoare (l)
	(cond 
		((null l) nil)
		(t (aux l (famultime l)))
	)
)