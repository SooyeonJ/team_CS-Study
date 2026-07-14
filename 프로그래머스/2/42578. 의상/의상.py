def solution(clothes):
    
    hash={}
    result=1
    
    for x,y in clothes:
        hash[y]=hash.get(y,0)+1
        
    for value in hash.values():
        result*=value+1
        
    return result-1
    
    '''
    조합론(경우의 수)로 생각한다.
    (N+1)(M+1)로 했을 때, +1은 아무것도 입지않은 경우이다.
    (N+1)(M+1) = NM + N + M + 1

    - NM: N과 M을 모두 사용하는 경우
    - N: N만 사용하는 경우
    - M: M만 사용하는 경우
    - 1: 모두 사용하지 않는 경우
    '''
    
   
        
       
    