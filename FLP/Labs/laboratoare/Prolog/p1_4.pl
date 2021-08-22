%4.
%  a. Substitute all occurences of a certain element of a list with
%  another element.
%  b. Build the sublist (lm, ..., ln) of the list (l1, ..., lk).

substitute(_,_,[],[]).
substitute(E1,E2,[E1|T],R):-
	substitute(E1,E2,T,R1),
	R=[E2|R1].
substitute(E1,E2,[H|T],R):-
	substitute(E1,E2,T,R1),
	R=[H|R1].

sublist([],_,_,[]):-!.
sublist(_,M,N,[]):-M>N,!.
sublist([H|T],M,N,[H|R]):-
	M=<1,N>=1,!,M1 is M-1,N1 is N-1,
	sublist(T,M1,N1,R).
sublist([_|T],M,N,R):-
	M1 is M-1,N1 is N-1,
	sublist(T,M1,N1,R).



