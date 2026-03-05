def solution(nums):
    max_pick = len(nums)//2
    kind = len(set(nums))
    return min(max_pick,kind)