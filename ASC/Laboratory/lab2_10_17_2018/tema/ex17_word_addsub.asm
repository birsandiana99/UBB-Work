bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a dw 13
    b dw 9
    c dw 3
    d dw 6
; our code starts here
segment code use32 class=code
;a+a-b-c-(d+d)
    start:
        ; ...
        mov ax, [a]
        add ax, [a]
        sub ax, [b]
        sub ax, [c]
        sub ax, [d]
        sub ax, [d]
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
