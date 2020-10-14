# Use words.txt as the file name
fname = input(Enter file name )
fh = open(fname, r)

print(fh.read().upper().rstrip())