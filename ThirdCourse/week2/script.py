import re
filename = input("Input Filename: ")
try:
	hd = open(filename, 'r')
	integers = []
	summ = 0
	for line in hd:
		integers = list(map(int, re.findall("[0-9]+", line)))
		if len(integers)>0:
			summ = summ + sum(integers)
	print(summ)

except Exception as e:
	print("Wrong Input filename")
