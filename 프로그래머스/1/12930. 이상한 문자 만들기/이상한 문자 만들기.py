def solution(s):
    result=[]
    i=0
    for x in s:
        if x==' ':
            result.append(x)
            i=0
        else:
            if i%2==0:
                result.append(x.upper())
                i+=1
            else:
                result.append(x.lower())
                i+=1
                
    return ''.join(result)