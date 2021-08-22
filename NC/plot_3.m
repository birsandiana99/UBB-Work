f = @(x) exp(sin(x));

nodes = [1,2,3,4,5];
values = [22,23,25,30,28];
clf;
hold on;

plot(nodes,values,'o','markerfacecolor','red');

X = linspace(1,5,1000);
plot(X, newton_formula(nodes,values,X),'--k','linewidth',5);


plot(X, lagrange_barycentric(nodes,values,X));