def solution(x):
    
    result=list(map(int,str(x)))
    
    if x%sum(result)==0:
        return True
    else:
        return False
    
    
   