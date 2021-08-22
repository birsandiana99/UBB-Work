%3.
%  a. Insert an element onto the n-th position of a list.
%  b. Define a predicate to determine the greatest common divisor of all
%     numbers in a list.
insert(E,1,L,[E|L]):-!.
insert(E,N,[H|T],[H|R1]):- N1 is N - 1,insert(E,N1,T,R1).


cmmdc(A,A,R):-R=A,!.
cmmdc(A,B,R):-A>B,
	C is A-B,
	cmmdc(C,B,R).
cmmdc(A,B,R):-A<B,
	C is B-A,
	cmmdc(A,C,R).
cmmdcList([H],H):-!.
cmmdcList([H1,H2|T],R):-
	cmmdc(H1,H2,R1),
	cmmdcList([R1|T],R).
