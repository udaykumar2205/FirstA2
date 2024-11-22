#wap to check the given perfect number or not.
n=int(input())
ds=0
i=1
while i<=n//2:
    if n%i==0:
        ds+=i
        i+=1
if n==ds:
    print('n is perfect')
else:
    print('n is not perfect')
