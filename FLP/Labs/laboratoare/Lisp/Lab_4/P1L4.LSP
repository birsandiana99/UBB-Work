;sa se scrie o fct care selecteaza al n-lea elem al unei liste sau nil daca 
;nu exista
(defun select(l n)
  (prog((poz 1)) ;pozitia la care sunt in lista 
    eti    
     (cond
        ((null l) nil)
        ((= poz n) (return (car l)))
        (t (setq poz (+ 1 poz)) (setq l (cdr l)) (go eti)) 
     )
  )
)
;nr pare-impare
(defun par_impar(l)
  (prog ((nrp 0) (nri 0) (lp nil) (li nil))
     eti 
      (cond
          ((null l) (return (list nrp lp nri li)))
          ((= 0 (mod (car l) 2)) (setq nrp (+ 1 nrp)) (setq lp (cons  (car l)   lp)) (setq l (cdr l)) (go eti))
          (t (setq nri (+ 1 nri)) (setq li (cons (car l) li)) (setq l (cdr l))(go eti))
      )
  )
)
