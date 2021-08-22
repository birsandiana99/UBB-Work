% 2. Determine the predecessor of a number represented as digits in a
% list. E.g.:
%    [1 9 3 6 0 0] --> [1 9 3 5 9 9]

adauga_sf(E,[],[E]):-!.
adauga_sf(E,[H|T],[H|L]):-adauga_sf(E,T,L).

invers([],[]).
invers([H|T],L):-invers(T,L1),adauga_sf(H,L1,L).

predecesor([],[]):-!.
predecesor(L,R):-invers(L,L1),pred(L1,S,1),invers(S,R).

pred([],[],_).
pred([H|T],[H|L],N):- N=:=0,!,pred(T,L,0).
pred([H|T],[M|L],N):- N=\=0,N=<H,M is H-N, pred(T,L,0).
pred([H|T],[M|L],N):- N=:=1,H=:=0,M is 10-N,pred(T,L,1).

