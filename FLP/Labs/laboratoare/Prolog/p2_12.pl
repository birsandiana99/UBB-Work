%12. Substitute all occurences of an element of a list with all the
% elements of another list. E.g. subst([1,2,1,3,1,4],1,[10,11],X) produces
%    X=[10,11,2,10,11,3,10,11,4].
concatenare([],L,L).
concatenare([H|L1],L2,[H|L3]):-
	concatenare(L1,L2,L3).

subst(_,_,[],[]).
subst(E,L,[E|T],R):-
	subst(E,L,T,R1),!,
	concatenare(L,R1,R).
subst(E,L,[H|T],[H|R]):-
	subst(E,L,T,R).
