%domains
%el=integer
%list=el*
%N1=integer
%N=integer
%predicates.
%      nthel(list,integer)
%      mult(list,list)
%      member(el,list)
%      egal(list,list)
%
%clauses.

nthel([H|T],1):-
	write(H).

nthel([H|T],N):-
	N1 is N-1,
	nthel(T,N1).

member(E,[E|_]):-
	!.

member(E,[_|T]):-
	member(E,T).

mult([],L):-
	!.

mult([H|T],L):-
	member(H,L),
	mult(T,L).

egal(L1,L2):-mult(L1,L2),mult(L2,L1).




