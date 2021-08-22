function L = adquad(a,b,err,f)
  L1 = repeatedSimpsonimsonVectorized(a,b,1,f);
  L2 = repeatedSimpsonimsonVectorized(a,(a+b)/2,1,f)+ repeatedSimpsonimsonVectorized((a+b)/2,b,1,f);
  if abs(L1-L2)<15*err
    L = L2;
   else
    L = adquad(a, (a+b)/2, err/2, f) + adquad((a+b)/2, b, err/2, f);
   endif
 endfunction