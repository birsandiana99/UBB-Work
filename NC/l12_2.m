f = @(x) x^3 - x^2 - 1
fd = @(x) 3*x^2 - 2*x 
x0 = 1;
x1 = 2;
[x,i] = secant_method(f,x0,x1,err=1e-12,max_iter=100)
[c,i]=bisection(f,x0,x1,err=1e-12,max_iter=100)


[c,i]=newton(f,fd,x0,err=1e-12,max_iter=100)
