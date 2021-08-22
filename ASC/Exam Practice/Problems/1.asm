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

;1.A text file is given. 
;Read the content of the file, count the number of vowels and display the result on the screen. 
;The name of text file is defined in the data segment.
segment data use32 class=data
    
    
    nume_fis db "ex1.txt",0
    access_mode db "r",0
    descriptor dd -1
    
    counter dd 0
    format db "%d",0
    cuvant db 0
    
    vowels db "aeiouAEIOU",0
    len equ $-vowels
    
segment code use32 class=code

start:
    
    push dword access_mode
    push dword nume_fis
    call [fopen]
    add esp,8
    mov [descriptor],eax
    
    cmp eax,0
    je sfarsit
    
    ;fread(string ptr, integer size, integer n, FILE * handle) - reads n times size bytes from the
    ; file identified by handle and place the read bytes in the string ptr.
    loop_citire:
        push dword [descriptor]
        push dword 1
        push dword 1
        push dword cuvant
        call [fread]
        add esp,4*4
        
        cmp eax,0
        je iesi
        
        ;pushad
        
        
        mov esi, vowels
        mov ecx,len
        
        verificare_vocala:
            lodsb
            cmp al,[cuvant]
            je e_vocala
            
            loop verificare_vocala
            cmp ecx,0
            jle afara
            e_vocala:
                mov ebx,[counter]
                inc ebx
                mov [counter],ebx
                jmp afara
        loop verificare_vocala
        afara:
        jmp loop_citire
            
        ;popad
    
    
    iesi:
        push dword [counter]
        push dword format
        call [printf]
        add esp,8
    
    
    
    push dword [descriptor]
    call [fclose]
    add esp,4
    
    sfarsit
    push dword 0
    call [exit]