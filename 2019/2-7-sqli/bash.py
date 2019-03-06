import os

print "Hello! I am your personal logging assistant."

print "Give me a string to log: ",

myLogString = raw_input()

# For debugging purposes:

print "Ok, running:\n echo '%s' >> /tmp/log.txt" % myLogString

# A faster way to write to log than opening it :)
os.system("echo '%s' >> /tmp/log.txt" % myLogString)
