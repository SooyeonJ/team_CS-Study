def solution(nums):
    hash={}
    nums.sort()
    
    for x in nums:
        hash[x]=hash.get(x,0)+1
        
    
    if len(hash.keys())>=len(nums)//2:
        return len(nums)//2
    else:
        return len(hash.keys())