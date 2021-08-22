%7. a. Transform a list in a set, in the order of the first appearance.
% E.g:[1,2,3,1,2] is transformed in [1,2,3].
%b. Decompose a list of numbers in a list of the form
%[ lista-de-numere-pare lista-de-numere-impare] (i.e. list with two list
% elements), and will also return the number of odd elements and the
% number of even elementelor.

%A
sterge(_,[],[]).
sterge(E,[E|T],T1):-sterge(E,T,T1),!.
sterge(E,[H|T],[H|T1]):-sterge(E,T,T1).

multime([],[]):-!.
multime([H|T],[H|L]):-sterge(H,T,T1),multime(T1,L).

%B
numar([],0,0).
numar([H|T],P,I):- H mod 2=:=0,!,numar(T,P1,I),P is P1+1.
numar([H|T],P,I):- H mod 2=:=1,!,numar(T,P,I1),I is I1+1.

separare([],[],[]).
separare([H|T],P,I):- H mod 2=:=0,!,separare(T,P1,I),P=[H|P1].
separare([H|T],P,I):- H mod 2=:=1,!,separare(T,P,I1),I=[H|I1].

final(L,R,P,I):-numar(L,P,I),separare(L,LP,LI),R=[LP,LI].




