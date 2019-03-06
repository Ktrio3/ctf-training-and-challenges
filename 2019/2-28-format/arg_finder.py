import sys

if len(sys.argv) > 1:

	if len(sys.argv) == 2:
		for i in range(1, int(sys.argv[1])+1):
			print "%d: %%p" % (i),
	else:
		for i in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
			print "%d: %%%d$p" % (i,i),
print
