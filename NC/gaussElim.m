function x = gaussElim(A, b)
  n = length(b);
  A = [A b];
  
  for k = 1: n-1
    #A(k:n, k)
    #look for the line that starts with the max element
   [val, pos] = max(A(k:n,k));
   pos = pos + k - 1;
   if pos != k 
     A([k,pos], k:end) = A([pos,k], k:end);
   endif
   for i = k+1:n
     m = A(i,k) / A(k,k);
     A(i, k:end) = A(i, k:end) - m* A(k,k:end);
   endfor
  endfor
  
  b = A(:,end);
  A(:,end) = [];
  x = triangular(A,b);
endfunction