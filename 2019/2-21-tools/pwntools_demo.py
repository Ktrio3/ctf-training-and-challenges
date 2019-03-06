from pwn import *

# Open a "remote" connection
def show_local_remote():
	try:
		c = remote("localhost", 2000)
	except:
		return
	c.sendline("Please write 'me'")

	print c.recvuntil("me") # Wait until nc writes "me" 
	print c.recvline()
	c.interactive() # Switch over to an interactive session

# Connects to localhost over ssh. Could be another remote server
def show_ssh():
	c = ssh(host="localhost", user="test", password="test")
	c.interactive()

# Connects to localhost over ssh, then starts a process
def ssh_proc():
	c = ssh(host="localhost", user="test", password="test")
	p = c.process("python")
	p.interactive()

# Shows off the default byte packing functions
def p32Demo():
	print "\xde\xad\xba\xbe"
	print "\xde\xad\xba\xbe".encode("hex")
	print p32(0xcafebabe).encode("hex")
	print p32(0xcafebabe, endian="big").encode("hex")
	print p64(0xdeadbeef).encode("hex")

def gdb_proc():
	#gdb.debug("./a.out") # Attaches GDB, and stops at first instruction
	
	# One way to start GDB, however, the 
	# process may terminate before GDB attaches
	# p = process("bash")
	# gdb.attach(p)
	# p.interactive()

def local_proc():
	p = process(["python"])
	p.sendline('print "Hi there from python!"')
	p.shutdown('send')
	print p.recvall()

def menu():
	while True:
		print "1. Remote 2. SSH 3. SSH Process 4. p32 5. GDB 6. Proc: ", 
		try:
			i = input()
		except:
			break
		if i is 1:
			show_local_remote()
		elif i is 2:
			show_ssh()
		elif i is 3:
			ssh_proc()
		elif i is 4:
			p32Demo()
		elif i is 5:
			gdb_proc()
		elif i is 6:
			local_proc()
		else:
			break
		print "\n"

if __name__ == "__main__":
	menu()