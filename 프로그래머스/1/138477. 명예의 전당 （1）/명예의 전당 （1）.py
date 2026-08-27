def solution(k, score):
    'len(score)가 k보다 작은 경우도 고려해야함'
    hall = []
    result = []

    for s in score:
        hall.append(s)
        hall.sort(reverse=True)
        
        '슬라이싱의 장점 : 범위가 넘어가도 에러가 나지 않고 존재하는 개수만큼만 가져온다.'
        result.append(min(hall[:k]))
        
    return result
        
    
    
    
    
    
    
    
    
    '''
    처음 풀었던 풀이, k와 len(score) 어느 값이 더 작은지 고려하지 않아서 테스트 9,11에서 오류가 남
    less=score[0]
    listscore=[0]*k
    result=[]
    for i in range(k):
        listscore[i]=score[i]
        if score[i]<less:
            less=score[i]
        result.append(less)
    
    for j in range(k,len(score)):
        if score[j]>=less:
            listscore.remove(less)
            listscore.append(score[j])
            listscore.sort()
            less=listscore[0]
        result.append(less)
        
    return result
    '''    
            