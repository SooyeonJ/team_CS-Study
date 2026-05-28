def solution(clothes):
    hash={}
    
    for x,y in clothes:
        hash[y]=hash.get(y,0)+1
        
    print(hash)
    answer=1
    for count in hash.values():
        answer*=(count+1)
            
    return answer-1
        
        
        
        
       
        
    