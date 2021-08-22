nodes = [1930:10:1980];
values = [123203,131669,150697,179323,203212,226505];
clc; hold on;
plot(nodes,values,'o','markerfacecolor','red');

X = linspace(1930,1980,1000);
plot(X, lagrange_barycentric(nodes,values,X));