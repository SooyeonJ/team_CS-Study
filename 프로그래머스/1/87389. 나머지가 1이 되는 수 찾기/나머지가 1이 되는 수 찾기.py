def solution(n):
    
    x=1
    while n<=1000000:
        if n%x==1:
            return x
        else: x+=1