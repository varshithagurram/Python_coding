def prime(n):
    i=2
    if n>1:
        while i<(int(n**0.5)+1):
            r=n%i
            if r==0:
               return "false"
            i+=1           
        else:
            return "true"
            
n=int(input("Enter the number:"))
ans=prime(n)
if ans=="false":
   print(n,"is not a prime number")
else:
    print(n,"is a prime number")