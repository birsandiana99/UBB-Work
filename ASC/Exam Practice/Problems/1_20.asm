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
;Read two doublewords a and b in base 16 from the keyboard. Display the sum of the low parts of the two numbers and the difference between the high 
;parts of the two numbers in base 16 Example:
;a = 00101A35h
;b = 00023219h
;sum = 4C4Eh
;difference = Eh    

segment data use32 class=data
    a dd 00101A35h
    b dd 00023219h
    s dd 0 
    d dd 0
    format db "%x",0
    format_afisare db "Suma: %x ; diferenta: %x",0
    
segment code use32 class=code

start:
    mov eax,[a] ; high in dx, low in ax    
    mov ebx,[b]
    mov [s],ax
    add [s],bx
    
    shr eax,16
    shr ebx,16
    
    mov [d],ax
    sub [d],bx
    
    push dword [d]
    push dword [s]
    push dword format_afisare
    call [printf]
    add esp, 4*3
    
    push dword 0
    call [exit]