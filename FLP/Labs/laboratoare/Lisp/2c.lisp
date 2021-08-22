;c. Write a function to return the product of all the numerical atoms from a list,
 ;    at superficial level.


(defun produs (l) 
	(cond
		((null l) 1)
		((numberp (car l)) (* (car l) (produs (cdr l))))
		(t (produs (cdr l)))
	)
)