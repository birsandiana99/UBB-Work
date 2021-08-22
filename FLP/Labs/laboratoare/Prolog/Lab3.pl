nocons([],[]):-!.
nocons([_],[]):-!.
nocons([A,B|L], R):- B=:=A+1,!,nocons([B|L],R).
nocons([_|L],L).

final([],[]):-!.
final([H],[H]):-!.
final([A,B|L],R):- B=:=A+1,!,nocons([B|L],R1),final(R1,R).
final([A,B|L],[A|R]):- final([B|L],R).
