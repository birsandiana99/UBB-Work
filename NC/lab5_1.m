nodes=[0 3 5 8 13];
values=[0 225 383 623 993];
der_values=[75 77 80 74 72];

[H, DH] = hermite_form(nodes,values,der_values,5)


#plot picture of H wrt time and DH wrt time
#plot speed wrt distance