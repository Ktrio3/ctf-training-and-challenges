all: noargs onearg multiarg

noargs: noargs.c
	gcc -no-pie -m32 -o noargs -fno-stack-protector noargs.c 

onearg: onearg.c
	gcc -no-pie -m32 -o onearg -fno-stack-protector onearg.c 

multiarg: multiarg.c
	gcc -no-pie -m32 -o multiarg -fno-stack-protector multiarg.c 

disable:
	echo "DISABLING ASLR UNTIL NEXT BOOT\n"
	sudo bash -c 'echo 0 > /proc/sys/kernel/randomize_va_space'

enable:
	echo "ENABLING ASLR\n"
	sudo bash -c 'echo 2 > /proc/sys/kernel/randomize_va_space'

clean:
	rm noargs onearg multiarg