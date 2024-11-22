#wap to check given number os armstrong number or not.
n=int(input())
dummy=n
sum=0
L=len(str(n))
while dummy>0:
    rem=dummy%10
    dummy=dummy//10
    sum+=rem**L
if n==sum:
    print('n is armstrong')
else:
    print('n is not armstrong')
   
