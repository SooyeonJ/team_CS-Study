from collections import Counter

def solution(participant, completion):
    return ''.join(list(Counter(participant) - Counter(completion)))