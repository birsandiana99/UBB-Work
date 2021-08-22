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
    a dd 0xff
    b dd 0xff
    s dd 0
    format_10 db "%d",0
    format_16 db "%x",0
    
segment code use32 class=code

start:
    push dword a 
    push dword format_10
    call [scanf]
    add esp,4*2
    
    push dword b
    push dword format_10
    call [scanf]
    add esp,4*2
    
    mov eax, [a]
    add eax, [b]
    mov [s],eax
    
    push dword [s]
    push dword format_16
    call [printf]
    add esp,8
    
    
    push dword 0
    call [exit]