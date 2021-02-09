# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
r = fh.read()
r = r.upper()
r = r.rstrip()
print (str(r))
