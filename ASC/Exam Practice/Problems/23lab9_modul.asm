%ifndef _23LAB9_MODUL_ASM_
%define _23LAB9_MODUL_ASM_

cifraSutelor:
    mov eax, [esp + 4] ; eax = numarul de impartit
    
    ; o sa impartim edx:eax la 10 de 3 ori
    mov edx, 0
    
    ; dupa impartire:
    ; eax = cat
    ; edx = rest
    
    mov ebx, 10 ; impartim la 10
    
    div ebx ; prima impartire
    
    mov edx, 0
    div ebx ; a doua impartire
    
    mov edx, 0
    div ebx ; a treia impartire
    
    ; edx contine acum cifra sutelor (0 daca numarul nu are o cifra a sutelor)
    mov eax, edx
    
    ret 4 ; ret urmat de cati bytes am pushat pe stack (in cazul nostru doar 4, adica eax)
%endif
    