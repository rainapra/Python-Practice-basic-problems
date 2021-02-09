n=input("Enter the number")
n=int(n)
a=1
while(a<=n):
    if (a%3==0 and a%5==0):
        print("FizzBuzz")
    elif (a%3==0):
        print("Fizz")
    elif (a%5==0):
        print("Buzz")
    else:
        print (str(a))
    a=a+1
