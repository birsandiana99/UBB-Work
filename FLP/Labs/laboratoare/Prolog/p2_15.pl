%15. Given a linear numerical list remove all sequences of consecutive
% values.E.g. remove([1, 2, 4, 6, 7, 8, 10], L) will produce L=[4, 10].
elimin([],[]).
elimin([H1|[H2|[H3|T]]],L):-
	H3=:=H2+1,
	H2=:=H1+1,!,
	L1=[H2|[H3|T]],
	elimin(L1,L).
elimin([H1|[H2|[H3|T]]],L):-
	H2=:=H1+1,
	H3=\=H2+1,!,
	L1=[H3|T],
	elimin(L1,L).
elimin([H1|[H2|[]]],[]):-H2=:=H1+1,!.
elimin([H|T],[H|L]):-elimin(T,L).
