f = @(x) 100 ./ (x .^ 2) .* sin(10 ./ x);
L = adquad(1,3,1e-10,f) 
