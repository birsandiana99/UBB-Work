bits 32
global start

extern exit, fopen, fclose, fread, printf
import exit msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import fread msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data
    inputFile db 'r1.txt', 0
    modRead db 'r', 0
    printFormat db '%c', 0
    alphabet db "ABCDEFGHIJKLMNOPRSTUVWXYZ", 0
    text times 100 db 0
    space equ ' '
    handle dd -1
segment code use32 class=code
    start:
        ; opens the file in read mode
        push dword modRead
        push dword inputFile
        call [fopen]
        add esp, 4*2
        mov [handle], eax
        cmp eax, 0; checks if there was an error while opening the file
        je endc; jumps to end of code if an error occured
        
        ; reads the contents of the file
        push dword [handle]
        push dword 100
        push dword 1
        push dword text
        call [fread]
        add esp, 4*4
        
        mov esi, 0; we start from the first character in the input
        decode:
            mov al, byte [text + esi]; al = current character
            ; check if al is a char or not
            mov edi, 0; we start from the first leter of the alphabet
            checkIfChar:
                mov bl, [alphabet+edi]; bl = current leter in the alphabet
                cmp bl, 0; checks if the end of the alphabet was reached
                je notChar; jumps to notChar section if so
                cmp al, bl; checks if al is a upper-case letter
                je char; jumps to char section if so
                add bl, 32; makes bl lower-case
                cmp al, bl; checks if al is a lower-case letter
                je char; jumps to char section if so
                inc edi; advances to the next character in the alphabet
            jmp checkIfChar
            
            notChar:
            cmp al, 0
            je endc; jumps to end of code if the end of the input was reached
            jmp printChar; jumps to character print section
            
            char:
            ; compares current caharacter to "A"
            cmp al, 65
            jne cmp_B; jumps to next comparison if the character is different
            mov al, 91
            jmp translate; jumps to character translation
            
            ; compares current character to "B"
            cmp_B:
            cmp al, 66
            jne cmp_a; jumps to next comparison if the character is different
            mov al, 92
            jmp translate; jumps to character translation
            
            ; compares current character to "a"
            cmp_a:
            cmp al, 97
            jne cmp_b; jumps to next comparison if the character is different
            mov al, 123
            jmp translate; jumps to character translation
            
            ; compares current character to "b"
            cmp_b:
            cmp al, 98
            jne translate; jumps to character translation if the character is different
            mov al, 124
            
            translate:; translates the current character
            sub al, 2
            ; prints out the current translated character
            printChar:
            cbw
            cwde
            push eax
            push printFormat
            call [printf]
            add esp, 4*2
            inc esi; advances to the next character
        jmp decode
        
        endc:
        ; closes the file
        push dword [handle]
        call [fclose]
        ; exits the program
        add esp, 4*1
        push dword 0
        call [exit]
