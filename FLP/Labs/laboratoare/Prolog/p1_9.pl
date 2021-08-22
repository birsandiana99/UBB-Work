%9.
%  a. Transform a list in a set, in the order of the last appearance.
%  E.g.: [1,2,3,1,2] is transformed in [3,1,2].
%b. Define a predicate to determine the greatest common divisor of all
%     numbers in a list.
adaug_sf(E, [], [E]).
adaug_sf(E, [H|T], [H|T1]) :- adaug_sf(E, T, T1).
invers([], []).
invers([H|T], L) :- invers(T, L1), adaug_sf(H, L1, L).
member(E, [E|_]) :- !.
member(E, [_|T]) :- member(E, T).
multime([], []).
multime([H|T], [H|L]) :- not(member(H,T)),!,multime(T,L).
multime([_|T],L):- multime(T,L).
