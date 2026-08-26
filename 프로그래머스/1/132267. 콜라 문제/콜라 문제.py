def solution(a, b, n):
    
    total=n
    result=0
    while total>=a:
        result+=b*(total//a)
        total=(total%a)+(b*(total//a))
    
    return result
        
    