f = @(x) 4./(1+x.^2);
T = romberg(f,0,1,10) 
fplot(f,[0,1])
ylim([0,4])