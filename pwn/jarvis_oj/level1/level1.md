# level 1  
With no protection opened, it's a shellcode pwn.  
So from gdb we can see the offset is 0x88  
payload should be shellcode + padding + 'a'*4+ ra
