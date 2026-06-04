"""
# math 함수 써서 푼 풀이

import math

def solution(n,m):
    gcd = math.gcd(n,m)
    lcm = (n*m)//gcd
    return [gcd,lcm]
"""

# 유클리드 호제법 통해서 푼 풀이

def solution(n,m):
    orginal_math=n*m
    
    while n>0:
        n,m=m%n,n
        
    gcd=m
    lcm=orginal_math//gcd
    
    return [gcd,lcm]
