def factorial(i):
    i>0
    if i==1:
        return 1
    elif i!=1:
        return i*factorial(i-1)

def solution(n):
    
    return max([int(x) for x in range(1,11) if factorial(x)<=n])
    


    