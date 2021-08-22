;se da o lista liniara Sa se genereze lista permutarilor sale.
;inserarea unui elem pe o poz in lista
(defun ins(e n l)
  (cond
    ((= n 1) (cons e l)) ;pe prima pozitie
    (t (cons (car l) (ins e (- n 1) (cdr l))))
   ;altfel pastrez primul elem si inserez pe e pe poz n-1 in cdr-ul listei l
  )
)
;inserarea unui elem pe toate pozitiile intr-o lista pana pe poz n 
(defun inser(e n l)
  (cond
     ((= n 0) nil) ;pe poz 0
     (t (cons (ins e n l) (inser e (- n 1) l)))
    ;altfel inserez pe poz n si fac acelasi lucru pana la poz n-1
  )
)
;inserarea pe toate poz a unui elem
(defun insert(e l)
  (inser e (+ (length l) 1) l) 
  ;inserez pe e in lista l pana pe poz lung listei +1
)
;am o lista de liste si un element, vreau sa inserez elem pe toate
;pozitiile in listele mici
(defun inserare(e l)
    (cond
       ((null l) nil) ;daca lista mare e vida, atunci nu mai am de inserat
       (t (append (insert e (car l)) (inserare e (cdr l))))
     ;altfel inserez pe e pe toate poz din prima lista mica si apoi la fel 
     ;in rest
    )
)
(defun permut(l)
  (cond 
    ((null (cdr l)) (list(list (car l))))
     ;daca lista e vida, atunci nu are permutari
    (t (inserare (car l) (permut (cdr l))))
    ;altfel fac permutarile pt cdr-ul listei si inserez primul elem din lista
    ;pe toate pozitiile in aceste permutari
  )
)
