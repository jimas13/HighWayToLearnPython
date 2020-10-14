def MaxCount(dictionaryitems):
    bigcount = 0
    bigword = None
    for email,count in dictionaryitems:
        if count > bigcount:
            bigword = email
            bigcount = count
	
    return [bigword, bigcount]

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
count = dict()
handle = open(name)
for line in handle:
    if not line.startswith("From "): continue
    email = line.split()[1]
    count[email] = count.get(email, 0) + 1
        
output = MaxCount(count.items())
print(output[0], output[1])


