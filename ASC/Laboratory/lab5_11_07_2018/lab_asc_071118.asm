bits 32
global start

extern exit, printf
import printf msvcrt.dll
import exit msvcrt.dll

segment date use32 class=data
	array db 1,2,3,4,5,6,7,8
	l equ $-array
	s db 0
	msg db 'the sum is %d', 10,13,0
segment code use32 class=code
start:
	mov ecx, l
	mov esi, 0
	mov bl, 0
	jecxz endc
	repeat:
		mov al, [array+esi]
		add bl, al
		inc esi
	loop repeat
	endc:
    mov [s], bl
    mov al, [s]
    cbw
    cwde
    push dword eax
    push dword msg
    call [printf]
    add esp, 4*2
    push    dword 0
    call    [exit]
