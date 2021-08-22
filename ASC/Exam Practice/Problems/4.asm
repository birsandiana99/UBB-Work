
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

;A text file is given. 
;Read the content of the file, count the number of odd digits and display the result on the screen. 
;The name of text file is defined in the data segment.
segment data use32 class=data
    digits db "13579",0
    len equ $-digits

    file_name db "ex4.txt",0
    mod_acces db "r",0
    file_descriptor dd -1
    
    format_s db "%s",0
    
    litera db 0
  
    ct dd 0
    format db "There are %d odd digits",0
    text times 101 db 0
    
    
segment code use32 class=code

start:
    push dword mod_acces
    push dword file_name
    
    call [fopen]
    add esp,8
    
    mov [file_descriptor],eax
    cmp eax,0
    je final
    
    push dword [file_descriptor]
    push dword 100
    push dword 1
    push dword text
    call [fread]
    add esp,4*4
    
    
    ;push dword text
    ;push dword format_s
    ;call [printf]
    ;add esp,8
    
    cld
    mov esi,text
    mov ecx,eax 
    
    loop_text:
        lodsb ;al este un byte
        mov [litera],al
        pushad
        
        mov esi,digits
        mov ecx,len
        loop_digits:
            lodsb
            cmp al,[litera]
            je contorizare
            loop loop_digits
                
       jmp sari
       contorizare:
       inc dword [ct]
       sari:      
       popad
       loop loop_text
       
     
     push dword [ct]
     push dword format
     call [printf]
     add esp,4*2
      
    
    push dword [file_descriptor]
    call [fclose]
    add esp,4
    
    final:
    push dword 0
    call [exit]