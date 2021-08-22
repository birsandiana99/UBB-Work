A = [10,7,8,7;7,5,6,5;8,6,10,9;7,5,9,10];
b =[32;23;33;31];
%triu(A)
%tril(A)
%triu(A) * x
bb = [32.1;22.9;33.1;30.9];
x = gaussElim(A, b);
x = gaussElim(A, bb);
%x = triangular(triu(A),b);

cond(A);


AA = [10,7,8.1,7.2;7.08,5.04,6,5;8,5.98,9.89,9;6.99,4.99,9,9.98];
x = gaussElim(A, b)
x = gaussElim(AA, b)

cond(A)


