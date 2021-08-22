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
    a db 1
    b db 1
    c db 1
    d db 1
    f dw 1
    g dw 1
    h dw 1
; our code starts here
segment code use32 class=code
;h/a + (2 + b) + f/d – g/c
    start:
        ; ...
        mov ax, [h]
        mov bl, [a]
        mov bh, 0
        div bx
        add al, 2
        add al, [b]
        mov cl, al
        mov ax, [f]
        mov bl, [d]
        mov bh, 0
        div bx
        add cl, al
        mov ax, [g]
        mov bl, [c]
        mov bh, 0
        div bx
        sub cl, al
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
