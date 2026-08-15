def solution(n, lost, reserve):
    '체육복을 가져온 학생도 체육복을 도난당 할 수 있다고 가정-> set 이용'
    real_lost = set(lost)-set(reserve)
    real_reserve = set(reserve)-set(lost)
    
    '여벌 체육복이 있는 학생 앞/뒤 탐색해서 lost가 있는 경우 해당 순서를 remove한다.'
    for r in sorted(real_reserve):
        if r-1 in real_lost:
            real_lost.remove(r-1)
        elif r+1 in real_lost:
            real_lost.remove(r+1)
            
    return n-len(real_lost)
    
    
               
            
            
                
    
    
            
            
            
            