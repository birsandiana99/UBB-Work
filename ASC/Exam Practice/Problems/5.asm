  
bits 32 
global start

extern printf,scanf,exit,fprintf,fscanf,fopen,fclose,fread

import fread msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import exit msvcrt.dll
import scanf msvcrt.dll
import fscanf msvcrt.dll
import printf msvcrt.dll
import fprintf msvcrt.dll


segment data use32 class=data
;Two byte strings s1 and s2 are given. Build the byte string d such that, for every byte s2[i] in s2, d[i] contains either the position of byte s2[i] in s1,
;either the value of 0.
;Example:
;pos:1 2 3 4 5
;s1: 7, 33, 55, 19, 46
;s2: 33, 21, 7, 13, 27, 19, 55, 1, 46 
;d: 2,  0, 1, 0, 0, 4, 3, 0, 5  

    s1 db 7, 33, 55, 19, 46
    lens1 equ $-s1
    s2 db 33, 21, 7, 13, 27, 19, 55, 1, 46 
    lens2 equ $-s2
    d times lens2 db 0
    
    lit dd 0
    el db 0
    format db "%i ",0
    
segment code use32 class=code

start:
    ;pt fiecare element din s2 tr sa vad pozitia lui in s1, sau 0 daca nu exista
    
    mov ecx,lens2
    mov esi,s2
    mov edi,d
    cld
    loop_s2:
        lodsb
        mov bl,al
        
        pushad
        
        
        
        mov esi,s1
        mov ecx,lens1
        
        
        loop_s1:
            lodsb 
            cmp al,bl
            je adauga_pozitia
            loop loop_s1
         
        ;cmp ecx,0
        ;jle afara
        
        
        mov eax,0
        stosb
        jmp sari

        adauga_pozitia:
            mov ebx,6
            sub ebx,ecx
            mov eax,ebx
            stosb
        
        sari:
            popad
            add edi,1
            loop loop_s2
            cmp ecx,0
            jle afara
            
     
     
     afara:
     mov ecx,lens2
     mov edi,0
     loop_p:
        cmp ecx,0
        jle final
        mov al,[d+edi]
        cbw
        cwde
        pushad
        mov [lit],eax
        push dword [lit]
        push dword format
        call [printf]
        add esp,4*2
        popad
        inc edi
        
        dec ecx
        jmp loop_p
        
        
        
    final:
        
    
    
       
    
    
    
    
    
    
    
    
    push dword 0
    call [exit]