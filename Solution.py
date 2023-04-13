def missingNumber(nums):
    l=[0]*(len(nums)+1)
    for i in nums:
        l[i]=1
    return l.index(0)
m=[3,0,1]
print(missingNumber(m))