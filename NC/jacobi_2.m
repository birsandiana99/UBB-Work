function [X_new, iterations] = jacobi_2(A,b,err=1e-10)
  M = diag(diag(A));
  N = M-A;
  c = M\b;
  T = M\N;
  X_old = zeros(size(b));
  X_new = X_old;
  iterations = 1;
  while iterations < 1000
    X_new = c+T*X_old;
    if norm(T,inf)/(1-norm(T,inf)) * norm(X_old - X_new, Inf) <= err
      return
    endif
    X_old = X_new;
    iterations++;
  endwhile
  endfunction