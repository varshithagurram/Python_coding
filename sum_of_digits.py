def sumofdigits(n):
    digits=[]
    while n>0:
        d=n%10
        digits.append(d)
        n=n//10
    return sum(digits)
n=int(input("Enter a number:"))
ans=sumofdigits(n)
print("The sum of digits of",n,"is:",ans)