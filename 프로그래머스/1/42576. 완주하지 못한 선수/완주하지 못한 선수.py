def solution(participant, completion):
   
    
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i]!=completion[i]:
            return participant[i]
        
    return participant[-1]

    ''''
    hash={}
    
    for x in participant:
        hash[x]=hash.get(x,0)+1
        
    for y in completion:
        hash[y]-=1
        
    for key in hash:
        if hash.get(key)>0:
            return key
    '''        
        

            
        
        
   