def solution(n):
    
    result=[]
    '3진법 변환 시 나누기를 멈추는 조건은 n>0이어야한다.'
    'n>1로 설저앟면, 마지막 남은 몫 n이 1일때 반복문이 종료되어 버리고, result.append(n)으로 들어가면서 나머지가 몫 1이 그대로 저장된다.'
    while n>0:
        n,a=n//3,n%3
        result.append(a)
    '리스트 역순으로 뒤집고 싶을 때, result[::-1]'
    '리스트[시작:끝:증감값] 형태로 동작한다. 시작과 끝을 비워두면 전체범위를 의미하고, 증감값에 -1을 넣으면 뒤에서부터 한칸씩 역순으로 뒤집은 새 리스트를 만들어낸다.'    
    return sum([x*(3**i) for i,x in enumerate(result[::-1])])
        
    
        
        
    
        