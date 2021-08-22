function x = triangular( A, b)
  % A = n x n matrix
  % b - column matrix 
  % the linear system is A * x = b
  n = length(b);
  x = zeros(n,1); %column matrix
  for i = n:-1:1 % lines
    x(i) =  (b(i) - A(i, i+1:n) * x(i+1:n)) / A(i,i);
  endfor
  endfunction