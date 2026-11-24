def btod(n):
    decimal=0
    power=1
    while n>0:
        d=n%10
        n=n//10
        decimal+=power*d
        power*=2
    return decimal
n=int(input("Enter a number in binary code:"))
ans=btod(n)
print("The decimal value of",n,"is:",ans)