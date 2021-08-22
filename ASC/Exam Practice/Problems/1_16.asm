bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit , scanf, printf              ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import scanf msvcrt.dll
import printf msvcrt.dll

;Read two numbers a and b (in base 10) from the keyboard. Calculate and print their arithmetic average in base 16
; Am facut media in baza 10 , ca sa afisez cu ,5 daca e cazul

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a dd 0xff
    b dd 0xff
    quotient dd 0
    remainder dd 0
    x dd 2
    format1 db "first number: ",0
    format2 db "second number: ",0
    format_citire db "%d",0
    format_afisare1 db "media aritmetica %d",0
    format_afisare2 db "media aritmetica %d,5",0
    
    

; our code starts here
segment code use32 class=code
    start:
        ; ...
        push dword format1
        call [printf]
        add esp,4
        
        push dword a
        push dword format_citire
        call [scanf]
        add esp, 4*2
        
        push dword format2
        call [printf]
        add esp,4
        
        push dword b
        push dword format_citire
        call [scanf]
        add esp, 4*2
        
        mov eax, [a]
        add eax, [b]
        cdq          ; edx:eax <- eax
        div dword [x] ; eax <- catul
                     ; edx <- restul
        mov [quotient],eax
        mov [remainder], edx
        
        cmp edx, 1h
        je afis2
        
        push dword [quotient]
        push dword format_afisare1
        call [printf]
        add esp, 4*2
        jmp final
        
        afis2:
            push dword [quotient]
            push dword format_afisare2
            call [printf]
            add esp, 4*2
    
    final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
