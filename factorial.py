def factorial(n):
    factorial=1
    if n==0 or n==1:
        return 1
    else:
     for i in range(1,n+1):
       factorial=factorial*i
     return factorial
n=int(input("Enter the number:"))
ans=factorial(n)
print("Factorial of",n,"is",ans)
    