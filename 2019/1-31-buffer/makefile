all: overwriteInt readString bof
	echo "DISABLING ASLR UNTIL NEXT BOOT\n"
	sudo bash -c 'echo 0 > /proc/sys/kernel/randomize_va_space'

readString: readString.c
	gcc -m32 -o readString readString.c

overwriteInt: overwriteInt.c
	gcc -m32 -o overwriteInt -fno-stack-protector overwriteInt.c

bof: bof.c
	gcc -no-pie -z execstack -m32 -o bof -fno-stack-protector bof.c 

disable:
	echo "DISABLING ASLR UNTIL NEXT BOOT\n"
	sudo bash -c 'echo 0 > /proc/sys/kernel/randomize_va_space'

enable:
	echo "ENABLING ASLR\n"
	sudo bash -c 'echo 2 > /proc/sys/kernel/randomize_va_space'

clean:
	rm overwriteInt readString bof