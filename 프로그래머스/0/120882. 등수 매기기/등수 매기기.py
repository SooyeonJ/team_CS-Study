def solution(score):
    answer = []
    avg_arr = []
    
    for i, j in enumerate(score):
        avg_arr.append(sum(j) / len(j))
        
    for val1 in avg_arr:
        rank = 1
        for val2 in avg_arr:       
            if val2 > val1:
                rank += 1
        answer.append(rank)
    return answer