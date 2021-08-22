bits 32
global start

extern exit, fopen, fprintf, scanf, printf, fclose 
import exit msvcrt.dll
import fopen msvcrt.dll
import fprintf msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll
import fclose msvcrt.dll

segment data use32 class=data
    file db "output.txt", 0
    printFormat db "Pentru %d: b16:%x 1-uri in binar: %d", 10, 13, 0
    input dd 0
    modWrite db "w", 0
    readFormat db "%d", 0
    handle dd -1
    numberOf1s db 0
    msg db "Introduceti numere. introduceti 0 cand doriti sa incheiati programul.", 10, 13, 0

segment code use32 class=code
    start:
        ; opens the file in write mode
        push dword modWrite
        push dword file
        call [fopen]
        add esp, 4*2
        mov [handle], eax
        cmp eax, 0
        je endc
        ; prints msg to the console
        push msg
        call [printf]
        add esp, 4*1
        
        readNumber:
            ; reads a number from the keyboard
            push dword input
            push dword readFormat
            call [scanf]
            add esp, 4*2
            cmp dword [input], 0; checks if the read number = 0
            je endc; ends the program if so
            mov ebx, [input]
            ; finds how many 1s there are in the read number's binary representation
            jmp find1s
            continueReading:
            ; writes the requested data to the file
            push dword [numberOf1s]
            push dword ebx
            push dword ebx
            push dword printFormat
            push dword [handle]
            call [fprintf]
            add esp, 4*5
        jmp readNumber; repeats the process

        ; finds the number of 1s in the read number's binary representation
        find1s:
            mov dword [numberOf1s], 0; there are 0 1s initially
            mov ecx, 32; goes through an entire dword
            find:
                test dword [input], 00000000000000000000000000000001b; checks if last bit is 1
                jz zero; jumps to zero segment if current bit = 0
                inc dword [numberOf1s]; increments numberOf1s otherwise
                zero:
                shr dword [input], 1; advances to the next bit
            loop find; repeats until ecx = 0
            jmp continueReading; returns to where it was called
            
        endc:
            ;closes the file
            push dword [handle]
            call [fclose]
            add esp, 4*1
            ; ends the program
            push    dword 0
            call    [exit]