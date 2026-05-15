def solution(numbers):
    result=[]
    for i in range(len(numbers)):
        j=i+1
        while(j<len(numbers)):
            result.append(numbers[i]+numbers[j])
            j+=1
            

    return sorted(set(result))
        
   