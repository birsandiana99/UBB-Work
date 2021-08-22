bits 32
global start

extern exit, fopen, fclose, fread, printf, fprintf
import exit msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import fread msvcrt.dll
import fprintf msvcrt.dll
import printf msvcrt.dll

segment data use32 class = data:

;A text file is given. The text file contains numbers (in base 10) separated by spaces. Read the content of the 
;file, determine the minimum number (from the numbers that have been read) and write the result at the end of file.

    file db 'input_ex27.txt', 0
    modread db 'r', 0
    modwrite db "a", 0
    min dd 147483647
    handle1 dd -1
    space equ ' '
    currentNumber dd 0
    printFormat db '%d', 0
    appendFormat db " %d", 0
    value db 0
    appendString times 10 db 0

segment code use32 class=code:
    start:
        ; opend the file in read mode
        push dword modread
        push dword file
        call [fopen]
        add esp, 4*2
        
        mov [handle1], eax; handle1 = handle for file in read mode
        cmp eax, 0; checks if there was an error while opening the file
        je error; jumps to end of code if there was an error while opening the file
        
        ; reads the contents from the input file and stores them in the value variable
        push dword [handle1]
        push dword 100
        push dword 1
        push dword value
        call [fread]
        add esp, 4*4
        cmp eax, 0; checks if there was an error while reading the file
        je error; jumps to end of code if there was an error while reading from the file
        
        ; closes the input file
        push dword [handle1]
        call [fclose]
        add esp, 4*1
        
        ; goes through every character that was read from the input file
        mov esi, 0
        findNumbers:
            mov al, byte [value+esi]
            push eax
            cmp al, 0; checks if we've reached the end of the input
            je spaceCase; evaluates the last number from the input
            cmp al, space; checks if we've reached a space character (a.k.a. we found a new number)
            je spaceCase; evaluates the newly found number
            
            ; builds the current number
            mov ebx, [currentNumber]
            jmp mul10; the unit digit becomes the decimal digit, decimal -> hundreds, ...
            ; add the current digit to the number that is being built
            addNextDigit:
            mov dword [currentNumber], ebx
            sub al, 48
            cbw
            cwde
            add [currentNumber], eax
            
            continue:
            inc esi; advances to the next character
            pop eax
            cmp al, 0; checks if we've reached end of input
            je endc; jumps to end of code if we've reached end of input
        jmp findNumbers
        
        jmp endc
        
        ; multiplies a number by 10 without doubleing it's size
        mul10:
            mov ecx, 9
            do:
                add ebx, [currentNumber]
            loop do
        jmp addNextDigit; jumps back to where it was called
        
        ; compares the current minimum and the newly found number, updating each as it is needed
        spaceCase:
            mov edx, [currentNumber]
            cmp [min], edx; compares the newly found number to the current minimum
            ja setMinimum; updates minimum if the new number is lower that the current minimum
            continueSpaceCase:
            mov dword [currentNumber], 0; resets the current number to 0, preparing it for the building of the next number
        jmp continue
        
        ; closes the input file in case of an I/O error
        error:
            push dword [handle1]
            call [fclose]
            add esp, 4*1
        jmp endprog
        
        ; updates the minimum variable
        setMinimum:
            mov [min], edx
        jmp continueSpaceCase
        
        endc:
        ; prints the lowest value from the input to the console
            push dword [min]
            push dword printFormat
            call [printf]
            add esp, 4*2
         
        
        ; opens the input file in append mode
            push modwrite
            push file
            call [fopen]
            add esp, 4*2
            
            mov [handle1], eax
            cmp eax, 0; checks if there was an error while opening the file
            je error; jumps to end of code if there was an error while opening the file
            
            appendToFile:
            mov byte [appendString+esi], 0
            ; appends to the end of the input file it's lowest value
            push dword [min]
            push dword appendFormat
            push dword [handle1]
            call [fprintf]
            add esp, 4*3
            
            ; closes the file
            push dword [handle1]
            call [fclose]
            add esp, 4*1
            
            endprog:
            
            push dword 0
            call [exit]