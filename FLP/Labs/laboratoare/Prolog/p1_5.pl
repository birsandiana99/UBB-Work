%5.a. The predicate should return success if the list has an even number
% of elements, and will fail otherwise; the elements of the list will not
% be counted.
%b. Compute the alternate sum of the elements of a list (l1- l2 + l3 ...).

length([]).
length([H|[H1|T]]):-length(T).

altsum([],_,_).
altsum([H|T],P,R):-
	P=:=1,!,
	altsum(T,2,H).
altsum([H|T],P,R):-
	P mod 2=:=0,!,
	P1 is P+1,
	R1 is R-H,
	altsum(T,P1,R1).
altsum([H|T],P,R):-
	P mod 2=:=1,!,
	P1 is P+1,
	R1 is R+H,
	altsum(T,P1,R1).
elsum(L,R):-altsum(L,1,R).


