;a)
(defun asociere(l1 l2)
  (cond
    ((null l1) nil)
    (t (append (list (cons (car l1) (car l2))) (asociere (cdr l1) (cdr l2))))
  )
)
;b
(defun numar(l)
  (cond 
    ((null l) 0)
    ((listp l) (+ (+ 1 (numar(car l))) (numar(cdr l))))
    ((atom (car l)) (numar(cdr l))) 
  )
)
(defun subliste(l)
  (+ 1 (numar l)) 
)
;c

(defun pozitie(l k c)
   (cond
      ((null l) nil) ; pt lista=vida
	  ((not (equal k c)) (pozitie (car l) k + 1 c))
   )
)

(defun insert(e l k c)
   (cond
      ((null l) nil) ; pt lista vida
	  ((equal k c) (append(e insert(e (car l) k + 1 c))
	  ((not (equal k c)) (append ((car l) insert(e (cdr l) k + 1 c))))
   )
)

(defun scrie(e l k c)
   (cond
      ((null l) nil) ; pt lista vida
	  ((equal p 0) nil) ; pt k=0 e nil
	  ((not (equal p 0)) (insert ( pozitie(car l) p 1) l p 1))
   )
)
;d

(defun nratomi(l)
   (cond
     ((null l) 0)
	 ((atom (car l)) (+ 1(nratomi(cdr l))))
	 (T (nratomi(cdr l)))   ; altfel
   )
)