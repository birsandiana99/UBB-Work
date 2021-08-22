;L1 - 5
;-------------------------------------------------------------------------------------------
;a) Write a function that returns an association list of two lists given as parameters.

( defun associate(l1 l2)
  ( cond 
    ( (null l1) nil )
    ( (null l2) nil )
    (t ( append ( list ( cons ( car l1 ) ( car l2 ))) ( associate ( cdr l1 ) ( cdr l2 ))))
  )
)

(associate '(a b c d) '(1 2 3 4))


;--------------------------------------------------------------------------------------------
;b) Write a function to determine the number of all sublists of a given list, on any level.

( defun sublistnr (l)
  ( cond 
    ( (null l) 0 )
    ( (listp (car l)) (+ 1 ( sublistnr ( car l )) ( sublistnr ( cdr l ))) )
    (t ( sublistnr ( cdr l )))
  )
)

( defun sublist (l)
  (+ 1 (sublistnr l))
)

( sublist  '(1 2 (3 4 5) ))

 

;--------------------------------------------------------------------------------------------
;c) Write the n-th element of a linear list twice.

( defun doublen(l n)
  ( cond
    ( (null l) nil )
    ( (= n 1) ( append  ( list ( car l ) ( car l ))  ( cdr l )))
    (t ( cons ( car l ) ( doublen ( cdr l ) (- n 1))))
  )
)

(doublen '(1 2 3 4 5) '2)


;-------------------------------------------------------------------------------------------
;d) Write a function to return the number of atoms in a list, at superficial level.

( defun countatoms(l)
  ( cond
    ( (null l) 0 )
    (t ( +  ( cond
              ( ( atom ( car l ) ) 1 )
              ( t 0 )
            )
            ( countatoms ( cdr l ))))
  )
)

(countatoms '(a b ((a) c) e (b) ) )

