def solution(answers):
    unmath1 = [1,2,3,4,5]*2000
    unmath2 = [2, 1, 2, 3, 2, 4, 2, 5]*1250
    unmath3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000
    
    count = [0,0,0]
    for i,x in enumerate(answers):
        if unmath1[i]==x:
            count[0]+=1
        if unmath2[i]==x:
            count[1]+=1
        if unmath3[i]==x:
            count[2]+=1
        
    max_value = max(count)
    
    return [i+1 for i,x in enumerate(count) if x==max_value]
            
        
    
