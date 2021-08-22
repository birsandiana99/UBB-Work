%7. Sort a list with keeping double values.
inserare(E,[],[E]):-!.
inserare(E,[H|T],[H|L]):-E>=H,!,inserare(E,T,L).
inserare(E,[H|T],[E|[H|T]]):-!.

sortare([],[]):-!.
sortare([H|T],L):-
	sortare(T,L1),
	inserare(H,L1,L).

%8.sort a list by eliminationg the doubles

sterge(_,[],[]).
sterge(E,[E|T],T1):-sterge(E,T,T1),!.
sterge(E,[H|T],[H|T1]):-sterge(E,T,T1).

sortare2([],[]):-!.
sortare2([H|T],L):-sterge(H,T,L1),
	sortare2(L1,L2),
	inserare(H,L2,L).
