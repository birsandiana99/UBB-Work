function table = finite_diff(values)
  table = nan(length(values));
  
  table(:,1) = values;
  
  for col=2:length(values)
    for k=1:length(values)+1-col
      table(k,col)=table(k+1,col-1) - table(k,col-1)
    endfor
  endfor
  endfunction