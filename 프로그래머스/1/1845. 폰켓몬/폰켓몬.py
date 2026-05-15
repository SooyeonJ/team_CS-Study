def solution(nums):
    
    selectN = len(nums)//2
    
    if selectN>len(set(nums)):
        return len(set(nums))
    elif selectN<=len(set(nums)):
        return selectN