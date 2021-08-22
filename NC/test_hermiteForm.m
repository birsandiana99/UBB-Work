nodes=[0 3 5 8 13];
values=[0 225 383 623 993];
der_values=[75 77 80 74 72];

clf; hold on;
X = linspace(0,13,100);
Y = linspace(0,993,100);
[H, dH] = hermiteForm(nodes, values, der_values, X);
#H respect to time
subplot(3,1,1)
plot(X, H);

#dH respect to time
subplot(3,1,2)
plot(X, dH);

#dH respect to distance
subplot(3,1,3)
plot(Y, dH);

#plot picture of H with respect to time and dH with respect to time
# and dH with respect to distance
