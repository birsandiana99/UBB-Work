%check if number is prime
prim(E,E):-true.
prim(E,D):-
	E mod D=:=0,false.
prim(E,D):-
	E mod D=\=0,!,
	D1 is D+1,
	prim(E,D1).
checkPrim(E):-prim(E,2).

addPrim([H|T],[H|[1|[H|R]]]):-
	checkPrim(H),!,addPrim(T,R).
addPrim([H|T],[H|R]):-
	\+checkPrim(H),!,addPrim(T,R).
addPrim([],[]).
isDivizor(E,D):-
	E mod D=:=0,
	true.
isDivizor(E,D):-
	E mod D=\=0,
	false.
%get list of divisors
divizor(E,[],E).

divizor(E,L,D):-
        isDivizor(E,D),!,
	divizor(E,L1,D1),
	L=[D|L1],
	D1 is D+1.
divizor(E,L,D):-
	\+ isDivizor(E,D),!,
	divizor(E,L,D1),
	D1 is D+1.
divizori(E,R):-divizor(E,R,2).
