bits 32
global start        

extern exit
import exit msvcrt.dll

segment data use32 class=data

    a dw 0101010101010101b
    b dw 1010101010101010b
    c dd 0

segment code use32 class=code
    start:
        ; Given the words A and B, compute the doubleword C as follows:
        mov ecx, 0
        
        ;the bits 0-5 of C are the same as the bits 3-8 of A
        mov ax, [a]; AX = A
        and ax, 0000000111111000b; we isolate bits 3-8 of AX
        ror ax, 3; we rotate the bits of AX with 3 positions to the right, so bits 3-8 are now bits 0-5
        add cx, ax; we make the bits 0-5 of CX = bits 0-5 of A
        
        ;the bits 6-8 of C are the same as the bits 2-4 of B
        mov ax, [b]; AX = B
        and ax, 0000000000011100b; we isolate the bits 2-4 of AX
        rol ax, 4; we rotate the bits of AX with 4 positions to the left, so bits 2-4 are now bits 6-8
        add cx, ax; we make bits 6-8 of CX = bits 2-4 of B
        
        ;the bits 9-15 of C are the same as the bits 6-12 of A
        mov ax, [a]; AX = A
        and ax, 0001111111000000b; we isolate bits 6-12 of AX
        rol ax, 3; we rotate the bits of AX with 3 positions to the left, so bits 6-12 are now bits 9-15
        add cx, ax; we make bits 9-15 of CX = bits 6-12 of A
        
        ;the bits 16-31 of C have the value 0
        mov [c], ecx; we form the final version of the doubleword C
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
        
        ; al = 0101b
        ; ah = 0001b
        
        ; and al, ah -> al = al and ah <=> al = 0101 and 0001 <=> al = 0001
