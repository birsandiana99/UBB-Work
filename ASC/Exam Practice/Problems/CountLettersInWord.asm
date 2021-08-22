
; we need to avoid multiple inclusion of this file
%ifndef _CLIW_ASM_ ; meh
%define _CLIW_ASM_ ; meh

; procedure definition
CountLettersInWord:
; void _stdcall CountLettersInWord(int &startWord,int &endWord,int string,int &letters)

    ; read the parameters from the stack
	MOV EAX, [ESP + 4*1];startWord
	MOV ECX, [ESP + 4*2];endWord
    MOV ESI, [ESP + 4*3];string
    MOV EBX, [ESP + 4*4];letters
    
    MOV BYTE [EBX],0;initialise number of letters with 0
    MOV EDX,0
    MOV DL,[EAX];get the start of the word to use as an index
    
    LoopLetters:
        
        CMP BYTE [ESI+EDX],0 ;check if the current character is 0
        JE WordEnd
        CMP BYTE [ESI+EDX],' ' ;check if the current character is a space
        JE WordEnd
        CMP BYTE [ESI+EDX],'z' ;check if the current character is greater than z
        JG NotLetter
        CMP BYTE [ESI+EDX],'a';check if the current character is lower than a
        JL NotLetter
        INC BYTE [EBX]
        NotLetter:
        INC DL;increment the index
        
        
    JMP LoopLetters
    WordEnd:

	ret
%endif