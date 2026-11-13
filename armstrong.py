def armstrong(n):
    sum=0
    while n>0:
        d=n%10
        sum=sum+(d**3)
        n=n//10
    return sum
n=int(input("Enter a number: "))
ans=armstrong(n)
if ans==n:
    print(n,"is an Armstrong number")
else:
  print(n,"is not an Armstrong number")