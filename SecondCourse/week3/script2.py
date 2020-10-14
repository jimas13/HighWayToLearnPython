# Use the file name mbox-short.txt as the file name
def GetNumeric(str):
	return float(str[str.find('0'):str.find('0')+6])

s = 0.0
count = 0
fname = input("Enter file name: ")
fh = open(fname, "r")
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
        s= s + GetNumeric(line)
        count = count + 1
print("Average spam confidence:", s/count)
