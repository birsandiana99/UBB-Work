%14. Determine the positions of the minimum element in a linear list.
% E.g.:pos([10,-14,12,13,-14], L) will produce L = [2,5].
minim(32000,[]):-!.
minim(M,[H|T]):-
	minim(M,T),
	M<H,!.
minim(M,[M|_]):-!.


detPoz(_,_,[],[]).
detPoz(E,N,[E|T],[N|L]):-!,
	N1 is N+1,
	detPoz(E,N1,T,L).
detPoz(E,N,[H|T],L):-N1 is N+1,detPoz(E,N1,T,L).

pozitii2(L,L1):-minim(M,L),
	detPoz(M,1,L,L1).
