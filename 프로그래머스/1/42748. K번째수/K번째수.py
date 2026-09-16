def solution(array, commands):
    '효율적인 알고리즘 : 리스트 컴프리핸션 사용'
    return [sorted(array[i-1:j])[k-1] for i,j,k in commands]
    
    
    
    '''
    result=[]
    result2=[]
    for x in commands:
        for y in x:
            result=sorted(array[x[0]-1:x[1]])
        result2.append(result[x[2]-1])
    return result2
    '''        
            
    
    
    