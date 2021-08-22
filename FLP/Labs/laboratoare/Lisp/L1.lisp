;a. Definiti o functie care determina succesorul unui numar reprezentat cifra
; cu cifra intr-o lista. De ex: (1 9 3 5 9 9) --> (1 9 3 6 0 0) 


; Transforma o lista in inversul numarului ce il reprezinta

( defun toNumber(l)
	( cond
		( (null l) 0 )
		(t ( + ( * ( toNumber ( cdr l )) 10) ( car l )))
	)
)


;Inverseaza ordinea elementelor dintr-o lista
( defun invert(l)
	( cond 
		( (null l) nil )
		(t ( append ( invert ( cdr l )) ( list ( car l ))))
	)
)

;Transforma un numar in lista corespunzatoare inversului numarului
( defun toList(x)
	( cond
		( (= x 0) nil)
		(t ( cons ( mod x 10 ) ( toList ( floor ( / x 10 )) )))
	)
)
;Incrementeaza un numar ce e reprezetat ca o lista


( defun increment2(l c ok)
	(cond	
		((null l) nil)
		((= ok 0) (cons (mod (+ (car l) 1) 10) (increment2 (cdr l) (floor (/ (+ (car l) 1) 10)) 1)))
		(t (cons (mod (+ (car l) c) 10) (increment2 (cdr l) (floor (/ (+ (car l) c) 10)) 1)))
	)
)

( defun increment(l)
	( invert (increment2 (invert l) 0 0))
)
;b. Sa se construiasca multimea atomilor unei liste.
; Exemplu: (1 (2 (1 3 (2 4) 3) 1) (1 4)) ==> (1 2 3 4) 

;Dintr-o lista cu mai multe nivele transforma intr-o lista cu un simplu nivel
( defun nivelare(l)
	( cond
		( (null l) nil )
		( (atom (car l )) (append  (list (car l)) (nivelare (cdr l))))
		(t (append (nivelare(car l)) (nivelare(cdr l))))
	)
)

;Verifica daca un numar nu apartine unei liste
( defun notFound(e l)
	(cond
		((null l) t)
		((= (car l) e) nil)
		(t (notFound e (cdr l)))
	)
)
;Elimina duplicatele dintr-o lista
( defun unique(l)
	(cond
		((null l) nil)
		((notFound (car l) (cdr l)) (cons (car l) (unique (cdr l))))
		(t (unique(cdr l)))
	)
)
;Returneaza toti atomii unei liste
( defun atomi(l)
	( unique ( nivelare l))
)

;c. Sa se scrie o functie care testeaza daca o lista liniara este o multime. 
( defun multime(l)
	(cond
		((null l) t)
		((notFound (car l) (cdr l)) (multime (cdr l)))
		(t nil)
	)
)
	
;d. Sa se elimine elementul de pe pozitia a n-a a unei liste liniare. 
(defun elimPoz(l n)
	( cond
		( (null l) nil)
		( (<= n 0) l)
		( (> n 1) (cons (car l) (elimPoz (cdr l) (- n 1))) )
		( (= n 1) (cdr l) )
	)
)
	  
			