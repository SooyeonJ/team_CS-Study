def gcd(a,b):
    
    while b!=0:
        tmp=a
        a=b
        b=tmp%b
        
    return a

def solution(numer1, denom1, numer2, denom2):
        
    num = numer1*denom2 + numer2*denom1
    denom = denom1*denom2
        
    return [num//gcd(num,denom),denom//gcd(num,denom)]