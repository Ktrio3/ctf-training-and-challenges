all: format example_format

example_format: example_format.c
	gcc -m32 example_format.c -o example_format

format: format.c
	gcc -m32 -fstack-protector format.c -o format

clean:
	rm format example_format
