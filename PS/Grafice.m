function Grafice
%deseneaza grafice
close all

x=0:0.01:3;
y1=x.^4/4;
y2=x.*sin(x);
y3=cos(x);

figure(1)
plot(x,y1)
figure(2)
plot(x,y2,'color','r')
figure(3)
plot(x,y3,'color','k','LineWidth',2)
figure(4)
hold on
plot(x,y1)
plot(x,y2,'r')

m=0;
s=1;
