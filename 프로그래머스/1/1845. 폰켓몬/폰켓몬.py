from collections import Counter
def solution(nums):
    answers = min(len(Counter(nums).keys()), int(len(nums)/2))
    return answers