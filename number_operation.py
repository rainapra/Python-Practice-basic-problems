n=0
s=0
while True :
    num = input("Enter a number: ")
    if num =='done':
        break
    try:
        val = float(num)
    except:
        print("Invalid input")
        continue
    n = n+1
    s = s+val
print(n, s, s/n)
