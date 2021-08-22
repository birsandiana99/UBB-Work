%13. Determine the product of a number represented as digits in a list
% to a given digit. E.g.: [1 9 3 5 9 9] * 2 --> [3 8 7 1 9 8]
adauga_sf(E,[],[E]).
	adauga_sf(E,[H|T],[H|L]):-adauga_sf(E,T,L).

	invers([],[]).
	invers([H|T],L):-invers(T,S),adauga_sf(H,S,L).

	produs([],_,[]):-!.
	produs(L,V,LL):-invers(L,L1),prod(L1,V,L2,0),invers(L2,LL).

	prod([],_,[],0):-!.
	prod([],_,[N],N).
	prod([H|T],V,[M|L],N):- N=:=0,P is V*H,M is P mod 10,N1 is P div 10,prod(T,V,L,N1).
	prod([H|T],V,[M|L],N):- N=\=0,P is V*H+N,M is P mod 10,N1 is P div 10,prod(T,V,L,N1).
