def solution(s, n):
    result=[]
    for x in s:
        if x==' ':
            result.append(x)
        elif x.islower():
            if ord(x)+n>ord('z'):
                result.append(chr(ord(x)-26+n))
            else:
                result.append(chr(ord(x)+n))
        elif x.isupper():
            if ord(x)+n>ord('Z'):
                result.append(chr(ord(x)-26+n))
            else:
                result.append(chr(ord(x)+n))
    
    print(ord('z'),ord('Z'),ord('a'),ord('e'))
    return ''.join(result)


    
            
    
    
    
    
        
    