function [x,i]=secant_method(f,x0,x1,err=1e-12,max_iter=100)
  
  for i=1:max_iter
    x = (x0*f(x1)- x1*f(x0)) / (f(x1)-f(x0));
    if abs(x-x1) < err || abs(f(x)) < err
      return
    endif
    x0=x1;
    x1=x;
  endfor
  
  endfunction