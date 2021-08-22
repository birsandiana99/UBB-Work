%Remove all occurences of a certain atom from a list.
sterge(_,[],[]).
sterge(E,[E|T],T1):-sterge(E,T,T1),!.
sterge(E,[H|T],[H|T1]):-sterge(E,T,T1).
%Out of a list of atoms produce a list of pairs (atom n), where the
%atom appears in the original lista for n times. E.g.:
%number([A B A B A C A], X) produces X = [[A 4] [B 2] [C 1]].
numarare(_,[],0).
numarare(E,[E|T],X):-numarare(E,T,X1),!,X is X1+1.
numarare(E,[_|T],X):-numarare(E,T,X).

pereche(A,B,functor(A,B)).
numar([],[]).
numar([H|T],[[H,N]|P]):-numarare(H,[H|T],N),
	sterge(H,[H|T],L),
	numar(L,P).
