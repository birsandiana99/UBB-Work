;fct care determina succesorul unui numar reprezentat prin sirul cifrelor
;intr-o lista
;ex (1 2 3 9 9 9) ==> (1 2 4 0 0 0)
;voi inversa sirul, adun 1 si apoi inversez la loc
;inversarea o voi face cu fct reverse
(defun urm(l)
   (cond
                             ; ((equal 9 (car l)) (cons 1 l))
     ((and (equal 9 (car l)) (not (equal nil (cdr l)))) (cons 0 (urm (cdr l)))) (equal 9 (car l)) (cons 0 (cons 1 nil)))
     (t (cons (+ 1 (car l)) (cdr l)))
                             ;(t (cons 0 (urm (cdr l)))) 
   )
)
(defun urmator(l)
   (setf l (reverse l))
   (setf l (urm l))
   (reverse l) 
)


