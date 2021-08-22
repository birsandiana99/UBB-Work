( defun left-subtree( tree )
  ( cond
    ( ( null tree ) nil )
    ( t ( car ( cdr tree ) ) )
  )
)

( defun right-subtree( tree )
  ( cond
    ( ( null tree ) nil )
    ( t ( car ( cdr ( cdr tree )  ) ) )
  )
)

( defun get-level( tree node counter )
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

( get-level '(A (B) (C (D (X) (Y)) (E))) 'Y '0 )
