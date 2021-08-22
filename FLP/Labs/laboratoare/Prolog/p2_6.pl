%6. Define the predicates "isequal" and "lessthan" for numbers written
% in list representation.
lungime([],0).
lungime([_|T],N):- lungime(T,N1),N is N1+1.


compara([],[],0).
compara(L1,L2,R):- lungime(L1,X),lungime(L2,Y),X<Y,!,R is -1.
compara(L1,L2,R):- lungime(L1,X),lungime(L2,Y),X>Y,!,R is 1.
compara([H1|_],[H2|_],R):- H1<H2,!,R is -1.
compara([H1|_],[H2|_],R):- H1>H2,!,R is 1.
compara([H1|T1],[H2|T2],R):- H1=:=H2,compare(T1,T2,R).

tip(L1,L2):- compara(L1,L2,1),write("Primul sir e mai mare"),nl.
tip(L1,L2):-compara(L1,L2,0),write("Egale"),nl.
tip(L1,L2):-compara(L1,L2,-1),write("Al doilea e mai mare"),nl.
