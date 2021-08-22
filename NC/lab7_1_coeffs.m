x = [1 2 3 4 5 6 7];
f = [13 15 20 14 15 13 10];
clf;hold on;
plot(nodes,values,'x')
m = 6;
%function [a,b] = find_coeffs(nodes, values, m)
  a = ((m+1)*sum(x.*f) - sum(x)*sum(f))/((m+1)*sum(x.^2) - (sum(x))^2)
  b = ((sum(x.^2)*(sum(f))) - (sum(x.*f)*sum(x)))/((m+1) * sum(x.^2) - (sum(x))^2)
%endfunction


p = @(x) (a*x+b);
p(3.5);
fplot(p,[0,8]);
E = norm(f-p(x)) ^ 2 %expr of the error

polyfit(x,f,2)





