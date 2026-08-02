from math import gcd

def solution(arr):
    answer=arr[0]
    for num in arr[1:]:
        answer=answer*num//gcd(answer,num)
    return answer





'''
'유클리드 호제법으로 최소공배수 계산'
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def solution(arr):
    answer=arr[0]
    for i in range(1,len(arr)):
        answer=answer*arr[i]//gcd(answer,arr[i])
        
    
    return answer
'''                

                   
            