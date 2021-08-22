(defun depth (tree)
           (cond 
				((atom tree) 0)
                ((1+ (apply #'max (mapcar #'depth tree))))
			)
)

(defun tree_depth(tree)
	(cond
		((null (car tree)) 0)
		((atom (car tree)) (let ((restDepth(tree_depth(cdr tree))))
							(if(> restDepth 0) restDepth 0)
							)
		)
		('t (let ( (leftDepth(+ 1 (tree_depth(car tree)))) (rightDepth (tree_depth(cdr tree))) )
		(if (> rightDepth leftDepth) rightDepth leftDepth)
		)
		)
		)
)
(defun balanced(tree)
	(
	 cond
		((null tree) t)
		('t (let((lh (tree_depth( cadr tree))) (rh (tree_depth( caddr tree))))
		(if ( < 1 (abs(- lh rh))) nil t)
		))
	)
)