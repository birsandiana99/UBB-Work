function L = newton_formula(nodes, values, x)
  
  table = divided_diff(nodes, values);
  coefs = table(1,:);
  L = x;
  for i=1:length(x)
    L(i) = coefs(1); 
    product = 1;
    
    for j=2:length(coefs)
      product = product * (x(i)-nodes(j-1));
      L(i) = L(i) + product * coefs(j);
    endfor
  endfor
endfunction

#newton_formula([1,1.5,2,3,4],[0,0.17609,0.30103,0.47712,0.60206],[2.5,3.25])

#Y=1:0.1:3.5
  #max(abs(log10(Y)-newton_formula([1,1.5,2,3,4],[0,0.17609,0.30103,0.47712,0.60206],Y)))
  #ans = 2.6495e-03