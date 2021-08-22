%2.
%a. Compute the union of two sets.
%b. Determine the set of all the pairs of elements in a list. E,g,
%with[a b c d] will produce [[a b] [a c] [a d] [b c] [b d] [c d]].

apartine(E,[E|_]).
apartine(E,[_|T]):-apartine(E,T).

union([],L,L):-!.
union([H|T],L,[H|T2]):- \+ apartine(H,L),union(T,L,T2).
union([_|T],L,T2):- union(T,L,T2).



imperechere(_,[],[]):-!.
imperechere(E,[H|T],R):-imperechere(E,T,R1), R = [[E,H]|R1].

concatenare([],L,L).
concatenare([H|L1],L2,[H|L3]):-
	concatenare(L1,L2,L3).

perechi([],[]):-!.
perechi([H|T],R):- imperechere(H,T,R1),perechi(T,R2),concatenare(R1,R2,R).









