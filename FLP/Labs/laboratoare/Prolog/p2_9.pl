%9. Merge two sorted lists with keeping the double values.
inter([],[],[]).
inter([],L2,L2):-!.
inter(L1,[],L1):-!.
inter([H1|L1],[H2|L2],[H1|L3]):- H1<H2,!,
	L=[H2|L2],
	inter(L1,L,L3).
inter([H1|L1],[H2|L2],[H2|L3]):- H1>=H2,!,
	L=[H1|L1],
	inter(L,L2,L3).

%10.Merge 2 sorted lists without keeping the double values


inter2([],[],[]):-!.
inter2([],L,L):-!.
inter2(L,[],L):-!.
inter2([H|T],[H1|T1],[H|L]):- H<H1,!,inter2(T,[H1|T1],L).
inter2([H|T],[H1|T1],[H1|L]):- H>H1,!,inter2([H|T],T1,L).
inter2([H|T],[H1|T1],[H|L]):- H=:=H1,!,inter2(T,T1,L).
