#wap to find the sum of individual digits of given number.
n=int(input())
sum=0
while n>0:
    rem=n%10
    n=n//10
    sum+=rem
print(sum)
