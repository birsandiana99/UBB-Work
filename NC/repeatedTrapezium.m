function area = repeatedTrapezium(a,b,n,f)
  area=0;
  nodes=linspace(a,b,n+1);
  for i=1:length(nodes)-1
    area=area + ((f(nodes(i+1))+f(nodes(i)))/2)...
         *((nodes(i+1)-nodes(i)));
  endfor
endfunction


