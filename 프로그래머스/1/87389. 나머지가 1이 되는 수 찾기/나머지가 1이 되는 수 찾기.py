def solution(n):
    
    
    return next(i for i in range(2, n) if n%i == 1)

    '''
    x=1
    while n<=1000000:
        if n%x==1:
            return x
        else: x+=1
    '''