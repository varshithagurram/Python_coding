def perfect(n):
    sum=0
    while n>0:
        for i in range(1,n):
            if n%i==0:
                sum=sum+i
        return sum
n=int(input("Enter a number:"))
ans=perfect(n)
if ans==n:
    print(n,"is a Perfect number")
else:
    print(n,"is not a Perfect number")