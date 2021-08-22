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
;Read one byte and one word from the keyboard. Print on the screen "YES" if the bits of the byte read are found consecutively among the bits of the ;word and "NO" otherwise.
;Example: a = 10 = 0000 1010b
;b = 256 = 0000 0001 0000 0000b
;The value printed on the screen will be NO.
;a = 0Ah = 0000 1010b
;b = 6151h = 0110 0001 0101 0001b
;The value printed on the screen will be YES (you can find the bits on positions 5-12). 
    msg db "introduceti nr: ",0
    a dd 0
    b dd 0
    
    format db "%d",0
    format_yes db "Yes",0
    format_no db "No",0
segment code use32 class=code
   
start:
    push dword msg
    call [printf] 
    add esp,4
    
    push dword a 
    push dword format
    call [scanf]
    add esp,4*2
    
    
    push dword msg
    call [printf] 
    add esp,4
    
    push dword b
    push dword format
    call [scanf]
    add esp,4*2
    
    
    mov ax,[b]
    mov ecx,16
    loop_b:
        cmp al, byte[a]
        je yes
        shr ax,1 
        
        loop loop_b
        
   no: 
        push dword format_no
        call [printf]
        add esp,4
        jmp final
        
        
   yes:
        push dword format_yes
        call [printf]
        add esp,4
    final:
    
    
    push dword 0
    call [exit]