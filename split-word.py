fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    word = line.rstrip().split()
    for cha in word:
        if cha in lst:
            continue
        else:
            lst.append(cha)
lst.sort()
print(lst)
