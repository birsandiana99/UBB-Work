%sub(L:list,R:list)
% L - list from where sublists are extracted
% R - one for the extracted sublists
% (i,o)
sub([],[]):-!.
sub([_|L],R):-sub(L,R).
sub([H|L],R):-sub(L,R1),R = [H|R1].

%colinearList(L:list)
% L - list of points to be checked if they are colinear
% (i)
colinearList([point(_,_),point(_,_)]):-!.
colinearList([point(X1,Y1),point(X2,Y2),point(X3,Y3)|L]):-
	(X1-X2) * (Y2-Y3) =:= (Y1-Y2) * (X2-X3),
	colinearList([point(X2,Y2),point(X3,Y3)|L]).

%check(L:list,R:list)
% L - list of lists of points to be checked if they are all colinear
% R - list of lists that corespond to the given condition
% (i,o)
check([],[]):-!.
check([H|L],R):-colinearList(H),check(L,R1),R = [H|R1],!.
check([H|L],R):- \+ colinearList(H),check(L,R).

%finalCheck(L:list,R:list)
% L - list of point from where sublists of colinear point are extracted
% R - list of lists of point ther reprezent sublists of L containing
% only colinear points
% (i,o)
finalCheck(L,R):- findall(A,sub(L,A),AS),check(AS,R),!.
