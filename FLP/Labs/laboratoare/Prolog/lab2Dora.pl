%domains
%el=integer-R,R1,R2
%list=el*-L,L1,L2,L3
%predicates
%   invert(list)->list;
%   concatenare(list,list)->list;
%   toNumber(list)->integer;
%   diff(list,list)->integer;
%clauses
invert([],[]):-!.
invert([H|L],R):-invert(L,R1),concatenare(R1,[H],R).

 concatenare([],L,L).
 concatenare([H|L1],L2,[H|L3]):-
	concatenare(L1,L2,L3).


toNumber([],0):-!.
toNumber([H|L],R):-toNumber(L,R1), R2 is R1 * 10, R is R2 + H.


diff(L1,L2,R):-invert(L1,LA1),invert(L2,LA2),toNumber(LA1,N1),toNumber(LA2,N2),R is N1 - N2.
