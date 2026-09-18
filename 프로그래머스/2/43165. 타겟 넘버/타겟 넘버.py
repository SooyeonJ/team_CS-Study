from itertools import product
def solution(numbers, target):    
  
    'product로 풀어보기'    
    l = [(x,-x) for x in numbers]
    
    s=list(map(sum,product(*l)))
    
    return s.count(target)
    
    
    
    
    
    
    
    
    
    
    
    '''
    def solution_2(i,current_sum):
        
        if i == len(numbers):
            if current_sum == target:
                return 1
            else:
                return 0
            
        return solution_2(i+1,current_sum+numbers[i])+solution_2(i+1,current_sum-numbers[i])
    
    return solution_2(0,0)
    '''                
            
        
            