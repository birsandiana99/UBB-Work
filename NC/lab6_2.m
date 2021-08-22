nodes = [0 pi/6 pi/4 pi/3 pi/2];
values = [0 1/2 sqrt(2)/2 sqrt(3)/2 1];

pp = csape(nodes, values, 'variational');

ppval(pp, [pi/7, 1/2, 2/3, 1])
sin([pi/7, 1/2, 2/3, 1])