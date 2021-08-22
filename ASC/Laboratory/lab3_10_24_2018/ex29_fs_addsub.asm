bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; d+c-b+(a-c) = d+c-b+a-c = d-b+a = d-(b-a)
    a db 5
    b dw 6
    c dd 7
    d dq 8
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ax, [b]
        mov bl, [a]
        mov bh, 0 ; bl = a
        sub ax, bx ; ax = b - a
        mov bx, ax
        mov edx, 0
        mov dx, bx ; eax = b - a
        mov eax, 0 ; edx:eax = b - a
        mov ecx, dword [d]
        mov ebx, dword [d+4] ; ecx:ebx = d
        sub ecx, edx
        sbb ebx, eax ; ecx:ebx = d - (b - a)
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program - 20
