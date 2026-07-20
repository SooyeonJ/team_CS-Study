'''
내가 풀었던 방식
--------------------------------------
def anw(a):
    count=0
    result=[]
    for x in range(1,a+1):
        if x*x==a:
            count+=1
        else:
            if a%x==0:
                count+=1
    return count
        

def solution(left,right):
    sol=[]
    for result in range(left,right+1):
        if anw(result)%2==0:
            sol.append(result)
        else: sol.append(-result)
    
    return sum(sol)
'''

'제곱근을 이용한 풀이 방법'

def solution(left,right):
    answer=0
    for i in range(left,right+1):
        '완전 제곱수인지 확인하는 것, 완전 제곱수는 루트를 씌워도 실수가 아닌 정수가 나오기 때문'
        if int(i**0.5)==i**0.5:
            answer-=i
        else:
            answer+=i
    return answer
    

        
            
            
