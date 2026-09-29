def two_sum(nums,target):
    seen={}
    for i in range (len(nums)):
        needed=target-nums[i]
        if needed in seen:
            return (seen[needed],i)
        seen[nums[i]]=i
nums=[2,4,7,3,1]
target=9
ans=two_sum(nums,target)
print(ans)