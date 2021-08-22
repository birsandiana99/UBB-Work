function L = adquad(a,b,err,f)
  L1 = simpson(f,a,b);
  L2 = simpson(f,a,(a+b)/2) + simpson(f,(a+b)/2,b);
  if(abs(L1-L2)<15*err
    L = L2;
   else
    L = adquad(a, (a+b)/2, err/2, f) + adquad((a+b)/2, b, err/2, f);
   endif
 endfunction