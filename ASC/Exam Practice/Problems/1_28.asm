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

;Read numbers (in base 10) in a loop until the digit '0' is read from the keyboard. 
;Determine and display the biggest number from those that have been read.

segment data use32 class=data
    format_read db "%d",0
    x dd 0
    ct dd 0
    msg db "Introdu:",0
    
segment code use32 class=code
start:
    mov ebx,0
    loop_citire:
        push dword msg
        call [printf]
        add esp,4
        
        push dword x
        push dword format_read
        call [scanf]
        add esp,4*2
        
        mov eax,[x]
        cmp eax,0
        je afara
        
        inc byte [ct]
        jmp loop_citire
        
        
    
    afara:
    push dword [ct]
    push dword format_read
    call [printf]
    add esp,8
    
    
    push dword 0
    call [exit]