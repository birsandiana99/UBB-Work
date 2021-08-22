bits 32
global _detMin
segment data public data use32
segment code public code use32
_detMin:
    push ebp
    mov ebp, esp
    sub esp, 4
    mov eax, [ebp+8]
    mov ebx, [ebp+12]
    cmp eax, ebx
    jbe final
    mov eax, ebx
    final:
    add esp, 4
    mov esp, ebp
    pop ebp
    ret