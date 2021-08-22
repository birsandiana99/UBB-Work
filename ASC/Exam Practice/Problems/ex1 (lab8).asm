;Se citesc de la tastatura numere (in baza 10) pana cand se introduce cifra 0. Determinaţi şi afişaţi cel mai mare număr dintre cele citite. 

bits 32 ;assembling for the 32 bits architecture
global start

; we ask the assembler to give global visibility to the symbol called start 
;(the start label will be the entry point in the program) 
extern exit, printf, scanf ; adaugam printf si scanf ca functii externa            
import exit msvcrt.dll    
import printf msvcrt.dll    ; indicam asamblorului ca functia printf se gaseste in libraria msvcrt.dll
import scanf msvcrt.dll

; our variables are declared here (the segment is called data) 
segment data use32 class=data
; 
    current dd 0
    max dd 0
    format  db "%d", 0
    message db "Max Number is: %d", 0
    
; the program code will be part of a segment called code
segment code use32 class=code
start:
    LoopZero:
        ;read dword into [current]
        PUSH DWORD current       
        PUSH DWORD format
        CALL [scanf] 
        ADD ESP, 4 * 2
        ;check if the number read is 0
        MOV EBX,[current]
        CMP EBX,0
        JE End
        ;check if the number is less or equal than the [max]
        CMP EBX,[max]
        JLE LoopZero
        ;if it is not, replace [max]
        MOV [max],EBX
    JMP LoopZero
    
    End:
    ;write dword from [max]
    PUSH DWORD [max]
    PUSH DWORD message 
    CALL [printf]
    ADD ESP, 4*2
        
; call exit(0) ), 0 represents status code: SUCCESS
push dword 0 ; saves on stack the parameter of the function exit
call [exit] ; function exit is called in order to end the execution of the program
	

