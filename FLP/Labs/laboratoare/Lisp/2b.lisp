;b. Write a function to compute the result of an arithmetic expression memorised 
 ;    in preorder on a stack. Examples:
  ;   (+ 1 3) ==> 4  (1 + 3)
   ;  (+ * 2 4 3) ==> 11  [((2 * 4) + 3)
    ; (+ * 2 4 - 5 * 2 2) ==> 9  ((2 * 4) + (5 - (2 * 2))

(defun aplica (op op1 op2)
	(apply op (list op1 op2))
)

;l will actually be the list l reversed
(defun printlist (l) 
     (cond 
	((null (cdr l)) (car l))
	( (and 
		(numberp (car l)) 
		(numberp (cadr l)) 
		(not(numberp (caddr l)))
	  ) (append 
			( append 
				;(list(cdddr l))
				(cons(list (car l) (caddr l) (cadr l)) nil) 
                              	(cdddr l)
                              ) 
                         (printlist (cdddr l))  
                       )     
	)  
	
	(t (cons (car l) (printlist (cdr l))))	
  
     )
)



(defun calculeste (l) 
	(cond 
		((null (cdr l)) (car l))
		((and 
				(not (numberp (car l))) 
				(numberp (cadr l)) 
				(numberp (caddr l))
			) 
		;
		(append
		;
			(append
				(list 
				    (aplica (car l) (cadr l) (caddr l) )
						 
                                 ) 
                                 (cdddr l)
                        ) 
			;
			(cons (list (cadr l) (car l) (caddr l)) nil) 	
			;
		)
		)		
		(t (cons (car l) (calculeste (cdr l))))
	)
)

(defun maincalc (l)
	(cond 
		((numberp (car l)) l)
		(t (maincalc (calculeste l)))
	)
)