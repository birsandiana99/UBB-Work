function X_new = jacobi(A, b, N)
  # N - nr of iterations
  # n - nr of components
  X_old = zeros(size(b));
  n = length(b);
  X_new = X_old;
  for k=1:N
    for i=1:n
      X_new(i) = 1/A(i,i) * (b(i) - ...
      A(i,1:i-1) * X_old(1:i-1) - ...
      A(i,i+1:n) * X_old(i+1:n));
    endfor
    X_old = X_new;
  endfor
endfunction
