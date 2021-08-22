 ;a. Sa se construiasca o functie care intoarce suma atomilor numerici
 ;dintr-o lista, de la orice nivel.
 
(defun suma(l)
	(cond
		((null l) 0)
		((numberp (car l)) (+ (car l) (suma (cdr l))))
		((symbolp (car l)) (suma (cdr l)))
		(t (+ (suma (car l)) (suma (cdr l))))
	)
)

 ;b. Sa se scrie o functie care intoarce multimea tuturor sublistelor unei
 ;liste date. Ex: Ptr. lista ((1 2 3) ((4 5) 6)) => ((1 2 3) (4 5) ((4 5) 6))
 
 (defun subliste(l)
	(cond 
		((null l) nil)
		((listp (car l)) (append (list (car l)) (subliste (car l)) (subliste (cdr l))))
		(t (subliste (cdr l)))
	)
)
 
 ;c. Sa se scrie o functie care testeaza egalitatea a doua multimi, fara
 ;sa se faca apel la diferenta a doua multimi.
 
 (defun notFound(e l)
	(cond
		((null l) t)
		((= (car l) e) nil)
		(t (notFound e (cdr l)))
	)
)

 (defun multimiAux(l1 l2 l3)
	(cond
		((not (equal (length l1) (length l2))) nil)
		((null l3) t)
		((notFound (car l3) l2) nil)
		(t (multimiAux l1 l2 (cdr l3)))
	)
)

 (defun multimiEgale(l1 l2)
	(multimiAux l1 l2 l1)
)

 ;d. Sa se intercaleze un element pe pozitia a n-a a unei liste liniare. 
 
 (defun inserare(l e n)
	(cond
		((null l) nil)
		((<= n 0) l)
		((> n 1) (cons (car l) (inserare (cdr l) e (- n 1))))
		((= n 1) (cons e l))
	)
)