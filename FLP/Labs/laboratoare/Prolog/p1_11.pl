%11.
%  a. Test whether a list is a set.
%  b. Remove the first three occurences of an element in a list. If the
%  element occurs less than three times, all occurences will be removed.
%-----A----
apare(E,[E|_]).
apare(E,[_|T]):-apare(E,T).

testSet([]):-!.
testSet([H|T]):-
	apare(H,T),!,
	false.
testSet([H|T]):-
	\+apare(H,T),!,
	testSet(T).
%------B---------
rem(E,L,R):-
	remove(E,3,L,R).
remove(_,_,[],[]).
remove(E,N,[E|T],L):-
	N=:=1,!,
	L=T.
remove(E,N,[E|T],L):-
	N>1,
	N1 is N-1,!,
	remove(E,N1,T,L).
remove(E,N,[H|T],[H|L]):-remove(E,N,T,L).











