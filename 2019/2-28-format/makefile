all: format_all format_c format_vuln varg_sum
	
aslr:
	echo "TEMPORARILY DISABLING ASLR"
	echo 0 | sudo tee /proc/sys/kernel/randomize_va_space

format_vuln: format_vuln.c
	gcc -m32 -o format_vuln format_vuln.c -Wl,-z,norelro 

format_c: format_c.c
	gcc -m32 -o format_c format_c.c

format_all: format_all.c
	gcc -m32 -o format_all format_all.c

varg_sum: varg_sum.c
	gcc -m32 -o varg_sum varg_sum.c

clean:
	rm format_c format_all format_vuln varg_sum