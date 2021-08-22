;fct care intoarce numarul atomilor dintr-o lista de la orice nivel
;se vor folosi fct MAP
(defun nr_elem(e)
 (cond 
   ((null l) 0)
   ((atom e) 1)
   (t (+ 1 (nr_elem(cdr l))))
 )
)
(defun numar(l)
  (mapcar 'nr_elem l)
)
