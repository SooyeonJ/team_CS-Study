def solution(lines):
    result = [0]*500
    
    for start,end in lines:
        for i in range(start,end):
            result[i+100]+=1
    
    answer=0
    for count in result:
        if count>=2:
            answer+=1
            
    return answer
        
        
  