function L=LagrangeBary(nodes,values,X)
  %nodes: x1,...,xn
  %values: f(x1),...,f(xn)
  %set of points: X
  w=CoeffBary(nodes); 
  for j=1:length(X)
    x_pos_node=find(nodes==X(j));
    %returns the position of the node equal to x(j)
    if x_pos_node
      L(j)=values(x_pos_node);
    else
      L(j)=sum(w.*values./(X(j)-nodes))/...
              sum(w./(X(j)-nodes));
    endif
  endfor
endfunction

function w=CoeffBary(nodes)
  w=nodes;
  for i=1:length(nodes)
    w(i)=1/prod(nodes(i)-nodes(nodes~=nodes(i)));
  endfor
endfunction
