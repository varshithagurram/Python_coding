arr=list(map(int,input("Enter elements of a sorted array with space in between:").split()))
seen=[]
for i in range (len(arr)):
    if arr[i] not in seen:
        seen.append(arr[i])

arr=seen
print(len(arr))