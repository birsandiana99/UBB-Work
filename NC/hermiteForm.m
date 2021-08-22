function [H, dH] = hermiteForm(nodes, values, der_values, X)
  table = divided_diff_double(nodes, values, der_values);
  coefs = table(1,:);
  double_nodes = repelem(nodes,2);
  H = X;
  dH = X;
  for i=1:length(X)
    H(i) = coefs(1);
    dH(i) = 0;
    P = 1;
    dP = 0;
    for j=2:length(coefs)
      dP = dP * (X(i) - double_nodes(j-1)) + P;
      P = P * (X(i) - double_nodes(j-1));
      H(i) = H(i) + P * coefs(j);
      dH(i) = dH(i) + dP * coefs(j);
    endfor
  endfor
endfunction