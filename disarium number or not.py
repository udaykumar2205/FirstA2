#wap to check given number is disarium number or not.
n=int(input())
dummy=n
sum=0
L=len(str(n))
while dummy>0:
    rem=dummy%10
    dummy=dummy//10
    sum+=rem**L
    L=-1
if n==sum:
    print('n is disarium')
else:
    print('n is not disarium')
