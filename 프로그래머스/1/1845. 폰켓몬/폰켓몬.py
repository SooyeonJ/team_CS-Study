def solution(nums):
    from collections import Counter
    return min(len(nums)//2, len(Counter(nums)))