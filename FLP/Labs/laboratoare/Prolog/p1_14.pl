%14.
%a.Define a predicate to remove from a list all recurring
%(repetitive) elements. (ex: l=[1,2,1,4,1,3,4] => l=[2,3])
% b.Remove all occurrence for a maximum value from a list on
% integer numbers.
%----A----
apare(E,[E|_]).
apare(E,[_|T]):-
	apare(E,T).
sterge(_,[],[]).
sterge(E,[E|T],T1):-sterge(E,T,T1),!.
sterge(E,[H|T],[H|T1]):-sterge(E,T,T1).

sterge2([],[]).
sterge2([H|T],R):-
	apare(H,T),!,
	sterge(H,T,R1),
	sterge2(R1,R).
sterge2([H|T],[H|L]):-
	sterge2(T,L).

%----B----
maxim([],-32000).
maxim([H|T],H):-maxim(T,M),M<H,!.
maxim([_|T],M):-maxim(T,M).

stergeMax([],[]).
stergeMax(L,R):-
	maxim(L,M),
	sterge(M,L,R).


