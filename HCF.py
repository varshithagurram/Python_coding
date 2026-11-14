"""def hcf(a,b):
    if a>b:
        small=b
        large=a
    else:
        small=a
        large=b
    while small!=0:
      temp=large
      large=small
      small=large%small
    if small==0:
      return large
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
ans=hcf(a,b)
print("HCF of",a,"and",b,"is",ans)"""
def hcf(a,b):
    dict={}
    if a>b:
        small=b
    else:
        small=a
    for i in range(1,small+1):
        if a%i==0 and b%i==0:
            dict[i]=i
    return max(dict.values())
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
ans=hcf(a,b)
print("HCF of",a,"and",b,"is",ans)