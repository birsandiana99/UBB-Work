isList([_|_]):-!.
isList([]):-!.


parcurgere([],[],_,_):-!.
parcurgere([H|T],R,N,P):-isList(H),append(H,[P,P],R1),P1 is P + N,
	parcurgere(T,R3,N,P1),R = [R1|R3].
parcurgere([H|T],R,N,P):- \+ isList(H),parcurgere(T,R1,N,P),R = [H|R1].


final(L,N,R):-parcurgere(L,R,N,0).


