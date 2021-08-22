%ifndef _FORMNUMBER_ASM_
%define _FORMNUMBER_ASM_

formNumber:
    ; builds the current number
    mov eax, [esp+4]; reads the current character from the stack
    mov ebx, [esp+8]; reads the number that is being formed from the stack
    mov dword edx, ebx
    jmp mul10; the unit digit becomes the decimal digit, decimal -> hundreds, ...
    ; add the current digit to the number that is being built
    addNextDigit:
    sub eax, 48
    add edx, eax
    
    ret
    
    ; multiplies a number by 10 without doubleing it's size
    mul10:
        mov ecx, 9
        do:
            add edx, ebx
        loop do
    jmp addNextDigit; jumps back to where it was called

%endif