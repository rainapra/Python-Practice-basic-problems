lar=None
sm=None
while True :
    num = input("Enter a number: ")
    if num =='done':
        break
    try:
        val = int(num)
        if sm is None:
            sm = val
            lar = val
        elif val < sm:
            sm = val
        elif val > lar:
            lar = val
    except:
        print("Invalid input")
print('Maximum is', lar)
print('Minimum is', sm)
