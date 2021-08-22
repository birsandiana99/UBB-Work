bits 32

; informam asamblorul ca dorim ca functia _calcStuff sa fie disponibila altor unitati de compilare
global _calcStuff

; linkeditorul poate folosi segmentul public de date si pentru date din afara
segment data public data use32

; codul scris in asamblare este dispus intr-un segment public, posibil a fi partajat cu alt cod extern
segment code public code use32

; int calcStuff(int, int, int)
; conventie cdecl
_calcStuff:
    ; creare cadru de stiva pentru programul apelat
    push ebp
    mov ebp, esp
    
    ; obtinem argumentele transmise pe stiva functiei calcStuff
    ; la locatia [ebp+4] se afla adresa de return (valoarea din EIP la momentul apelului)
    ; la locatia [ebp] se afla valoarea ebp pentru apelant
    mov eax, [ebp + 8]      ; eax <- a
    
    mov ebx, [ebp + 12]     ; ebx <- b
	
	mov ecx, [ebp + 16] 	; ecx <- c
    
	add eax, ebx ; eax = a + b
	sub eax, ecx ; eax = a + b - c

    ; refacem cadrul de stiva pentru programul apelant
    mov esp, ebp
    pop ebp

    ret
    ; conventie cdecl - este responsabilitatea programului apelant sa elibereze parametrii transmisi