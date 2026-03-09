def solution(citations):
    answer = 0
    citations = sorted(citations)[::-1]
    
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            answer = i + 1
    
    return answer