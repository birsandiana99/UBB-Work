maxim([H],H).
maxim([H|T],R):-
	maxim(T,R1),
	R1>H,
	R is R1.
maxim([H|T],R):-
	maxim(T,R1),R1=<H,R is H.


concatenare([H|T1],L2,[H|L3]):-
	concatenare(T1,L2,L3).
concatenare([],L,L).
subst([],_,_,[]).
subst([H|T],E,L,R):-
	subst(T,E,L,R1),
	H=\=E,
	R=[H|R1].
subst([H|T],E,L,R):-
	subst(T,E,L,R1),
	H=:=E,
	append(L,R1,R).

final(L,L1,R):-
	maxim(L,M),
	subst(L,M,L1,R).
































