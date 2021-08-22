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
;Read the content of the file, determine the digit with the highest frequency and display the digit along with its frequency on the screen. 
;The name of text file is defined in the data segment.
segment data use32 class=data
    filename db "ex66.txt",0
    file_descriptor dd -1
    mod_acces db "r",0
    
    c db 0
    digits db "0123456789",0
    
    
    maxim dd 0
    
    format_afisare db "The most frequent digit is: %c ,with a frequency of %d",0
    
    len dd 0
    
    text times 101 dd 0
    
    digit db 0
    
    format db "%d",0
   
    
segment code use32 class=code
start:
    push dword mod_acces
    push dword filename
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
    
    mov dword [len],eax
    
    
    
    
    mov esi,digits
    mov ecx,10 ; in eax will be the length of the text
    cld
    
    loop_digits:
        lodsb ;al-cifra curenta
        mov byte[c],al
        pushad
        mov ebx,0 ;cu ebx vom contoriza aparitia unei cifre in text
        mov esi,text
        mov ecx,[len] ;there are 10 digits
        
        loop_text:
            lodsb
            cmp byte[c],al
            je e_cifra_c
            jmp sari
            
            e_cifra_c:
                inc ebx
            sari:
                loop loop_text
            
       cmp ebx, dword[maxim]
       ja aici
       
       jmp sari2
       
       
             
       aici:
            mov dword[maxim],ebx
            mov byte [digit],al
            
      sari2:
            popad
            loop loop_digits
            
                
        
      
      push dword [maxim]
      push dword [digit]
      push dword format_afisare
      call [printf]
      add esp, 8
        
        
    
    
      push dword [file_descriptor]
      call [fclose]
      add esp,4
    
    
    
    final:
    push dword 0
    call [exit]