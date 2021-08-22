f = @(E) E - 0.8*sin(E) - 2*pi / 10;
fd = @(E) 1-0.8*cos(E);
E0 = 1;
newton(f,fd,E0,err=1e-12,6)