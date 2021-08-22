%15.a. Define a predicate to test if a list of an integer elements has a"valley"
% aspect (a set has a "valley" aspect if elements decreases up to a
%certain point, and then increases. (ex: 10 8 6 9 11 13)
%  b. Calculate the sum of alternating elements of a list. (l1 - l2 + l3 ...)

valleyDown([H1|[H2|T]]):-
	H2>H1,!,false.
valleyDown([H1|[H2|T]]):-
	H1=<H2,!,
	valleyDown([H2|T]).


valleyUp([H1|[H2|T]]):-
	H2<H1,!,false.
valleyUp([H1|[H2|T]]):-
	H1>=H2,!,
	valleyUp([H2|T]).
