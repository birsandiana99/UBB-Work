isInDescendingOrder([H1,H2|T]):-
H1 > H2,!,
isInDescendingOrder([H2|T]).
isInDescendingOrder([H1,H2|T]):-
H1 < H2,!,
isInAscendingOrder([H2|T]).

isInAscendingOrder([_]):-!.
isInAscendingOrder([H1,H2|T]):-
H1 < H2,!,
isInAscendingOrder([H2|T]).

hasValleyAspect([H1,H2|T]):-
H1 > H2,!,
isInDescendingOrder([H2|T]).
