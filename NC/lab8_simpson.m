function area = lab8_simpson(a,b,n,f)
  area=0;
  nodes=linspace(a,b,n+1);
  for i=1:length(nodes)-1
    b = nodes(i+1);
    a = nodes(i);
    
    area = area + (b-a)/6 * (f(a) + 4*f((a+b)/2) + f(b));
   
  endfor
endfunction

