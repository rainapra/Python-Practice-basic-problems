def pr_count(start,n):
    s=[]
    count=1
    while count<=n:
        if(start % 2 ==0):
            s.append(start)
            count += 1
        else:
            False
        start += 1
    return s

start = input("Enter first number")
n = input("Enter number of prime numbers you want to see")

start = int(start)
n = int(n)
s = pr_count(start,n)
print ("Prime numbers: ", s)
