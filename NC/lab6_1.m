nodes = linspace(0,2*pi,5);
values = [0 1 0 -1 0];

pp = csape(nodes, values, 'variational');

ppval(pp, pi/4)
sin(pi/4)