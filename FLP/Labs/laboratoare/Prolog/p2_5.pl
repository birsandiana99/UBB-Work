% 5. Determine the value of a polynomial in a point. The polynomial is
% given as the list of its coefficients.
polin([H],X,S1,S2):- S2 is S1*X+H,!.
polin([H|T],X,S1,S2):- S3 is S1*X+H,polin(T,X,S3,S2).
polinom(L,X,S):-polin(L,X,0,S).
