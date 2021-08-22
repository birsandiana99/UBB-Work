%6.a. Compute the intersection of two sets.
% b. Build the list (m, ..., n) of all the integer numbers in the
% interval[m, n].
%A
apare(E,[E|_]).
apare(E,[_|T]):-apare(E,T).

intersectie([],_,[]).
intersectie([H|T],T1,[H|L]):-apare(H,T1),intersectie(T,T1,L).
intersectie([H|T],T1,L):- \+ apare(H,T1),intersectie(T,[H|T1],L).


interval(M,N,[]):-M>N,!.
interval(M,N,[M|R]):-
	M=<N,
	M1 is M+1,
	interval(M1,N,R).
