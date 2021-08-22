bits 32 
global start

extern printf,scanf,exit,fprintf,fscanf,fopen,fclose,fread

import fread msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import exit msvcrt.dll
import scanf msvcrt.dll
import fscanf msvcrt.dll
import printf msvcrt.dll
import fprintf msvcrt.dll


segment data use32 class=data


segment code use32 class=code

start:

    push dword 0
    call [exit]