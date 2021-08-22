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



;Read a decimal number and a hexadecimal number from the keyboard. Display the number of 1's of the sum of the two numbers in decimal format. Example:
;a = 32 = 0010 0000b
;b = 1Ah = 0001 1010b
;32 + 1Ah = 0011 1010b
;The value printed on the screen will be 4  

segment data use32 class=data
    msg db "Introduceti nr: ",0
    a dd 0
    b dd 0
    s dd 0
    format_a db "%d",0
    format_b db "%x",0
    ct dd 0
    
    ;14  8+4+2         000000000000000000000000001110
segment code use32 class=code

start:
    push dword msg
    call [printf]
    add esp,4
    
    push dword a
    push dword format_a
    call [scanf]
    add esp,8
    
    
    push dword msg
    call [printf]
    add esp,4
    
    push dword b
    push dword format_b
    call [scanf]
    add esp,8
    
    mov eax,[a]
    add eax,[b]
    
    
    mov ecx,32
    mov ebx,0
    counter:
         sar eax,1
         jc adauga_ct
         loop counter
         jmp final
         adauga_ct:
            inc ebx
            loop counter
    final:
    mov [ct],ebx
    
    push dword [ct]
    push dword format_a
    call [printf]
    add esp,8
        
    
    
    
    
    
    push dword 0
    call [exit]