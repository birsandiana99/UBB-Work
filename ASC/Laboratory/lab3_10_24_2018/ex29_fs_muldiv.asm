bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; (a+b)/(c-2)-d+2-x; a,b,c-byte; d-doubleword; x-qword
    a db 5
    b db 5
    c db 5
    d dd 5
    x dq 5
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov al, [a]
        add al, [b]; al = a+b
        mov bl, [c]
        sub bl, 2; bl = c-2
        mov ah, 0; ax = a+b
        div bl
        mov bl, al; bl = (a+b)/(c-2)
        mov edx, 0
        mov dl, bl
        sub edx, [d]; edx = (a+b)/(c-2) - d
        add edx, 2; edx = (a+b)/(c-2) - d + 2
        mov eax, 0
        mov ebx, dword [x+4]
        mov ecx, dword [x]
        sub edx, ecx
        sbb eax, ebx; edx:eax = (a+b)/(c+2) - d + 2 - x
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
