;Two character strings S1 and S2 are given. Obtain the string D by concatenating
;the elements found on the positions multiple of 3 from S1 and the elements of S2
;in reverse order.
;Example:

;S1: '+', '4', '2', 'a', '8', '4', 'X', '5'
;S2: 'a', '4', '5'
;D: '+', 'a', 'X', '5', '4', 'a'

bits 32 ;assembling for the 32 bits architecture
global start

; we ask the assembler to give global visibility to the symbol called start 
;(the start label will be the entry point in the program) 
extern exit ; we inform the assembler that the exit symbol is foreign; it exists even if we won't be defining it
import exit msvcrt.dll  ; we specify the external library that defines the symbol
        ; msvcrt.dll contains exit, printf and all the other important C-runtime functions

; our variables are declared here (the segment is called data) 
segment data use32 class=data
; 
    s1 db '+', '4', '2', 'a', '8', '4', 'X', '5','Y','Y';declare S1
    l1 equ ($-s1)/3+1;declare length S1
    s2 db 'a', '4', '5';declare S2
    l2 equ $-s2;declare length S2
    d times l1+l2 db 0;declare d of length l1+l2
    
; the program code will be part of a segment called code
segment code use32 class=code
start:

    ;first part of the string d
    MOV ECX,l1;move first length in ECX
    MOV ESI,0;move 0 in ESI
    
    JECXZ End;jump to End if ECX is 0
    
    Repeat1:
        MOV AL,[s1+(ESI*3)];move the elements on positions multiple of 3 to AL
        MOV [d+ESI],AL;move from AL to the string d
        INC ESI;increment ESI
    LOOP Repeat1;repeat,ECX-1
    
    ;second part of the string d
    MOV ECX,l2;move second length in ECX
    MOV ESI,0;move 0 in ESI
    
    JECXZ End;jump to End if ECX is 0
    
    Repeat2:
        MOV AL,[s2+ECX-1];move the elements on the reverse positions to AL
        MOV [d+l1+ESI],AL;move from AL to the end of the string d
        INC ESI;increment ESI
    LOOP Repeat2;repeat,ECX-1
    
    End:
    
    ; call exit(0) ), 0 represents status code: SUCCESS
    push dword 0 ; saves on stack the parameter of the function exit
    call [exit] ; function exit is called in order to end the execution of the program
	

