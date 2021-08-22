bits 32
global start

extern exit, printf, scanf
import exit msvcrt.dll
import printf msvcrt.dll
import scanf msvcrt.dll

segment data use32 class=data:

;A character string is given (defined in the data segment). Read one character from the keyboard, then count the 
;number of occurences of that character in the given string and display the character along with its number of 
;occurences.
    
	charArray db 'a','b','c','d','a','f','e','a','d','e'; the array of characters
    len equ $-charArray; length of charArray
    readChar db "Please enter a character ", 0; Message to be printed out before reading a character
    readFormat db "%c", 0; necessary for reading a character via scanf
    printFormat db "the character %c appears %d times in the defined array", 10, 13, 0; message to be printed out with the read character and the number of times it is found in charArray
    charToFind db 0; the character to find in charArray
   
segment code use32 class=code:
    start:
        ; prints the message that notifies the necessity of inputting a character
        push dword readChar
        call [printf]
        add esp, 4*1
        ; reads the requested character
        push charToFind
        push dword readFormat
        call [scanf]
        add esp, 4*2
        
        mov esi, 0; starting offset for charArray
        mov ebx, 0; counts the number of occurences of the read character in charArray
        mov ecx, len; ecx = length of charArray
        jecxz endc; jumps to the end of the program if charArray is empty
        findOccureneces:
            mov al, [charArray+esi]; al = current element from charArray
            cmp al, [charToFind]; compares the inputted character and the current character
            je incrementOccucrences; jumps to incrementOccucrences if the 2 are equal
            contiune:; tag to be jumped to if the number of occurences was incremented
            inc esi; advance to the next element of charArray
        loop findOccureneces; repeats findOccureneces until ecx = 0
        jmp endc
        
        incrementOccucrences:
        inc ebx; increments the counter of occurences
        jmp contiune; jumps back to where it was called
        
        endc:
        ; prints out the inpputted character and the number of its occurences
        push dword ebx
        mov al, [charToFind]
        cbw
        cwde
        push dword eax
        push dword printFormat
        call [printf]
        add esp, 4*3
        ; exits the program
        push dword 0
        call [exit]
        