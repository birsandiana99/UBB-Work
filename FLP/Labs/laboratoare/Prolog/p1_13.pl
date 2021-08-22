%13.
%a.Substitute in a list a value with all the elements of another list.
%b. Remove the n-th element of a list.

%----A=P2_12--------



%--------B--------
delete([],_,[]).
delete([H|T],1,T):-!.
delete([H|T],N,[H|L]):-
	N1 is N-1,
	delete(T,N1,L).
