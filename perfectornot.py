n=int(input('Enter a number :'))

l=n
m=0
for i in range(1,n):
    if(n%i==0):
        m=m+i
if(m==l):
    print(m," is perfect number.")
else:
    print(l,' not perfect number.')