name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
sen = list()
for line in handle:
    if line.startswith('From '):
        word = line.split()
        sen.append(word[1])
    else:
        continue
dic = dict()
for mail in sen:
    dic[mail] = dic.get(mail,0) + 1

maxcount = None
maxword = None
for mail,count in dic.items():
    if maxcount is None or count > maxcount:
        maxcount = count
        maxword = mail

print(maxword, maxcount)
