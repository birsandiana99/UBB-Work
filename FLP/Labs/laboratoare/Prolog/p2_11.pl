%11. Determine the position of the maximal element of a linear list.
% E.g.:maxpos([10,14,12,13,14], L) produces L = [2,5].
maxim([],-32000).
maxim([H|T],H):-maxim(T,M),M<H,!.
maxim([_|T],M):-maxim(T,M).

pozitii([],[]):-!.
pozitii(L,R):-maxim(L,M),pozitie(L,R,M,1).
pozitie([],[],_,_):-!.
pozitie([H|T],[P|R],M,P):- H=:=M,!,P1 is P+1, pozitie(T,R,M,P1).
pozitie([_|T],R,M,P):-P1 is P+1,pozitie(T,R,M,P1).
