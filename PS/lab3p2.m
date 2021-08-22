clear all
close all
n=100;
p=0.65;
k=0:n;
mu=n*p;
sig=sqrt(n*p*(1-p));

X=pdf('bino',k,n,p);
figure(1)
hold on
bar(k,X,'b');

x=mu-3*sig:0.01:mu+3*sig;
Z=pdf('normal',x,mu,sig);
plot(x,Z,'Color','r','LineWidth',2);