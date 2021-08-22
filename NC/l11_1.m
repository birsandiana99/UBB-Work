n = 10;
A = diag(-ones(n-1,1),-1) + diag(3* ones(n,1),0) + diag(-ones(n-1,1),1);
b = [2;ones(n-2,1);2];
#A\b

##iterations = 20;
##X1 = jacobi(A,b,iterations)
##%norm(A\b - X, Inf);
##
##X2 = gauss_siedel(A,b,iterations)
##%norm(A\b - X, Inf)
##
##X3 = SOR(A,b,iterations, 1.15 )

[X, iter] = jacobi_2(A,b)
[X, iter] = gauss_2(A,b)
[X, iter] = SOR_2(A,b, 1.15)