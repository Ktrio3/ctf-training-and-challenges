all: bof_nx bof_aslr bof_all bof_none overwriteStruct overwriteInt

overwriteInt: overwriteInt.c
	gcc -m32 -o overwriteInt overwriteInt.c

overwriteStruct: overwriteStruct.c
	gcc -m32 -o overwriteStruct overwriteStruct.c

bof_all: bof.c
	gcc -m32 -o bof_all bof.c

bof_aslr: bof.c
	gcc -m32 -z execstack -o bof_aslr -fno-stack-protector bof.c 

bof_nx: bof.c
	gcc -no-pie -m32 -o bof_nx -fno-stack-protector bof.c

bof_none: bof.c
	gcc -no-pie -z execstack -m32 -o bof_none -fno-stack-protector bof.c 

disable:
	echo "DISABLING ASLR UNTIL NEXT BOOT\n"
	sudo bash -c 'echo 0 > /proc/sys/kernel/randomize_va_space'

enable:
	echo "ENABLING ASLR\n"
	sudo bash -c 'echo 2 > /proc/sys/kernel/randomize_va_space'

clean:
	rm bof_nx bof_aslr overwriteStruct bof_none bof_all overwriteInt