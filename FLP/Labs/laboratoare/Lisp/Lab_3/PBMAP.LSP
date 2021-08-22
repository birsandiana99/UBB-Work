;lungimea unei liste, la orice nivel
(defun lung(l)
  (cond
    ((atom l) 1)
    (t (apply '+ (mapcar 'lung l)))
  )
)
;sa se modifice atomii numerici dintr-o lista prin dublarea valorii,la orice ni;vel
(defun modif(l)
   (cond 
      ((numberp l) (* 2 l))
      ((atom l) l)
      (t (mapcar 'modif l))
   )
)
;sa se determine maximul atomilor numerici de la orice nivel dintr-o lista
;neliniara
(defun maxim(l)
   (cond
     ((numberp l) l)
     ((atom l) -10000)
     (t (apply 'max (mapcar 'maxim l)))
   )
)
(defun invers(l)
  (cond
     ((atom l) l)
     (t (set 'll (mapcar 'invers l)) (reverse ll)) 
  )
)
(defun inv(l)
   (cond
     ((atom l) l)
     (t (apply 'reverse (mapcar 'invers l)))
   )
)
