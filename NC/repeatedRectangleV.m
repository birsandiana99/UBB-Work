function surface = repeatedRectangleV(a,b,n,f)  surface = 0;  f=@(x) 4./(1+x.^2);  h=(b-a)/n;    midPoints = (a+h/2):h:(b-h/2);    surface = sum(f(midPoints)) * h;endfunction