from collections import Counter
def solution(nums):
    ans = min(len(Counter(nums).keys()), int(len(nums)/2))
    return ans