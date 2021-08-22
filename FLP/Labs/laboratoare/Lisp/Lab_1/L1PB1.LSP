;Sa se obtina lista atomilor unei liste la orice nivel, in aceasi ordine
(defun get_list(l)
  (cond
    ((atom l) (list l))
    (t (mapcan 'get_list l))
  )
)
(defun get_list1(l)
  (cond 
     ((null l) nil)
     ((atom l) (list l))
     ((atom (car l)) (cons (car l) (get_list1 (cdr l))))
     (t (append (get_list1 (car l)) (get_list1 (cdr l))))
  )
)
;intoarce maximul atomilor numerici de la nivel superficial
(defun get_max(l)
  (cond 
    ((null l) -666)
    ((numberp l) l)
    ((atom l) -666)
    ((numberp (car l)) (max (car l) (get_max (cdr l))))
    (t (get_max (cdr l)))
  )
)
;suma a 2 vectori
(defun suma(l1 l2)
   (cond
     ((null l1) nil)
     (t (cons (+ (car l1) (car l2)) (suma (cdr l1) (cdr l2))))
   )
)
;inverseaza secventele continue de atomi dintr-o lista
