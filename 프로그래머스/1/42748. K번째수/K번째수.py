def solution(array, commands):
    result=[]
    result2=[]
    for x in commands:
        for y in x:
            result=sorted(array[x[0]-1:x[1]])
        result2.append(result[x[2]-1])
    return result2
            
            
    
    
    