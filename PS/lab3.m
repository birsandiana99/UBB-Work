clear all
mu=1;
sig=1;
normal=cdf('normal',0,mu,sig);

%p1

n=10;
T=cdf('t',0,n);

%sub. 1)

sub11=cdf('normal',0,mu,sig);
sub12=1-cdf('normal',0,mu,sig);

sub11T=cdf('t',0,n);
sub12T=1-cdf('t',0,n);

fprintf('%1.4f ',sub11,sub12,sub11T,sub12T);
fprintf('\n');
%sub. 2)

sub21=cdf('normal',1,mu,sig)-cdf('normal',-1,mu,sig);
sub22=1-sub21;

sub21T=cdf('t',1,n)-cdf('t',-1,n);
sub22T=1-sub21;

fprintf('%1.4f ',sub21,sub22,sub21T,sub22T);
fprintf('\n');
%sub. 3)

alpha=0.25;
Xalpha=icdf('normal',alpha,mu,sig);
XalphaT=icdf('t',alpha,n);

fprintf('%1.4f ',Xalpha,XalphaT);
fprintf('\n');

%sub. 4)

beta=0.35;
Xbeta=1-icdf('normal',beta,mu,sig);
XbetaT=1-icdf('t',beta,n);

fprintf('%1.4f ',Xbeta,XbetaT);
fprintf('\n');