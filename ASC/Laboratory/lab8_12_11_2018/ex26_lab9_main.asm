bits 32
global start

extern exit, printf, fread, fopen, fclose
import exit msvcrt.dll
import printf msvcrt.dll
import fread msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll

%include "ex26_lab9_module.asm"

segment data use32 class=data:

;Read from file numbers.txt a string of numbers (odd and even). Build two strings using readen numbers:
;P – only with even numbers
;N – only with odd numbers
;Display the strings on the screen.

    file db 'input_ex26_lab9.txt', 0
    modread db 'r', 0
    handle dd -1
    space equ ' '
    evenValues times 20 dd 0
    oddValues times 20 dd 0
    printFormat db ' %d', 0
    currentNumber dd 0
    lastEvenPosition dd 0
    lastOddPosition dd 0
    endl db '', 10,13,0
    value db 0

segment code use32 class=code:
    start:
    ; opend the file in read mode
        push dword modread
        push dword file
        call [fopen]
        add esp, 4*2
        
        mov [handle], eax; handle1 = handle for file in read mode
        cmp eax, 0; checks if there was an error while opening the file
        je error; jumps to end of code if there was an error while opening the file
        
        ; reads the contents from the input file and stores them in the value variable
        push dword [handle]
        push dword 100
        push dword 1
        push dword value
        call [fread]
        add esp, 4*4
        cmp eax, 0; checks if there was an error while reading the file
        je error; jumps to end of code if there was an error while reading from the file
        
        ; closes the input file
        push dword [handle]
        call [fclose]
        add esp, 4*1
        
        ; goes through every character that was read from the input file
        mov esi, 0
        findNumbers:
            mov al, byte [value+esi]
            cbw
            cwde
            push eax
            cmp al, 0; checks if we've reached the end of the input
            je spaceCase; evaluates the last number from the input
            cmp al, space; checks if we've reached a space character (a.k.a. we found a new number)
            je spaceCase; evaluates the newly found number
            
            push dword [currentNumber]
            push eax
            call formNumber
            add esp, 4*2
            mov dword [currentNumber], edx
            
            continue:
            inc esi; advances to the next character
            pop eax
            cmp al, 0; checks if we've reached end of input
            je endc; jumps to end of code if we've reached end of input
        jmp findNumbers
        
        jmp endc
        
        spaceCase:
            mov ebx, [currentNumber]
            and ebx, 00000001h
            jz addEven
            jnz addOdd
        
        addEven:
            mov edi, [lastEvenPosition]
            mov ebx, [currentNumber]
            mov dword [evenValues+edi*4], ebx
            inc dword [lastEvenPosition]
            mov dword [currentNumber], 0
        jmp continue
        
        addOdd:
            mov edi, [lastOddPosition]
            mov ebx, [currentNumber]
            mov dword [oddValues+edi*4], ebx
            inc dword [lastOddPosition]
            mov dword [currentNumber], 0
        jmp continue
        
        ; closes the input file in case of an I/O error
        error:
            push dword [handle]
            call [fclose]
            add esp, 4*1
        jmp endprog
        
        endc:
        mov esi, 0
        mov ecx, [lastEvenPosition]
        printEvens:
            push ecx
            push dword [evenValues+esi*4]
            push dword printFormat
            call [printf]
            add esp, 4*2
            pop ecx
            inc esi
        loop printEvens
        
        push dword endl
        call [printf]
        add esp, 4*1
        
        mov esi, 0
        mov ecx, [lastOddPosition]
        printOdds:
            push ecx
            push dword [oddValues+esi*4]
            push dword printFormat
            call [printf]
            add esp, 4*2
            pop ecx
            inc esi
        loop printOdds
        endprog:
        push dword 0
        call [exit]