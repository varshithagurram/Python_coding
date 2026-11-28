arr=list(map(int,input("Enter elements in an array with space:").split()))
sorted=sorted(arr)
second_largest=sorted[-2]
print("The second largest element in the array is:",second_largest)
print(sorted)