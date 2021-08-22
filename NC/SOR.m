function X_new = SOR(A, b, N, omega)
  # N - nr of iterations
  # n - nr of components
  X_old = zeros(size(b));
  n = length(b);
  X_new = X_old;
  for k=1:N
    for i=1:n
      X_new(i) = omega/A(i,i) * (b(i) - ...
      A(i,1:i-1) * X_new(1:i-1) - ...
      A(i,i+1:n) * X_old(i+1:n)) + (1-omega) * X_old(i);
    endfor
    X_old = X_new;
  endfor
endfunction
