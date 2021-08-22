function L = lagrange_barycentric(nodes, values, X)
  A = bary_coef(nodes);
  L = zeros(size(X));
  for j=1:length(X)
    in = find(nodes==X(j));
    if length(in) > 0
      L(j) = values(in(1));
    else
      nominator = 0;
      denominator = 0;
      for i = 1:length(nodes)
        nominator = nominator + (A(i) * values(i)) / (X(j) - nodes(i));
        denominator = denominator + A(i) / (X(j) - nodes(i));
      endfor
      L(j) = nominator/denominator;
    endif
  endfor
endfunction

function A = bary_coef(nodes)
  A = ones(size(nodes));
  for i=1:length(nodes)
    for j=1:length(nodes)
      if i!=j
        A(i) = A(i) / (nodes(i)-nodes(j));
      endif
    endfor
  endfor
endfunction