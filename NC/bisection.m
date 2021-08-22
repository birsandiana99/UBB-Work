function [c,i]=bisection(f,a,b,err=1e-12,max_iter=100)
  
  for i=1:max_iter
    c = (a+b)/2;
    if abs(b-a) < err || abs(f(c)) < err
      return
    endif
    
    if f(a) * f(c) < 0
      b = c;
    else
      a = c;
    endif
  endfor
  
  endfunction