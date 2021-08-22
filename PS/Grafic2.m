function Grafic2
close all
x=-3:0.01:3;
m=0;
s=1;
f=1/(2*pi*s)*exp(-(x-m).^2/(2*s));

figure(1)
hold on
plot(x,f,'color','m')

m1=-1;
m2=1;
f1=1/(2*pi*s)*exp(-(x-m1).^2/(2*s));
f2=1/(2*pi*s)*exp(-(x-m2).^2/(2*s));

figure(2)
hold on
plot(x,f,'b')
plot(x,f1,'r')
plot(x,f2,'k')
title('Gauss')
xlabel('x')
ylabel('f(x)')

s1=2;
s2=3;
f3=1/(2*pi*s1)*exp(-(x-m).^2/(2*s1));
f4=1/(2*pi*s2)*exp(-(x-m).^2/(2*s2));
figure(3)
hold on
plot(x,f,'b')
plot(x,f3,'r')
plot(x,f4,'k')
legend('s=1','s=2','s=3')
%s este varianta si se noteaza cu sigma patrat