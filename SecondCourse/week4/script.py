fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    templist = line.rstrip().split()
    for word in templist:
    	if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
