function T=romberg(f,a,b,n)
  T = nan(n);
  for i=1:n
    T(i,1) = repeatedTrapezium(a,b,2^(i-1),f);
    for j=2:i
      T(i,j) = (4^ (-j+1) * T(i-1,j-1) - T(i, j-1))/...
      (4^(-j+1) - 1);
    endfor
  endfor
  % n - nr of lines in matrix
  endfunction