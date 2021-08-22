a=0;b=4;
f=@(x) sin(2*x)+cos(x)+3;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
n=6; h=(b-a)/n; ai=a; bi=ai+h;
nodes=(ai+bi)/2;color='r';%Rectangle
%nodes=[ai,bi];color='g';%Trapezium
%nodes=[ai,(ai+bi)/2,bi];color='m';%Simpson
%nodes=[ai,ai+h/3,ai+2*h/3,bi];color='y';
%nodes=[ai,ai+h/4,ai+2*h/4,ai+3*h/4,bi];color='c';
%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clf; hold  on; grid  on; set(gca,'FontSize',15);
x=linspace(a,b,1001);
ylim([0 ceil(max(f(x)))]);xlim([a,b]);
plot(x,f(x),'b','LineWidth',8);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
fill([x b a],[f(x) 0 0],'b','FaceAlpha',0.25);
title(['True area \approx ' num2str(quad(f,a,b),'%.3f')...
'                                                      ']);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
area=0;
for k=1:n
    waitforbuttonpress;
    L=@(X) LagrangeBary(nodes,f(nodes),X);
    area+=quad(L,ai,bi);
    x=linspace(ai,bi,201);
    plot(nodes,f(nodes),'ok','Markersize',10,'MarkerFaceColor',color);
    waitforbuttonpress;
    plot(x,L(x),color,'LineWidth',8);
    waitforbuttonpress;
    plot(x,L(x),color,'LineWidth',8);
    fill([x bi ai],[L(x) 0 0],color,'FaceAlpha',0.3);
    plot(nodes,f(nodes),'ok','Markersize',10,'MarkerFaceColor',color);
    title(['True area \approx ' num2str(quad(f,a,b),'%.3f')...
    sprintf('\t\t\t') 'Approximated area \approx ' num2str(area,'%.3f')]);
    ai=bi; bi=bi+h; nodes+=h;
endfor