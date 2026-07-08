def solution(s, n):
    result=[]
    
    for x in s:
        if x.isupper():
            ch=chr((ord(x)-ord('A')+n)%26+ord('A'))
            result.append(ch)
        elif x.islower():
            ch=chr((ord(x)-ord('a')+n)%26+ord('a'))
            result.append(ch)
        else:
            result.append(x)
            
        
    return ''.join(result)
            
    
    
        
    