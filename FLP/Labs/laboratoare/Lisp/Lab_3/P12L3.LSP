;definiti o fct care intoarce lista tuturor atomilor care apar intr-o lista
;pe orice nivel. 
(defun atomi(l)
 (cond
   ;((null l) nil)
   ((atom l) l)
   (t (mapcan 'atomi l))
 )
)
