def solution(n):

    answer=[]
    
    while n>0:
        x,n=n%3,n//3
        answer.append(str(x))

    return int(''.join(answer),3)

        
    
        
        
    
        