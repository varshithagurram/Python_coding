def two_sum(nums,target):
    seen={}
    for i in range (len(nums)):
        needed=target-nums[i]
        if needed in seen:
            return (seen[needed],i)
        seen[nums[i]]=i
n=int(input("Enter the number of values:"))
nums=list(map(int,input().split()))
print(nums)
target=int(input("Enter the target value:"))
ans=two_sum(nums,target)
print(ans)