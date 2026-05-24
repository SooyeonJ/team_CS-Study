def solution(progresses, speeds):
    
    last_work = [(100-x+y-1)//y for x,y in zip(progresses,speeds)]
    result=[]
    
    
    while last_work:
        current = last_work.pop(0)
        count = 1
        
        while last_work and last_work[0]<=current:
            last_work.pop(0)
            count+=1
    
        result.append(count)
    
    return result
            
            
    
    
        
            