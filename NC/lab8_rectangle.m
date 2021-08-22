function area = repeatedRectangle(a,b,n,f)
  area=0;
  nodes=linspace(a,b,n);
  for i=1:length(nodes)-1
    area=area + f((nodes(i+1)+nodes(i))/2)...
         *((nodes(i+1)-nodes(i)));
  endfor
endfunction