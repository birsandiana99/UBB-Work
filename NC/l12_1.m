f = @(x) (x-2)^2 - log(x);
a = 1;
b = 2;
[c,i]=bisection(f,a,b,err=1e-12,max_iter=100)
[c,i]=false_position(f,a,b,err=1e-12,max_iter=100)
%fzero(f,[a,b]) - check