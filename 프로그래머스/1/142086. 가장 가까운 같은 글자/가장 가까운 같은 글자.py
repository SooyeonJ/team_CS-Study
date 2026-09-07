def solution(s):
    '딕셔너리 활용 : 문자를 key로, 해당 문자가 마지막으로 등장한 index를 value로 저장'
    answer=[]
    last_seen={}
    
    for i, char in enumerate(s):
        if char in last_seen:
            '이전 위치와의 거리 계산'
            answer.append(i-last_seen[char])
        else:
            '처음 등장한 경우'
            answer.append(-1)
                         
        '현재 문자의 마지막 위치 업데이트'
        last_seen[char]=i
        
    return answer
    
    
    
    
    
    
    '''
    answer = []
    result= []
    sol=''
    for x in s:
        if x not in answer:
            answer.append(x)
            result.append(-1)
        elif x in answer:
            sol=[i for i,x in enumerate(answer) if answer[i]==x]
            result.append(max(sol))
            
    
    return result
    '''        