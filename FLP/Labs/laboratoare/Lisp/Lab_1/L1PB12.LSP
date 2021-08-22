;sa se determine cmmdc al numerelor dintr-o lista liniara
(defun cmmdc(a b)
  (cond
    ((= a 0) b)
    ((= b 0) a)
    (t (cmmdc b (mod a b)))
  )
)
(defun cmmdc_sir(l)
  (cond
    ((null l) 0)
    ((numberp l) l)
    ((not (numberp (car l))) (cmmdc_sir (cdr l)))
    (t (cmmdc (car l) (cmmdc_sir (cdr l))))
  )
)
