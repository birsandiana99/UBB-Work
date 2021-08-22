( defun left-subtree( tree )
  ( cond
    ( ( null tree ) nil )
    (t (cadr tree))
  )
)
( defun right-subtree( tree )
  ( cond
    ( ( null tree ) nil )
    (t (caddr tree))
  )
)

( defun getlevel( tree node counter )
  ( cond
    ( ( null tree ) -1 )
    ( ( eql (car tree) node )  counter )
    ( t  ( setq func ( get-level ( left-subtree tree ) node ( + 1 counter ) ) )
         ( cond 
           ( ( not ( eql func -1 ) ) func )  
           ( t ( get-level ( right-subtree tree ) node ( + 1 counter ) ) ) 
         )
    )
  )
)

(getlevel '(A (B)(C (D) (E))) 'E 0)
