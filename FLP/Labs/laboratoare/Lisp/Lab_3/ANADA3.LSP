;sa se construiasca o functie care intoarce adancimea unei liste
;cu fct MAP
(defun adancime(l)
  (cond
    ((atom l) 0) 
    (t (+ 1 (apply 'max (mapcar 'adancime l))))
  )
)
