bits 32
global start

extern exit, printf
import exit msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data
;A byte string S is given. Build the string D whose elements represent the sum of each two consecutive bytes of S. 
    array1 db 1, 2, 3, 4, 5, 6
    l1 equ $-array1
    a db 0
    array2 times l1-1 db 0
    msg db '%d '

segment code use32 class=code
    start:
        mov ecx, l1; ecx = lenght of array1
        mov edx, 0; edx = current legth of array2
        dec ecx; account for initialization of al with the first element of array1
        mov al, [array1+0]; al = first element of array1
        mov esi, 1; esi = 1 because al = first element of array1
        mov edi, array2
        jecxz endc
        findNewArray:
            add al, [array1+esi];al = array1[i-2] + array1[i-1] + array1[i]
            sub al, [a]; bl = bl - array1[i-2]
            mov bl, [array1+esi-1]; al = array1[i-1]
            mov [a], bl; a = array1[i-1]
            stosb; append al to array2
            inc edx; extend length of array2 by 1
            inc esi; advance to next element of array1
        loop findNewArray
        endc:
        ; code for printing the elements of array2
        mov ecx, edx; ecx = length of array2
        mov esi, 0; we start at first element of array2
        showNewArray:
            mov al, [array2+esi]; al = array2[esi]
            cbw; ax = al
            cwde; eax = ax
            push ecx
            push eax
            push dword msg
            call [printf]
            add esp, 4*2
            pop ecx
            inc esi; advance to the next element of array2
        loop showNewArray
        push    dword 0
        call    [exit]