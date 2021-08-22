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

;A byte string S is given. Build the string D whose elements represent the sum of each two consecutive bytes of S.

segment data use32 class=data
    s db 1,4,5,9
    len equ $-s
    lend equ len-2
    d times len-1 db 0
    cifra dd 0
    format db "%d ",0
segment code use32 class=code

start:
    mov esi,s
    mov edi,d
    mov ecx,len
    mov eax,0
    lodsb ;al - primul element
    loop_sir:
        push ecx
        mov bl,al ;bl primul elem
        lodsb ;al - al doilea element
        add bl,al ;bl are suma
        mov cl,al
        mov al,bl
        stosb
        mov al,cl
        pop ecx
        
        loop loop_sir
    
    mov ecx,0
    loop_afisare:
        cmp ecx,lend
        jg afara1
        mov al,[d+ecx]
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