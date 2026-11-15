def lcm(a,b):
    dict={}
    if a>b:
        large=a
        small=b
    else:
        large=b
        small=a
    for i in range(1,small+1):
        x=large*i
        dict[i]=x
    for j in dict.values():
        if j%small==0:
            return j
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
ans=lcm(a,b)
print("LCM of",a,"and",b,"is",ans)