function table = divided_diff_double(nodes,values, der_val)
  n = 2*length(values);
  table = nan(n);
  

  double_nodes = repelem(nodes,2);
    
  table(:,1) = repelem(values,2);
  #second column
  table(1:2:end-1,2) = transpose(der_val);
  table(2:2:end-2,2) = diff(values)'./diff(nodes)';
  
  for col=3:n
    for k=1:n+1-col
      table(k,col)=(table(k+1,col-1) - table(k,col-1))/...
      (double_nodes(k+col-1)-double_nodes(k));
      
    endfor
  endfor
  endfunction
  
 # divided_diff([1:5],[3;5;2;1;7])
 # 