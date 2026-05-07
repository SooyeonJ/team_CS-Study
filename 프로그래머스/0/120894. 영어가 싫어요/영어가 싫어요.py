def solution(numbers):
    answer = []
    
    for i,x in enumerate(numbers):
        if 'one' in numbers[i:i+3]:
            numbers = numbers.replace('one','1')
        elif 'two' in numbers[i:i+3]:
            numbers = numbers.replace('two','2')
        elif 'three' in numbers[i:i+5]:
            numbers = numbers.replace('three','3')
        elif 'four' in numbers[i:i+4]:
            numbers = numbers.replace('four','4')
        elif 'five' in numbers[i:i+4]:
            numbers = numbers.replace('five','5')
        elif 'six' in numbers[i:i+3]:
            numbers = numbers.replace('six','6')
        elif 'seven' in numbers[i:i+5]:
            numbers = numbers.replace('seven','7')
        elif 'eight' in numbers[i:i+5]:
            numbers = numbers.replace('eight','8')
        elif 'nine' in numbers[i:i+4]:
            numbers = numbers.replace('nine','9')
        elif 'zero' in numbers[i:i+4]:
            numbers = numbers.replace('zero','0')
            
        
    return int(numbers)
        
        
        
        
            
      
            
           
        
