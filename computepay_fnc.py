def computepay(h,r):
    if h<=40:
        p=h*r
    else:
        p=(h*r) + (h-40)*0.5*r
    return p

hrs = input("Enter Hours:")
rate = input("Enter rate")
h=float(hrs)
r=float(rate)
p = computepay(h,r)
print("Pay",p)
