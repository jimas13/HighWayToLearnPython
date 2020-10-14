def Sort_Tuple(tup):
    return(sorted(tup, key = lambda x: x[0]))

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
count = dict()
handle = open(name)
for line in handle:
    if not line.startswith("From "): continue
    time = (line.split()[5]).split(':')[0]
    count[time] = count.get(time, 0) + 1
countlist = Sort_Tuple(count.items())
for item in countlist:
	print(item[0], item[1])
