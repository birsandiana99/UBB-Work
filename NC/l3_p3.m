f = @(x) (1+cos(pi*x)) ./ (1 + x);
clf;
hold on;
nodes = linspace(0,10,21);

values = f(nodes);


fplot(f,[0,10]);

plot(nodes,values,'o','markerfacecolor','red');

X = linspace(0,10,100);
plot(X, lagrange_barycentric(nodes,values,X));