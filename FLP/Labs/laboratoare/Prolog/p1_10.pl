%10.
%  a. Determine the least common multiple of all elements of a linear
%  numerical list.
%  b. Insert a given value v after the 1-st, 2-nd, 4-th, 8-th ...element of a list.
%----A----
cmmdc(A,A,R):-R=A,!.
cmmdc(A,B,R):-A>B,
	C is A-B,
	cmmdc(C,B,R).
cmmdc(A,B,R):-A<B,
	C is B-A,
	cmmdc(A,C,R).
cmmmc(A,A,R):-R=A,!.
cmmmc(A,B,R):-
	cmmdc(A,B,C),!,
	R is A*B/C.
%-----B-----
inserare(V,[H|T],P1,P2,R):-
	P1=:=P2,!,
	P3 is P1*2,
	P4 is P2+1,
	inserare(V,T,P3,P4,R1),
	R=[H|[V|R1]].
inserare(V,[H|T],P1,P2,R):-
	P1=\=P2,!,
	P4 is P2+1,
	inserare(V,T,P1,P4,R1),
	R=[H|R1].
inserare(_,[],_,_,[]):-!.
