def solution(s):
    answer = list(map(str,s.split()))
    result=0
    for i,x in enumerate(answer):
        if(x!='Z'):
            result+=int(x)
        elif(x=='Z'):
            result-=int(answer[i-1])
    
    return result
           
            
        
        
        
