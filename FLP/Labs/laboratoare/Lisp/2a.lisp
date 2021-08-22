;  a. Write a function to return the set of all pairs from a list given as parameter. 
;    Example: (a b c d) --> ((a b) (a c) (a d) (b c) (b d) (c d))

(defun pereche (e l)            ;(e l1) (e l2)....
	(cond
		((null l) nil)
		(t (cons (list e (car l)) (pereche e (cdr l))))
	)
)

(defun perechi (l)               ;main function
	(cond 
		((null l) nil)
		(t (append (pereche (car l) (cdr l)) (perechi (cdr l))))
	)
)