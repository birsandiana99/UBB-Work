; 1. Sa se construiasca o functie care intoarce numarul atomilor dintr-o lista, de la orice nivel.
; folosind functii MAP

(defun nrAtomi(l)
	( cond
		((null l) 0)
		((atom l) 1)
		(t (apply #'+ (mapcar #'nrAtomi l)))
	)
)