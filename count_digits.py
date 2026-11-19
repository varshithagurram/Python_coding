"""n=int(input("Enter a number:"))
if n in range(0,10):
    print(1)
elif n in range(10,100):
    print(2)
elif n in range(100,1000):
    print(3)
elif n in range(1000,10000):
    print(4)
elif n in range(10000,100000):
    print(5)
elif n in range(100000,1000000):
    print(6)
elif n in range(1000000,10000000):
    print(7)"""
def count(n):
    a=0
    b=1
    while n>0:
     if n in range(10**a,10**b):
      return b
     a+=1
     b+=1
n=int(input("Enter a number:"))
print(count(n))
        
