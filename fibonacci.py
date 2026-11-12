def fibonacci(n):
    arr = [0] * n
    arr[0] = 0
    arr[1] = 1
    for i in range(2,len(arr)):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr
n=int(input("Enter the number of terms:"))
ans=fibonacci(n)
print("terms of fibonacci series is:",ans)
