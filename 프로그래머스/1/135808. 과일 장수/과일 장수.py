def solution(k, m, score):
    heap=[]
    score.sort(reverse=True)
    answer=0
    
    for x in score:
        heap.append(x)
        if len(heap)==m:
            answer+=x*m
            heap=[]
        
    return answer
        
    