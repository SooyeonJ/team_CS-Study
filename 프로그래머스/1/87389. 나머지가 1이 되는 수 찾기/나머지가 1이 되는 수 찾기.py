def solution(n):
    x=1
    while(n!=1000001):
        if(n%x==1):
            return x
        else:
            x+=1
        