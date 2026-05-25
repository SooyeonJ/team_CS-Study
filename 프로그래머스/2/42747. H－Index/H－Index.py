def solution(citations):
    
    citations.sort(reverse=True)
    H=0
    i=0
    while i<len(citations):
        if citations[i]>H:
            i+=1
            H+=1
        elif citations[i]<=H:
            return H
    return H
    
        
    
    
    