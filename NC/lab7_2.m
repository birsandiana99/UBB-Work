clf;
nodes=[0 10 20 30 40 60 80 100];
values=[0.0061 0.0123 0.0234 0.0424 0.0738 0.1992 0.4736 1.0133];

[c,b,a]=polyfit(nodes,values,2)

