bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, scanf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll
import scanf msvcrt.dll

%include "23lab9_modul.asm"

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    sir dd 5892, 456, 33, 7, 245
    len equ ($ - sir)/4
    sir_dest times len dd 0
    
    int_fmt db "%d", 0
    str_fmt db "%s", 0
    
    spatiu db " ", 0

; our code starts here
segment code use32 class=code
    start:        
        mov edi, sir_dest
        mov esi, sir ; esi = sirul initial
        mov ecx, len
        loopSir:
            lodsd
            
            push dword eax ; catre modul
            call cifraSutelor
            stosd
        loop loopSir
        
        mov ecx, len
        mov esi, sir_dest ; sirul rezultat
        
        loopAfisare:
            lodsd
            
            pushad
            push dword eax
            push dword int_fmt
            call [printf]
            add esp, 4 * 2
            
            push dword spatiu
            push dword str_fmt
            call [printf]
            add esp, 4 * 2
            popad
        loop loopAfisare
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
