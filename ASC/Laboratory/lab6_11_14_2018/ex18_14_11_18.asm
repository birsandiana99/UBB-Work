bits 32
global start

extern exit, printf
import exit msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data
; A string of doublewords is given. Order in increasing order the string of the high words (most significant) from these doublewords. The low words (least significant) remain unchanged.
    numbers dd 1256ABCDh, 12AB5678h, 12344344h, 11239080h
    len equ $-numbers
    highParts times len dd 0
    newNumbers times len dd 0
    highest dd 0
    lowest dd 0
    msg db '%d '
segment code use32 class=code
    start:
        jmp main
        ;reverses the values of eax and edx
        reverseNumbers:
            mov [highest], eax
            mov [lowest], edx
            mov eax, [lowest]
            mov edx, [highest]
            mov ebx, edi
        jmp continueSorting; jumps back where it was called during the sorting
        
        main:
        mov ecx, len; ecx = length of array numbers (number of bytes of the array)
        mov esi, 0; starting from first element of array numbers
        mov edi, highParts; we set highParts as the destination array
        jecxz endc; jumps to end of code if the numbers array has no elements
        
        ; here we isolate the high parts oh the elements of the numbers array
        findHighParts:
            ; we set the low part of the current element of the highParts array to 0
            mov al, 0
            stosb
            stosb
            add esi, 2; adjusts the offset for the numbers array
            push ecx; we save the value of ecx before modifying it so that the current loop will continue as intended
            mov ecx, 2
            ; we set the high part of the current element of the highParts array to the highPart of the respective element in the numbers array
            getFromNumbers:
                mov al, [numbers+esi]
                stosb
                inc esi
            loop getFromNumbers
            pop ecx; we reset the value of ecx to what it was before the modification
        loop findHighParts
        
        mov esi, 0; starting from the first element from the highParts array
        mov ecx, len/4 - 1; we set ecx to the lenth of the highParts array -1
        sortHighParts:
            push ecx; we save the value of ecx before modifying it so that the current loop will continue as intended
            ; we determine the offset of the element from the 
            mov edi, 0
            mov ecx, esi
            jecxz afterNextAddress
            findNextAddress:
                add edi, 4
                sub ecx, 3
            loop findNextAddress
            afterNextAddress:
            add edi, 4
            pop ecx; we reset the value of ecx to what it was before the modification
            mov eax, [highParts+esi]; eax = current element from the highParts array
            push ecx; we save the value of ecx before modifying it so that the current loop will continue as intended
            sortNewNumbers:
                mov edx, [highParts+edi]; edx = current element of the highParts array + offset edi
                cmp eax, edx; compares eax to edx
                ja reverseNumbers; jumos to reverseNumbers if eax > edx
                continueSorting:
                mov dword [highParts+esi], eax; current element of highParts = lowest between eax and edx
                mov dword [highParts+edi], edx; current element of highParts = highest between eax and edx
                add edi, 4; advance to next element of highParts
            loop sortNewNumbers
            pop ecx; we reset the value of ecx to what it was before the modification
            add esi, 4; advance to next element of highParts
        loop sortHighParts
        jmp completeWithLowParts; jumps to the completeWithLowParts section
        
        ; prints out the elements of highParts and exits the program
        endc:
        mov ecx, len/4
        mov esi, 0
        showNewNumbers:
            mov eax, [highParts+esi]
            push ecx
            push eax
            push dword msg
            call [printf]
            add esp, 4*2
            pop ecx
            add esi, 4
        loop showNewNumbers
        push    dword 0
        call    [exit]
        
        ;completes the low parts of the elements from highParts with the low parts of the respective elements from numbers
        completeWithLowParts:
        mov ecx, len; ecx = length of numbers array (number of bytes in array)
        mov esi, 0; starting from the first byte of numbers
        mov edi, 0; starting from the first byte of highParts
        findLowParts:
            push ecx; we save the value of ecx before modifying it so that the current loop will continue as intended
            mov ecx, 2
            ; we set the low part of the current element of highParts to the low part of the respective element from numbers
            searchInNumbers:
                mov al, [numbers+esi]
                mov [highParts+edi], al
                inc edi
                inc esi
            loop searchInNumbers
            pop ecx; we reset the value of ecx to what it was before the modification
            add esi, 2; we skip the high part of the current element from numbers
            add edi, 2; we skip the high part of the current element from highParts
        loop findLowParts
        jmp endc; jumps to end of code