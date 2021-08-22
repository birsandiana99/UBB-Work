(defun parcurgS(l nv nm)
	(cond
		((null l) nil)
		((= nv (+ 1 nm)) nil)
		(t (cons (car l) (cons (cadr l) (parcurgS (cddr l) (+ 1 nv) (+ nm (cadr l))))))
	)
)

(defun parcurgD(l nv nm)
	(cond
		((null l) nil)
		((= nv (+ 1 nm)) l)
		(t (parcurgD (cddr l) (+ 1 nv) (+ nm (cadr l))))
	)
)

(defun stanga(l)
	(parcurgS (cddr l) 0 0)
)

(defun dreapta(l)
	(parcurgD (cddr l) 0 0)
)

(defun postordine(l)
	(cond
		((null l) nil)
		(t ( append (postordine (stanga l)) (postordine (dreapta l)) (list (car l))))
	)
)