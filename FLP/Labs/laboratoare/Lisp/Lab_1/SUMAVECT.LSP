;functie care intoarce suma a doi vectori de lungime egala

(defun sum_vect(v1 v2)
  (cond
     ((null v1) nil)
     (t (cons (+ (car v1) (car v2)) (sum_vect (cdr v1) (cdr v2))))
  )
)
