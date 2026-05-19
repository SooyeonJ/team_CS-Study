def solution(x):
    
    a=0
    b=x
    while b!=0:
        a+=b%10
        b=b//10
    
    if x%a==0:
        return True
    else:
        return False