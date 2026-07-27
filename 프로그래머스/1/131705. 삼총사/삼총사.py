'''
def solution(number):
    
    sorted(number)
    
    count=0
    for i in range(len(number)-2):
        for j in range(i+1,len(number)-1):
            for z in range(j+1,len(number)):
                if number[i]+number[j]+number[z]==0:
                    count+=1
    if count!=0:
        return count
    else:
        return 0
'''

'combination 함수 쓰는 방법'
'itertools 모듈에 내장된 combinations 함수를 사용'
from itertools import combinations

def solution(number):
    
    count=0
    for x in combinations(number,3):
        if sum(x)==0:
            count+=1
    
    if count>0:
        return count
    else: return 0


    
    