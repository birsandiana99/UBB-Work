isList([H|T]):-!.

concatenare([],L,L).
concatenare([H|L1],L2,[H|L3]):-
	concatenare(L1,L2,L3).
