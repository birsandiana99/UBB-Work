
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

;A file name and a text (defined in the data segment) are given. 
;The text contains lowercase letters, uppercase letters, digits and special characters. 
;Transform all the lowercase letters from the given text in uppercase. 
;Create a file with the given name and write the generated text to file.
                          
segment data use32 class=data
    text db "Ana, $are MeRe?",0
    len equ $-text
    fileName db "ex13.txt",0
    filedescriptor dd -1
    access db "w",0
    text2 db 0
segment code use32 class=code

start:
    push dword access
    push dword fileName
    call [fopen]
    add esp,8
    
    mov [filedescriptor],eax 
    cmp eax,0 
    je final
    
    mov esi, text
    mov edi,text2
    mov ecx, len
    cld
    
    loop_sir:
        lodsb
        cmp al,'a'
        jb adauga
        
        cmp al,'z'
        ja adauga
        
        
        
        schimba:
            mov bl, 'a'-'A'
            sub al,bl
            
        adauga:
            stosb
            loop loop_sir
    
    push dword text2
    push dword [filedescriptor]
    call [fprintf]
    add esp,4*2
    
    push dword [filedescriptor]
    call [fclose]
    add esp,4
    
    final:
    push dword 0
    call [exit]