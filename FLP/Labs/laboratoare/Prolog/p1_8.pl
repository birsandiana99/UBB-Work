%8.a. Compute the difference of two sets.
%  b. Build a list by inserting the value 1 after each even element of
%  the given list.
apare(E,[E|_]).
apare(E,[_|T]):-apare(E,T).
%---A---
difference([],_,[]).
difference(L,[],L):-!.
difference([H|T],L,R):-
	\+apare(H,L),!,
	R=[H|R1],
	difference(T,L,R1).
difference([H|T],L,R):-
	apare(H,L),!,
	difference(T,L,R).

%---B---

add([],[]).
add([H|T],[H|[1|T1]]):-H mod 2=:=0,!,
	add(T,T1).
add([H|T],[H|T1]):-add(T,T1).






