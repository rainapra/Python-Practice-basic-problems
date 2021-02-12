name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
t = list()
for line in handle:
    if line.startswith('From '):
        word = line.find(':')
        hour = line[word-2:word]
        t.append(hour)
        t.sort()
    else:
        continue
dic = dict()
for time in t:
    dic[time] = dic.get(time,0) + 1

for time,count in dic.items():
    print(time,count)
