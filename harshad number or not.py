#wap to check given number is harshad number or not.
n=int(input())
dummy=n
sum=0
while dummy>0:
    rem=dummy%10
    dummy=dummy//10
    sum+=rem
if n%sum==0:
    print('n is harshad')
else:
    print('n is not harshad')
