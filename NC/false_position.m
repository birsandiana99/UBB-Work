function [c,i]=false_position(f,a,b,err=1e-12,max_iter=100)
  
  for i=1:max_iter
    c = (a*f(b)- b*f(a)) / (f(b)-f(a));
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