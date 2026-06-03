def solution(numbers):
    
    str_numbers=[str(x) for x in numbers]
    
    max_numbers=sorted(str_numbers, key=lambda x:x*3, reverse=True)
  
    if max_numbers[0]=='0':
        return '0'
    else:
        return ''.join(max_numbers)
    
    
    
    
        
    
    
    
            
            
    

    
    
            
        
   
        
    