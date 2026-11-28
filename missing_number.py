arr=list(map(int,input("Enter the elements in an array with space:").split()))
for i in range(max(arr)+1):
    if i not in arr:
        print(i)