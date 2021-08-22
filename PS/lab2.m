clear all
n=3;
p=0.5;
k=0:n;

Y=pdf('bino',k,n,p);
figure(1)
hold on
plot(k,Y,'b*')

Z=cdf('bino',k,n,p);
figure(2)
hold on
plot(k,Z,'ro')

figure(3)
stairs(Z)

C=pdf('bino',0,n,p);

C1=1-pdf('bino',1,n,p);

D=cdf('bino',2,n,p);
D1=cdf('bino',1,n,p);

E=1-cdf('bino',0,n,p);
E1=1-cdf('bino',1,n,p);

N=5000;
A=rand(3,N);
x=sum(A<0.5);
v(1)=sum(x==0)/N;
v(2)=sum(x==1)/N;
v(3)=sum(x==2)/N;
v(4)=sum(x==3)/N;
figure(1)
plot(k,v,'gs');