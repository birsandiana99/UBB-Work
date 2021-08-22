clear all
close all

n=100;
p=0.03;
lambda=n*p;
k=0:n;

X=pdf('bino',k,n,p);
figure(1)
hold on
bar(k,X,'b');

Z=pdf('poiss',k,lambda);
figure(2)
bar(k,Z,'r');

figure(3)
bar(k,[X',Z']);