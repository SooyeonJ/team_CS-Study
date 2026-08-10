def solution(arr):
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
    answer=[]
    for x in arr:
        if len(answer) == 0 or answer[-1]!=x:
            answer.append(x)
            
    return answer
    
    
    '''
    sol=[]
    for i,j in zip(arr,arr[1:]):
        if i!=j:
            sol.append(i)
    
    if len(sol)==0 and len(arr)!=0:
        return [arr[0]]
    elif len(arr)!=0 and sol[-1]!=arr[-1]:
        sol.append(arr[-1])
        
    return sol
   '''          
    

    
 