# level3 pwn  
## x86
### some knowledge about GOT and PLT
GOT:Global Offset Table  
PLT:Procedure Linkage Table  
plt - got - real address

        The system function and /bin/sh string are in the link file  
        And we have the read function in our program,  
        So it's gonna be like payload1 = padding + write.plt + func + 1 + write.got() +4  
        The return address of write function is our vulnerable function so we got the same write address.
        and payload2 = padding + system + aaaa + binsh  
        system = libc.system + write.got - write.libc  
        binsh  = libc.binsh + write.got - write.libc
        
