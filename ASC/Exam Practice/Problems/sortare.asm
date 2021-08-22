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
    s db 1,5,3,19,2,40
    len equ $-s-1
    len1 equ len+1
    
    format db "%d ",0
    cifra dd 0

segment code use32 class=code
start:
    
    ;for 1 1->n-1 ->>EDI
    ;for j i+1->n ->>ESI
    
    mov edi,0
    for_i: 
        mov esi,edi
        inc esi
        
        for_j:            
            mov al,[s+edi] ; s[i]
            mov bl,[s+esi] ; s[j]
            cmp al,bl 
            jg interschimba; s[i] > s[j]
            
            jmp skip
            
            interschimba:
                mov cl,[s+edi]
                mov [s+edi],bl
                mov [s+esi],cl
            skip:
                inc esi
                cmp esi,len
                jbe for_j
                
        inc edi
        cmp edi,len 
        jb for_i
        
        
    afara:
    mov ecx,0
    loop_afisare:
        cmp ecx,len
        jg afara1
        mov al,[s+ecx]
        cbw
        cwde
        push ecx
        mov [cifra],eax
        push dword [cifra]
        push dword format
        call [printf]
        add esp,8
        pop ecx
        inc ecx
        jmp loop_afisare
               
            
    
    afara1:
    
    
    push dword 0
    call [exit]