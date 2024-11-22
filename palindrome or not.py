#wap to check given number is palindrome or not.
n=int(input())
dummy=n
rev=0
while dummy>0:
    rem=dummy%10
    dummy=dummy//10
    rev=rev*10+rem
if rev==n:
    print('n is palindrome')
else:
    print('n is not palindrome')
