;Se da un nume de fisier (definit in segmentul de date). Sa se creeze un fisier cu numele dat, apoi sa se citeasca 
;de la tastatura cuvinte pana cand se citeste de la tastatura caracterul '$'. Sa se scrie in fisier doar cuvintele 
;care contin cel putin o litera mica (lowercase).

bits 32 ;assembling for the 32 bits architecture
global start

; we ask the assembler to give global visibility to the symbol called start 
;(the start label will be the entry point in the program) 
extern exit, fopen, fprintf, fclose, printf, scanf
import exit msvcrt.dll  
import fopen msvcrt.dll  
import fprintf msvcrt.dll
import fclose msvcrt.dll
import printf msvcrt.dll    
import scanf msvcrt.dll


; our variables are declared here (the segment is called data) 
segment data use32 class=data
; 
    string times 20 db 0
    filename db "whatever.txt",0
    accessmode db "w",0
    format  db "%s", 0
    fileinfo dd -1
    startletter equ 'a'
    endletter equ 'z'
; the program code will be part of a segment called code
segment code use32 class=code
start:
    ;open/create file
    PUSH DWORD accessmode   
    PUSH DWORD filename
    CALL [fopen]
    ADD ESP, 4*2 
    ;save fileinfo
    MOV [fileinfo], EAX
    ;check for errors
    CMP EAX, 0
    JE End
    LoopWords:
        ;read string given into [string]
        PUSH DWORD string       
        PUSH DWORD format
        CALL [scanf] 
        ADD ESP, 4 * 2
        ;check if the first character read is $
        MOV ESI,string
        CMP BYTE [ESI],'$'
        JE End
        ;check if the string has any small characters
        LoopChars:
            CMP BYTE [ESI],0;if the word has ended, it's not good, leave it
            JE LoopWords
            CMP BYTE [ESI],endletter;
            JG LoopCharSkip
            CMP BYTE [ESI],startletter
            JGE ContainsChar
            LoopCharSkip:
            INC ESI
        JMP LoopChars
        ContainsChar:
        ;write the string to the file
        PUSH DWORD string
        PUSH DWORD [fileinfo]
        CALL [fprintf]
        ADD esp, 4*2
    JMP LoopWords
    ;close the file
    PUSH DWORD [fileinfo]
    CALL [fclose]
    ADD ESP, 4
    
    End:
; call exit(0) ), 0 represents status code: SUCCESS
push dword 0 ; saves on stack the parameter of the function exit
call [exit] ; function exit is called in order to end the execution of the program
	

