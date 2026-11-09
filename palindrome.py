def palindrome(num):
    sum=0
    while (num>0):
     d=num%10
     sum=sum*10+d
     num=num//10
    return sum
n=int(input("enter the number:"))
sum=palindrome(n)
if sum==n:
     print("The given number is palindrome")
else:
 print("The given number is not palindrome")
 