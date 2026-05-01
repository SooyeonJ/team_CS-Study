def solution(array):
    dict={}
    
    for N in array:
        dict[N]=dict.get(N,0)+1
        
    max_value = max(dict.values())
    
    result = [k for k,v in dict.items() if v==max_value]
    
    if len(result)>1:
        return -1
    else :
        return result[0]
        
    

            

   